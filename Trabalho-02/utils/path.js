import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

export function getPathDB() {
  const __filename = fileURLToPath(import.meta.url);
  const __dirname = dirname(__filename);

  const filePath = join(__dirname, "..", "database", "database-memory.json");
  return filePath;
}
