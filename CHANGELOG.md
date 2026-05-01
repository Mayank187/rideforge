# Changelog

All notable changes to RideForge will be documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [Unreleased]

---

## [0.1.0] — 2026-05-02

### Added
- Project scaffold with `uv` and `pyproject.toml` (hatchling)
- `rideforge/config.py` — typed settings via `pydantic-settings`, loads from `.env`
- `rideforge/cli.py` — Typer CLI with `hello` and `version` commands
- `rideforge/__main__.py` — enables `python -m rideforge`
- `.env.example` — documented environment variable template
- `docs/notes.md` — learning journal with stack decisions
- Full directory structure for agents, chains, tools, middleware, MCP servers, and API
