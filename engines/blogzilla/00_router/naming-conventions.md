# Naming Conventions

Consistent naming makes it easy for the AI and humans to locate files and understand their purpose. Blogzilla uses kebab‑case (lowercase letters and hyphens) and version numbers to indicate drafts and revisions.

## Run Folders

Every execution of the engine has its own run folder. Use the pattern:

```
run‑YYYY‑MM‑DD‑[topic‑slug]/
```

* `YYYY‑MM‑DD` – date the run started (UTC or your local timezone).
* `topic‑slug` – a short, hyphenated version of the blog topic or keyword (remove spaces and punctuation).

Example: `run‑2026‑03‑13‑adaptive‑prompting/`

## File Names

Generated content files follow this pattern:

```
[topic]‑[asset]‑[platform]‑[status]‑v[number].md
```

* `topic` – same as the topic slug in the run folder.
* `asset` – a short identifier such as `summary`, `meta`, `highlights`, `thread`, `carousel`, `script`, `response`, `pin`, `article` or `digest`.
* `platform` – the platform or context (e.g. `core`, `x`, `linkedin`, `instagram`, `youtube`, `quora`, `facebook`, `pinterest`, `medium`, `substack`, `blogger`, `devto`). Use `core` for summaries and highlights.
* `status` – `draft`, `final`, or another lifecycle tag (e.g. `review`, `archive`).
* `v[number]` – version number starting at `v1` and incrementing on each revision.

Examples:

- `adaptive‑prompting‑summary‑core‑draft‑v1.md` – initial summary for the topic “Adaptive Prompting.”
- `adaptive‑prompting‑thread‑x‑final‑v2.md` – second revision of the X thread, final version.
- `adaptive‑prompting‑carousel‑instagram‑final‑v1.md` – completed Instagram carousel.
- `adaptive‑prompting‑expansion‑topics‑v1.md` – expansion suggestions file.

## Tracker Files

Tracker files collect data across runs. Use descriptive names:

* `tracker‑[topic]‑master‑v[number].md` – master tracker for a topic.
* `tracker‑[topic]‑platform‑outputs‑v[number].md` – record of all platform outputs.
* `tracker‑[topic]‑feedback‑v[number].md` – feedback and analytics for the topic.

## Other Files

Use clear labels for miscellaneous files:

- `run‑brief‑[topic]‑v[number].md` – run brief created during source intake.
- `new‑topics.md`, `collaboration‑opps.md`, `backlink‑opps.md`, `lead‑magnet.md`, `automation‑improvement.md` – outputs from the amplification‑expansion context.

By adhering to these conventions you ensure that future processes can find files without manual intervention and that duplicate names are avoided.