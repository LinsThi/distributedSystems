import { Transport } from "../Transport/index.js";

export class Truck extends Transport {
  constructor(model, capacity, fuelEfficiency, payloadCapacity) {
    super(model, capacity, fuelEfficiency);
    this.payloadCapacity = payloadCapacity;
  }

  toString() {
    return super.toString() + `\nPayload Capacity: ${this.payloadCapacity}`;
  }
}
