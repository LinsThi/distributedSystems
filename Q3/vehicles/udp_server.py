import socket
import json
from rental import RentalCompany
from utils import serialize, deserialize

def response(rental_company: RentalCompany):
    response = {
        "content": {
            "name": rental_company.name,
            "vehicles": [str(vehicle) for vehicle in rental_company.vehicles]
        },
        "status": "success"
    }
    return json.dumps(response).encode('utf-8')


def server(port=6789):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_port = port
        server_socket.bind(('192.168.0.7', server_port))
        print("Server is listening on port", server_port)
        while True:

            data, client_address = server_socket.recvfrom(4096)
            client_ip, client_port = client_address
            print("Received connection from client with IP:", client_ip, "and port:", client_port)

            received_obj = deserialize(data)

            if isinstance(received_obj, RentalCompany):
                print(f"Received data for Rental Company: [{str(received_obj)}]")
            else:
                print("Received unknown data")

            server_socket.sendto(make_response(received_obj), client_address)

    except Exception as e:
        print("Error:", str(e))
    finally:
        server_socket.close()


if __name__ == "__main__":
    server(6789)