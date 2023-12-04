export class RentalCompany {
  constructor(name) {
    this.name = name;
    this.vehicles = [];
  }

  addVehicles(...vehicles) {
    vehicles.forEach((vehicle) => {
      this.vehicles.push(vehicle);
    });
  }

  toString() {
    const vehiclesStr = this.vehicles
      .map((vehicle) => vehicle.toString())
      .join(",\n");
    return `RentalCompany\n\tName: ${this.name}\n\tVehicles: [\n${vehiclesStr}]`;
  }
}
