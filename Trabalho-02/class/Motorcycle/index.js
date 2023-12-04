import { Transport } from "../Transport/index.js";

export class Motorcycle extends Transport {
  constructor(model, capacity, fuelEfficiency, hasSidecar) {
    super(model, capacity, fuelEfficiency);
    this.hasSidecar = hasSidecar;
  }

  toString() {
    const sidecarStr = this.hasSidecar ? "Yes" : "No";
    return super.toString() + `\nHas Sidecar: ${sidecarStr}`;
  }
}
