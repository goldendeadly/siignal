# Changelog

All notable changes to the Siignal ecosystem will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] — 2026-05-28

### Added
- Eval harness with 41 test cases across all 5 engines (format, injection, edge-case)
- CI/CD pipeline via GitHub Actions (structural lint, eval dry-run, safety scan, syntax check)
- Live eval workflow (manual trigger with API key for full end-to-end testing)
- CHANGELOG.md and VERSION files for all engines
- Lightweight safety checks in CLI agent (input validation, secret scanning, injection detection)

### Changed
- CLI agent upgraded with pre-flight safety layer before LLM calls

## [0.1.0] — 2026-05-27

### Added
- Initial monorepo structure with 5 engines:
  - AdZilla (offer-to-ads transformation)
  - Blogzilla (content repurposing and amplification)
  - SignalBeast (recursive content deployment)
  - Neural Marketing Engine (end-to-end strategy and funnel generation)
  - Realtor Concierge (lead intake, qualification, and appointment booking)
- Python CLI agent (`cli/siignal_agent.py`) supporting all 5 engines
- Example inputs and outputs for each engine
- Root README with API key instructions and usage documentation
- MIT License

## [Unreleased]

### Planned
- Optimization Agent integration (`/tools/optimization-agent/`)
- Web dashboard for run history and analytics
- Multi-engine pipeline chaining (AdZilla → Realtor Concierge)
- Webhook triggers for automated runs
