from typing import List

# Classe base para Meios de Transporte
class Transport:
    """
    Transport class

    :param model: Model of the transport
    :param capacity: Capacity of the transport
    :param fuel_efficiency: Fuel efficiency of the transport
    """
    def __init__(self, model, capacity, fuel_efficiency):
        self.model = model
        self.capacity = capacity
        self.fuel_efficiency = fuel_efficiency

    def __str__(self):
        return f"Model: {self.model}\nCapacity: {self.capacity}\nFuel Efficiency: {self.fuel_efficiency}"

# Subclasses de Meios de Transporte
class Car(Transport):
    def __init__(self, model, capacity, fuel_efficiency, trunk_space):
        super().__init__(model, capacity, fuel_efficiency)
        self.trunk_space = trunk_space

    def __str__(self):
        return super().__str__() + f"\nTrunk Space: {self.trunk_space}"

class Truck(Transport):
    def __init__(self, model, capacity, fuel_efficiency, payload_capacity):
        super().__init__(model, capacity, fuel_efficiency)
        self.payload_capacity = payload_capacity

    def __str__(self):
        return super().__str__() + f"\nPayload Capacity: {self.payload_capacity}"

class Bus(Transport):
    def __init__(self, model, capacity, fuel_efficiency, passenger_count):
        super().__init__(model, capacity, fuel_efficiency)
        self.passenger_count = passenger_count

    def __str__(self):
        return super().__str__() + f"\nPassenger Count: {self.passenger_count}"

class Motorcycle(Transport):
    def __init__(self, model, capacity, fuel_efficiency, has_sidecar):
        super().__init__(model, capacity, fuel_efficiency)
        self.has_sidecar = has_sidecar

    def __str__(self):
        sidecar_str = "Yes" if self.has_sidecar else "No"
        return super().__str__() + f"\nHas Sidecar: {sidecar_str}"

class RentalCompany:
    def __init__(self, name):
        self.name = name
        self.vehicles = []

    def add_vehicles(self, *vehicles):
        for vehicle in vehicles:
            self.vehicles.append(vehicle)

    def __str__(self):
        vehicles_str = ",\n".join([str(vehicle) for vehicle in self.vehicles])
        return f"RentalCompany\n\tName: {self.name}\n\tVehicles: [\n{vehicles_str}]"
