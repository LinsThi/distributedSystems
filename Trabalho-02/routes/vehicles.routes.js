import { Bus } from "../class/Bus/index.js";
import { Car } from "../class/Car/index.js";
import { Motorcycle } from "../class/Motorcycle/index.js";
import { Truck } from "../class/Truck/index.js";

import { readFile, writeFile } from "node:fs/promises";
import { getPathDB } from "../utils/path.js";

const vehicles = async (fastify, options) => {
  fastify.post("/vehicles", async (request, reply) => {
    const { model, capacity, fuelEfficiency } = request.body;
    const dbPath = getPathDB();

    try {
      const data = await readFile(dbPath, "utf-8");
      const jsonData = JSON.parse(data);
      const listVehicles = jsonData.vehicles || [];

      let vehicle;

      switch (model) {
        case "Bus":
          const { passengerCount } = request.body;
          vehicle = new Bus(model, capacity, fuelEfficiency, passengerCount);
          break;
        case "Car":
          const { trunkSpace } = request.body;
          vehicle = new Car(model, capacity, fuelEfficiency, trunkSpace);
          break;
        case "Motorcycle":
          const { hasSidecar } = request.body;
          vehicle = new Motorcycle(model, capacity, fuelEfficiency, hasSidecar);
          break;
        case "Truck":
          const { payloadCapacity } = request.body;
          vehicle = new Truck(model, capacity, fuelEfficiency, payloadCapacity);
          break;
        default:
          return reply
            .code(400)
            .send({ message: "Modelo de veículo inválido" });
      }

      listVehicles.push(vehicle);
      jsonData.vehicles = listVehicles;

      await writeFile(dbPath, JSON.stringify(jsonData, null, 2));

      return { message: "Veículo cadastrado com sucesso!", vehicle };
    } catch (err) {
      console.error(err);
      return reply.code(500).send({ message: "Erro ao cadastrar o veículo" });
    }
  });
};

export default vehicles;
