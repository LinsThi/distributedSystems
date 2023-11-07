import socket

def client():
    server_host = "192.168.0.8"
    server_port = 7896

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_host, server_port))

        username = input(client_socket.recv(1024).decode('utf-8'))
        client_socket.send(username.encode('utf-8'))

        password = input(client_socket.recv(1024).decode('utf-8'))
        client_socket.send(password.encode('utf-8'))

        while True:
            message = client_socket.recv(1024).decode('utf-8')

            array_splited = message.split(':')

            if array_splited[0] == 'get_value':
                user_option = input(array_splited[1] + ' ')
                client_socket.send(user_option.encode('utf-8'))
            if array_splited[0] == 'exit':
                print(array_splited[1])
                client_socket.close()
            else:
                removeOperation = message.split(':')
                print(removeOperation[len(removeOperation) - 1])
    
    except ConnectionRefusedError:
        print("Connection refused.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
  client()