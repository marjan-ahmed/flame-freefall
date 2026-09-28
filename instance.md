---
format: 2
name: flame-freefall
title: Flame in Freefall
description: A governed, citation-backed corpus of NASA microgravity combustion investigations (BASS-II, SAFFIRE, FLEX, ACME) and the fire-safety standards and research priorities that frame them.
toolchain:
  requires: ">=0.0.60"
  scaffolded: "0.0.60"
# `database.dsn_env` names the environment variable holding your Postgres DSN —
# never the DSN itself, which belongs in .env. It is filled in because naming a
# variable costs nothing and needs no database: `npm run dev` and `npm run build` do
# not read it, and the value only has to exist when you climb to the served
# rung. To climb: copy .env.example to .env and set KSOR_DB_URL, then
# `npm run provision` once (schema + grant), then `npm run refresh` to PUBLISH the
# record, then `npm run serve`. Serving does not publish — that is deliberate, and
# skipping refresh serves nothing.
# Local Sentence Transformers supplies normalized 384-dimensional vectors,
# zero-padded to the existing pgvector schema's 1536 dimensions; this preserves
# cosine similarity and avoids changing the deployed database schema.
# Start system/sentence-transformers before ingesting or serving the record.
# Leaving `retrieval:` out starts with the abstention gate off; calibrate it
# afterwards with `ksor calibrate --queries-file` to avoid LLM-synthesized probes.
database:
  dsn_env: KSOR_DB_URL
embedding:
  provider: sentence-transformers
  model: sentence-transformers/all-MiniLM-L6-v2
  dim: 1536
# Where agents reach this record's MCP surface, and the semver it publishes as.
# Both go into /.well-known/mcp/server.json, the document an agent reads to
# DISCOVER this record instead of being told the URL. Leave mcp_url out until
# the server is actually published: an invented URL is worse than none.
# mcp_url: https://records.example.com/mcp
# version: 0.1.0
---

This record is authoritative for NASA's microgravity combustion
investigations covered here — BASS-II, SAFFIRE (including the later Saffire
VI flight), FLEX, and ACME — plus the fire-safety certification standard
(NASA-STD-6001B) and the decadal-survey research priorities (Liao, Miller,
and the "Thriving in Space" survey) that frame why they matter. It does not
cover other PSI-catalogued investigations outside this set (e.g. DAFT, SLICE,
SPICE, CFI, SAME), and it does not cover anything about spacecraft fire
safety beyond what these specific sources state. Every numeric claim here
traces to a verbatim quote from its source document — a gap in a source is
recorded as an open question, never filled by inference or general
knowledge.

Write and govern the knowledge once; every surface here derives from it. When a
slide deck, a wiki page or a model's memory disagrees with this record, this
record wins.
