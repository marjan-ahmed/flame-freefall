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
# Sentence Transformers supplies normalized 384-dimensional vectors, zero-padded
# to a 1536-dimensional schema. This is a different space from Gemini: use a new
# database, then provision and ingest it before serving. Ingest and query must use
# the same model and dimensions.
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

This record is authoritative only for the sources represented in its governed
NASA combustion documents: solid-fuel investigations (BASS, BASS-II, SAFFIRE),
droplet investigations (FLEX, FLEX-2, CFI), gaseous-flame investigations including
ACME and SPICE, and smoke/aerosol investigations SAME and SAME-R. Data-source
inventories describe additional PSI tables; an inventory is not a scientific
review of every investigation it lists. Foundations cover NASA-STD-6001B and
the cited decadal-survey research priorities.

The record is not a fire-risk predictor, materials qualification authority or
validation of combustion at lunar or Martian gravity. Missing data describes
this collection, not proof of safety or absence of research. BRE uses gaseous
burners to emulate condensed fuels; relevant indirect evidence must not be
presented as direct solid-material testing. Search tolerances are numerical
heuristics, not validated physical equivalence or safety margins.

Every claim must be supported by the retrieved source passage. A gap or conflict
in a source remains an open question, never filled from model memory. Source
approval metadata is a recorded attestation, not independent proof of review.
