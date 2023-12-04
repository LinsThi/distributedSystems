import { readFile, writeFile } from "node:fs/promises";
import { RentalCompany } from "../class/RentalCompany/index.js";
import { getPathDB } from "../utils/path.js";

const company = async (fastify, options) => {
  fastify.get("/company", async (request, reply) => {
    const dbPath = getPathDB();

    const response = await readFile(dbPath, "utf-8", (err, data) => {
      try {
        return data;
      } catch (err) {
        console.error(err);
      }
    });

    reply.status(200).send(response);
  });

  fastify.post("/company", async (request, reply) => {
    const { name } = request.body;

    const dbPath = getPathDB();

    const currentData = await readFile(dbPath, "utf-8");
    const jsonData = JSON.parse(currentData);
    const company = jsonData.name || {};

    if (Object.keys(company).length > 0) {
      return reply
        .status(400)
        .send({ message: "Já existe uma empresa cadastrada" });
    }
    const newCompany = new RentalCompany(name);

    await writeFile(dbPath, JSON.stringify(newCompany, null, 2));

    return reply.status(201).send({
      message: "Empresa cadastrada com sucesso!",
      company: newCompany,
    });
  });

  fastify.put("/company", async (request, reply) => {
    const { name } = request.body;

    const dbPath = getPathDB();

    const currentData = await readFile(dbPath, "utf-8");
    const jsonData = JSON.parse(currentData);
    const company = jsonData.name || {};

    if (Object.keys(company).length === 0) {
      return reply
        .status(400)
        .send({ message: "Não existe uma empresa cadastrada" });
    }

    jsonData.name = name;

    await writeFile(dbPath, JSON.stringify(jsonData, null, 2));

    return reply.status(200).send({
      message: "Nome da empresa atualizada com sucesso!",
      company: jsonData,
    });
  });
};

export default company;
