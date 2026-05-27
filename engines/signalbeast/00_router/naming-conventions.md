# Naming Conventions

Consistent naming allows SignalBeast to locate and process files automatically. Use kebab‑case and version numbers for all files and folders.

## Run Folders

Every execution has its own folder:

```
run‑YYYY‑MM‑DD‑[topic‑slug]/
```

* `YYYY‑MM‑DD` – date of the run.
* `topic‑slug` – concise, hyphenated identifier derived from the source topic.

Example: `run‑2026‑03‑13‑signal‑beast/`

## File Names

Generated assets use this pattern:

```
[topic]‑[asset]‑[platform]‑[status]‑v[number].md
```

* `topic` – matches the topic slug used in the run folder.
* `asset` – describes the content type: `summary`, `meta`, `highlights`, `thread`, `carousel`, `script`, `answer`, `pin`, `article`, `digest`, `email`, `prompt`, `rewrite`, `matrix`, etc.
* `platform` – indicates the destination or context (e.g. `core`, `x`, `linkedin`, `instagram`, `youtube`, `quora`, `facebook`, `pinterest`, `medium`, `substack`, `blogger`, `devto`, `email`, `prompt`, `rewrite`). Use `core` for summary and highlights.
* `status` – `draft`, `final`, `mutated`, `recursed` or other lifecycle tags.
* `v[number]` – version number starting at `v1`.

Examples:

- `signal‑beast‑summary‑core‑draft‑v1.md`
- `signal‑beast‑thread‑x‑final‑v2.md`
- `signal‑beast‑carousel‑instagram‑draft‑v1.md`
- `signal‑beast‑mutate‑x‑recursed‑v1.md`
- `signal‑beast‑supercluster‑matrix‑v1.md`

## Tracker & Matrix Files

* `tracker‑[topic]‑master‑v[number].md` – master tracker for the run.
* `matrix‑[topic]‑platform‑outputs‑v[number].md` – detailed publication matrix.
* `supercluster‑grid‑[topic]‑v[number].md` – SEO supercluster grid produced by the decoder.

Use clear names for expansion and recursion outputs (e.g. `new‑topics.md`, `collaboration‑opps.md`, `mutation‑log.md`).