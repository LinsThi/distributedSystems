import socket, threading
from utils import *

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
            print(f"Conexão de {client_address} estabelecida.")

            client_socket.send("Digite seu nome de usuário: ".encode('utf-8'))
            username = client_socket.recv(1024).decode('utf-8')
            client_socket.send("Digite sua senha: ".encode('utf-8'))
            password = client_socket.recv(1024).decode('utf-8')
            login(username, password, client_socket)
            # login('admin', '123', client_socket)
            # login('antonio', '123', client_socket)
    except Exception as e:
        print("Listen socket:", str(e))

if __name__ == "__main__":
  server()