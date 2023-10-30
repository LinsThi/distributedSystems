import socket
import json
from utils import serialize, deserialize

from rental import RentalCompany, Car, Truck, Bus, Motorcycle

from pprint import pprint

def client(host="localhost", port=6789):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip_address = socket.gethostbyname(host)

        rental_company = RentalCompany("Rent-A-Car")
        car1 = Car("Sedan", 5, 30, 15)
        truck1 = Truck("Pickup", 2, 15, 2000)
        bus1 = Bus("Tour Bus", 40, 8, 50)
        motorcycle1 = Motorcycle("Sport Bike", 1, 50, False)
        
        print("Sending data to server...")
        rental_company.add_vehicles(car1, truck1, bus1, motorcycle1)

        client_socket.sendto(serialize(rental_company), (ip_address, port))

        print("Waiting for response...")

        data, server_address = client_socket.recvfrom(1024)
        response = json.loads(data)

        pprint(response)
        client_socket.close()

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    client("192.168.0.2", 6789)