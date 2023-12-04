export class Transport {
  constructor(model, capacity, fuelEfficiency) {
    this.model = model;
    this.capacity = capacity;
    this.fuelEfficiency = fuelEfficiency;
  }

  toString() {
    return `Model: ${this.model}\nCapacity: ${this.capacity}\nFuel Efficiency: ${this.fuelEfficiency}`;
  }
}
