import { Transport } from "../Transport/index.js";

export class Bus extends Transport {
  constructor(model, capacity, fuelEfficiency, passengerCount) {
    super(model, capacity, fuelEfficiency);
    this.passengerCount = passengerCount;
  }

  toString() {
    return super.toString() + `\nPassenger Count: ${this.passengerCount}`;
  }
}
