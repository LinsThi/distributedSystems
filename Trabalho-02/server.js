import { fastify } from "fastify";
import vehicles from "./routes/vehicles.routes.js";
import company from "./routes/company.routes.js";

const server = fastify();

server.register(company);
server.register(vehicles);

server.listen({
  port: 3333,
});
