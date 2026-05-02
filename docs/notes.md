# RideForge — Learning Journal

A running log of decisions, discoveries, and dead ends while building this project.

---

## 2026-05-02 — Project Setup

- Initialized project with `uv` and `pyproject.toml` (hatchling build backend).
- Chose Ollama + `qwen2.5:3b` as the local LLM — fast, runs offline, good for structured output.
- Used `pydantic-settings` for config so env vars map cleanly to typed fields.
- Dependency split: core deps in `[project.dependencies]`, test tools in `[project.optional-dependencies.dev]`.
- `uv sync --all-extras` installs everything into `.venv` in one shot.

### Stack decisions

| Concern | Choice | Why |
|---|---|---|
| LLM runtime | Ollama | Local, no API cost, easy model swaps |
| LLM model | qwen3.5:2b | Small enough to run on CPU, decent reasoning |
| Orchestration | LangGraph | Stateful multi-agent graphs, built-in checkpointing |
| Tool protocol | MCP | Standard interface, reusable across agents |
| Vector store | FAISS | Lightweight, no server needed |
| API | FastAPI + SSE | Streaming responses for long trip planning |
| CLI | Typer | Minimal boilerplate, automatic `--help` |
| Observability | LangSmith | Trace chains and agent steps visually |

---

## Backlog / Open Questions

- [ ] How to handle vision inputs (road/gear photos) with qwen2.5:3b — does it support multimodal?
- [ ] Best chunking strategy for ride knowledge corpus (FAISS).
- [ ] LangGraph Store vs. external SQLite for rider profile persistence.
- [ ] MCP server transport: `stdio` for local dev, `sse` for deployed?
- [ ] Evaluate `qwen3.5:2b` if 3b reasoning quality is insufficient.

---

<!-- Add new entries at the top under a new ## YYYY-MM-DD heading -->
