import { spawnSync } from "node:child_process";
import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const projectRoot = resolve(fileURLToPath(new URL("..", import.meta.url)));
const allowedCommands = new Set(["schema", "grant", "ingest", "gc", "serve"]);
const [command, ...args] = process.argv.slice(2);
const databaseName = "flame_freefall_sentence_transformers";

if (!allowedCommands.has(command)) {
  console.error(`Usage: node scripts/ksor-local.mjs <${[...allowedCommands].join("|")}> [args...]`);
  process.exit(2);
}

function configuredValue(name) {
  if (process.env[name]) return process.env[name];
  const envFile = readFileSync(resolve(projectRoot, ".env"), "utf8");
  for (const line of envFile.split(/\r?\n/)) {
    const entry = line.trim().replace(/^export\s+/, "");
    const prefix = `${name}=`;
    if (!entry.startsWith(prefix)) continue;
    return entry.slice(prefix.length).trim().replace(/^(["'])(.*)\1$/, "$2");
  }
}

let databaseUrl;
try {
  const rawDatabaseUrl = configuredValue("KSOR_DB_URL");
  if (!rawDatabaseUrl) throw new Error("KSOR_DB_URL is not configured in the environment or root .env");
  const parsed = new URL(rawDatabaseUrl);
  if (!["postgres:", "postgresql:"].includes(parsed.protocol)) throw new Error("KSOR_DB_URL must be a PostgreSQL URL");
  parsed.pathname = `/${databaseName}`;
  databaseUrl = parsed.toString();
} catch (error) {
  console.error(`Cannot select the local Sentence Transformers database: ${error.message}`);
  process.exit(1);
}

const env = {
  ...process.env,
  KSOR_DB_URL: databaseUrl,
  SENTENCE_TRANSFORMERS_BASE_URL:
    process.env.SENTENCE_TRANSFORMERS_BASE_URL ??
    configuredValue("SENTENCE_TRANSFORMERS_BASE_URL") ??
    "http://127.0.0.1:8001/v1",
};
const cli = resolve(projectRoot, "node_modules", "@panaversity", "ksor", "dist", "cli.mjs");
console.log(`KSOR local target database: ${databaseName}; embedding endpoint: ${env.SENTENCE_TRANSFORMERS_BASE_URL}`);

const result = spawnSync(process.execPath, [cli, command, ...args], {
  cwd: projectRoot,
  env,
  stdio: "inherit",
});

if (result.error) {
  console.error(`Could not start ksor: ${result.error.message}`);
  process.exit(1);
}
process.exit(result.status ?? 1);
