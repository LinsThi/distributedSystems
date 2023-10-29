import io
from Q1.TCP.client import client

class OutputStream (io.IOBase):
   def write(self, title, people):
     pass

class PessoaPrintStream (OutputStream):
   def write(self, title, people):
      print(title)

      for person in people:
        name_bytes = len(person.name.encode('utf-8'))
        cpf_bytes = len(str(person.cpf).encode('utf-8'))
        age_bytes = len(str(person.age).encode('utf-8'))

        total_bytes = name_bytes + cpf_bytes + age_bytes

        print(f'Nome: {person.name} ({name_bytes} Bytes), CPF: {person.cpf} ({cpf_bytes} Bytes), Idade: {person.age} ({age_bytes} Bytes), Total de bytes utilizados: {total_bytes}')
   
class PessoaFileStream (OutputStream):
   def write(self, title, people):
      file = open('Q1/result/peoples_q1.txt', 'w')
      string_out = title
      
      for person in people:
          name_bytes = len(person.name.encode('utf-8'))
          cpf_bytes = len(str(person.cpf).encode('utf-8'))
          age_bytes = len(str(person.age).encode('utf-8'))

          total_bytes = name_bytes + cpf_bytes + age_bytes

          string_out += f'Nome: {person.name} ({name_bytes} Bytes), CPF: {person.cpf} ({cpf_bytes} Bytes), Idade: {person.age} ({age_bytes} Bytes), Total de bytes utilizados: {total_bytes}\n'

      file.write(string_out)
      file.close()
   
class PessoaTCPStream (OutputStream):
   def write(self, title, people):
      message = title
      
      for person in people:
        name_bytes = len(person.name.encode('utf-8'))
        cpf_bytes = len(str(person.cpf).encode('utf-8'))
        age_bytes = len(str(person.age).encode('utf-8'))

        total_bytes = name_bytes + cpf_bytes + age_bytes

        message += f'\nNome: {person.name} ({name_bytes} Bytes), CPF: {person.cpf} ({cpf_bytes} Bytes), Idade: {person.age} ({age_bytes} Bytes), Total de bytes utilizados: {total_bytes}'

      client(message)