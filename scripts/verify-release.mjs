/** Read-only public deployment checks; never publishes or mutates a service. */
import { readFileSync, writeFileSync } from "node:fs";
import { createHash } from "node:crypto";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL("../", import.meta.url));
const runsFile = readFileSync(resolve(root, "psi-data/derived/runs.json"));
const expected = createHash("sha256").update(runsFile).digest("hex");
const urls = [
  ["site", "https://marjan-ahmed.github.io/flame-freefall/"],
  ["decision_workflow", "https://marjan-ahmed.github.io/flame-freefall/decide/"],
  ["dataset", "https://marjan-ahmed.github.io/flame-freefall/psi/runs.json"],
  ["chat_health", "https://flame-freefall-site.vercel.app/health"],
  ["corpus_health", "https://flamefreefall-sor.vercel.app/health"],
  ["corpus_ready", "https://flamefreefall-sor.vercel.app/ready"],
];
const checks = await Promise.all(urls.map(async ([name, url]) => {
  try {
    const response = await fetch(url, { signal: AbortSignal.timeout(15000) });
    const result = { name, url, status: response.status, reachable: response.ok };
    if (name === "dataset" && response.ok) {
      const payload = await response.json();
      result.dataset_sha256 = payload.sha256;
      result.records = payload.runs?.length;
      result.matches_local_dataset = payload.sha256 === expected;
    }
    return result;
  } catch (error) {
    return { name, url, reachable: false, error: error.name, code: error.cause?.code ?? null };
  }
}));
const passed = checks.every(c => c.reachable && c.matches_local_dataset !== false);
const report = { checked_at: new Date().toISOString(), read_only: true, passed, expected_dataset_sha256: expected, checks,
  limitations: "HTTP health is not retrieval correctness, answer validation or evidence that local code was deployed. A mismatching dataset or missing route requires publication and a fresh check; this command never publishes." };
const output = resolve(root, "research/release-verification.json");
writeFileSync(output, JSON.stringify(report, null, 2) + "\n");
console.log(JSON.stringify(report, null, 2));
process.exitCode = passed ? 0 : 1;
