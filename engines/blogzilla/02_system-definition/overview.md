# System Overview

The Blogzilla content engine is organised into layers—router, context areas and workspaces—to create a repeatable yet flexible system for transforming a single blog source into a full spectrum of derivative content. This overview summarises the system’s purpose, inputs, outputs, key stages and architectural principles.

## Purpose

Blogzilla turns a blog post, keyword or idea into a multi‑platform content package. It combines semantic analysis, modular content generation, platform‑specific adaptation, SEO reinforcement, CTA layering, tracking and recursion to compound the reach and longevity of the original source.

## Inputs

- Source blog post, URL or idea
- Resonance mode (Authority, Emotional, Technical, Viral or Educational)
- Core intent (e.g. SEO dominance, lead generation, thought leadership, audience growth)
- Niche or domain
- Optional recursion flag

## Outputs

- Summary and meta description
- Modular highlights tagged by type (framework, principle, statistic, provocation, meta‑insight)
- Platform‑specific outputs (threads, posts, carousels, scripts, articles, pins, digests)
- SEO/canonical statements and hashtag sets
- Tracker tables documenting the run
- Expansion suggestions (new topics, collaborations, backlinks, lead magnets, automation improvements)

## Key Stages

1. **Source Intake** – capture the blog source, set resonance mode and core intent, create the run brief and run folder.
2. **Context Analysis** – decode the tone, audience intent, conversion goal, primary and secondary keywords, long‑tail variants and related questions; produce a canonical statement.
3. **Core Generation** – write a summary, meta description and 5–10 highlights; tag each highlight as framework, principle, statistic, provocation or meta‑insight.
4. **Platform Generation** – adapt the core assets into channel‑specific formats for X/Twitter, LinkedIn, Instagram, YouTube, Quora, Facebook, Pinterest, Medium, Substack, Blogger and Dev.to; include appropriate CTAs and hashtags.
5. **Amplification & Expansion** – identify new blog topics, collaborations, backlinks, lead magnet ideas and automation improvements.
6. **Tracking & Memory** – log outputs and performance metrics into trackers, record lessons learned and resonance scores, and plan next iterations.
7. **Automation & Deployment** – prepare publishing cadence, schedule posts, produce design guidance and set up automation flows.

## Architectural Principles

- **Layer separation** – separate router definitions, context files and workspaces so the AI reads only what is relevant to each task.
- **Context‑derived names** – derive context names from the workflow; avoid arbitrary or generic labels.
- **Predictable naming** – follow strict file and folder naming conventions so files are discoverable by scripts and prompts.
- **Source preservation** – never modify the original source material; generated content lives in separate workspaces.
- **Iterative workflow** – treat each run as a cycle that feeds into future runs via trackers and expansion suggestions; do not attempt to produce every possible file at once.

This overview sets the stage for the detailed workflow map in `workflow-map.md` and the operating procedures in `MASTER_SOP.md`.