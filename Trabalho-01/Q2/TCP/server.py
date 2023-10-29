import socket, threading

from Q1.entities.PessoaOutputSteam import PessoaOutputStream
from Q2.entities.PessoaInputStream import PessoaInputStream
from Q1.entities.OutputStream import *
from Q2.entities.InputStream import *

tcp_input_stream = PessoaInputTCPStream()
pessoa_input_stream = PessoaInputStream([], tcp_input_stream)
print_stream = PessoaPrintStream();
pessoa_output_stream = PessoaOutputStream(pessoa_input_stream.people, print_stream)

def server():
    server_host = "192.168.0.2"
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
            data = self.client_socket.recv(1024).decode('utf-8')
            pessoa_input_stream.read_system(str(data))
            self.client_socket.send(pessoa_output_stream.write_system())
        except Exception as e:
            print("Error:", str(e))
        finally:
            self.client_socket.close()

if __name__ == "__main__":
    server()