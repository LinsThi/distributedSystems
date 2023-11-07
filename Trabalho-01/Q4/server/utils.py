import json, os, threading
from time import sleep

timer = 3
# Obtenha o diretório atual do script
current_dir = os.path.dirname(__file__)
json_path = os.path.join(current_dir, '../database/db.json')
clients_list = []
vote_finalized = False

def read_data():
  with open(json_path, 'r') as file:
    return json.load(file)

def save_data(data):
  with open(json_path, 'w') as file:
    json.dump(data, file, indent=2)

def menu_admin(client_socket):
  message = ''
  
  while True:
    message = '--------------------------------\n'
    message += '1 - Transmitir uma mensagem\n'
    message += '2 - Adicionar candidato\n'
    message += '3 - Remover candidato\n'
    message += '4 - Finalizar votação\n'
    message += '--------------------------------\n'
    client_socket.send(message.encode('utf-8'))

    sleep(1)

    message = f"get_value:Olá Admin, o que você deseja fazer:"
    client_socket.send(message.encode('utf-8'))
    admin_option = int(client_socket.recv(1024).decode('utf-8'))

    if(admin_option == 1):
      client_socket.send(f"get_value:Digite a messagem".encode('utf-8'))
      message = str(client_socket.recv(1024).decode('utf-8'))
      admin_message(message)
    if(admin_option == 2):
      client_socket.send(f"get_value:Digite o nome do candidato que você deseja adicionar:".encode('utf-8'))
      candidate_name = str(client_socket.recv(1024).decode('utf-8'))
      client_socket.send(f"get_value:Digite o número do candidato que você deseja adicionar:".encode('utf-8'))
      candidate_number = int(client_socket.recv(1024).decode('utf-8'))
      
      client_socket.send(admin_add_candidate(candidate_name, candidate_number).encode('utf-8'))
    if(admin_option == 3):
      client_socket.send(f"get_value:Digite o número do candidato que você deseja remover:".encode('utf-8'))
      candidate_number = int(client_socket.recv(1024).decode('utf-8'))
      client_socket.send(admin_remove_candidate(candidate_number).encode('utf-8'))
    if(admin_option == 4):
       message = print_candidates_and_votes().encode('utf-8')
       client_socket.send(message)

def admin_message(message):
    for client_connection in clients_list:
       print(message)
       client_connection.send(message.encode('utf-8'))
  
def admin_add_candidate(candidate_name, candidate_number):
    # Carregue os dados do arquivo JSON
    data = read_data()

    # Verifique se o número do candidato já existe
    for candidate in data['candidates']:
      if candidate['number'] == candidate_number:
        return "Já existe um candidato com esse número. Escolha um número diferente."

    new_candidate = {
        "number": candidate_number,
        "name": candidate_name,
        "nvotes": 0
    }
    data['candidates'].append(new_candidate)
    # Salve os dados atualizados no arquivo JSON
    save_data(data)
    return f"Candidato {candidate_name} com número {candidate_number} foi adicionado com sucesso."

def admin_remove_candidate(candidate_number):
    # Carregue os dados do arquivo JSON
    data = read_data()
    # Encontre e remova o candidato com o número especificado
    for candidate in data['candidates']:
      print(candidate['number'], candidate_number, candidate['number'] == candidate_number)
      if candidate['number'] == candidate_number:
        data['candidates'].remove(candidate)
        # Salve os dados atualizados no arquivo JSON
        save_data(data)
        return f"Candidato com número {candidate_number} foi removido com sucesso."
    else:
      return f"Nenhum candidato encontrado com o número {candidate_number}."

# Função para fazer login
def login(username, password, socket):
    data = read_data()

    # Verifique se o usuário e a senha correspondem
    for user in data['users']:
      if user['user'] == username and user['pass'] == password:
        clients_list.append(socket)
        if user['isAdmin']:
          menu_admin(socket)
          break
        else:
           menu_user(user, socket)
           break
    else:
      socket.send("Credenciais de login incorretas.".encode('utf-8'))

def menu_user(username, client_socket):
  while True:
    message = '---------------Menu---------------\n'
    message += '1 - Exibir candidatos\n'
    message += '2 - Votar em um candidato\n'
    message += '3 - Sair\n'
    message += '----------------------------------\n'
    client_socket.send(message.encode('utf-8'))

    sleep(1)

    message = f"get_value:Olá {username['name']}, o que você deseja fazer:"
    client_socket.send(message.encode('utf-8'))
    user_option = int(client_socket.recv(1024).decode('utf-8'))
    
    if(user_option == 1):   
      client_socket.send(print_candidates().encode('utf-8'))
    if(user_option == 2):
      if vote_finalized:
          client_socket.send("Votação já foi finalizada\n\n".encode('utf-8')) 
      else:
        if username['isAlreadyVote'] == True:
          client_socket.send("Você já votou.\n\n".encode('utf-8'))
        else:
          client_socket.send(f"get_value:Digite o número do candidato em quem você deseja votar:".encode('utf-8'))
          candidate_number = int(client_socket.recv(1024).decode('utf-8'))
          client_socket.send(vote_candidate(candidate_number).encode('utf-8'))
    if(user_option == 3):
      client_socket.send('exit:Fechando sistemas...'.encode('utf-8'))
      break

def vote_candidate(candidate_number):
    data = read_data()

    for candidate in data['candidates']:
        if candidate['number'] == candidate_number:
            candidate['nvotes'] += 1
            save_data(data)
            return "Seu voto foi registrado."
    else:
        return "Número de candidato inválido. Por favor, escolha um candidato válido."

def print_candidates():
  # Carregue os dados do arquivo JSON
  data = read_data()

  message = "Candidatos:\n"

  border_char = "-"
  border_width = 26
  message += border_char * border_width+"\n"

  for candidate in data['candidates']:
    message +=f"| {candidate['name']} - Número {candidate['number']} |\n"

  message +=border_char * border_width + "\n"
  return message

def print_candidates_and_votes():
    # Carregue os dados do arquivo JSON
    data = read_data()

    message = "\nCandidatos e a quantidade de votos:\n"

    # Ordene a lista de candidatos pelo número de votos em ordem decrescente
    sorted_candidates = sorted(data['candidates'], key=lambda x: x['nvotes'], reverse=True)

    border_char = "-"
    border_width = 40
    message += border_char * border_width + '\n'

    for candidate in sorted_candidates:
      message += f"| {candidate['name']} - Número {candidate['number']} = {candidate['nvotes']} votos      |\n"

    message += border_char * border_width + '\n'
    return message
