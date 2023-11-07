import socket, threading

from Q1.entities.Pessoa import Pessoa
from Q1.entities.PessoaOutputSteam import PessoaOutputStream
from Q1.entities.OutputStream import *

output_print_stream = PessoaOutputPrintStream();
people_list = [Pessoa('Marcos', 123456789, 30), Pessoa('Judite', 123456789, 23) ]
pessoa_output_stream = PessoaOutputStream(people_list, output_print_stream)

def server():
    server_host = "192.168.0.8"
    server_port = 7896
    
    try:
        print("Server started")
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.bind((server_host, server_port))
        listen_socket.listen(5)
        
        while True:
            client_socket, client_address = listen_socket.accept()
            print(client_address)
            print("connection established")
            connection = Connection(client_socket)
            connection.start()
    except Exception as e:
        print("Listen socket:", str(e))

class Connection(threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
    
    def run(self):
        try:
            message = pessoa_output_stream.write_system()
            self.client_socket.send(message.encode('utf-8'))
        except Exception as e:
            print("Error:", str(e))
        finally:
            self.client_socket.close()

if __name__ == "__main__":
    server()