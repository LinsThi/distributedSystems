import { Transport } from "../Transport/index.js";

export class Car extends Transport {
  constructor(model, capacity, fuelEfficiency, trunkSpace) {
    super(model, capacity, fuelEfficiency);
    this.trunkSpace = trunkSpace;
  }

  toString() {
    return super.toString() + `\nTrunk Space: ${this.trunkSpace}`;
  }
}
