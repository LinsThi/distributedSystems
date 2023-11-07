import socket

def client():
    server_host = "192.168.0.7"
    server_port = 7896
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_host, server_port))

        data = s.recv(1024).decode('utf-8')
        print("Received: ", data)
    except ConnectionRefusedError:
        print("Connection refused.")
    except Exception as e:
        print("Error:", e)
    finally:
        s.close()

if __name__ == "__main__":
    client()