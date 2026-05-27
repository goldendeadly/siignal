# Siignal

**Siignal** is a modular AI-powered marketing engine ecosystem. It transforms a single input (an offer, a blog post, a keyword) into a full-spectrum marketing campaign — from strategy and content generation to advertising, platform deployment, and recursive amplification.

Siignal operates as an autonomous agent: give it a run brief, and it executes a structured, multi-phase workflow using LLM intelligence to produce production-ready marketing assets.

---

## Architecture

Siignal is composed of four specialized engines, each handling a distinct phase of the marketing lifecycle:

| Engine | Purpose | Status |
|--------|---------|--------|
| **AdZilla** | Transforms an offer into multi-platform advertising campaigns | CLI Agent Ready (7 contexts) |
| **Blogzilla** | Generates and repurposes blog content across platforms | Framework |
| **SignalBeast** | Recursive content deployment — 100+ assets from one source | CLI Agent Ready (7 contexts) |
| **Neural Marketing Engine** | End-to-end strategy, content, and conversion asset generation | Framework |

All engines share a common layered architecture:

```
engine/
├── 00_router/          # System definition, routing table, naming conventions
├── 02_system-definition/ # Workflow maps and overviews
├── 03_contexts/        # Operational phases with prompts and workflows
├── 05_prompts/         # Environment-specific prompt collections
├── 06_templates/       # Standardized output templates
└── MASTER_SOP.md       # Step-by-step execution guide
```

---

## Quick Start

### Prerequisites

- Python 3.10+
- An OpenAI API key (or any OpenAI-compatible API)

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/siignal.git
cd siignal
pip install -r cli/requirements.txt
```

### Set Your API Key

```bash
export OPENAI_API_KEY="sk-your-api-key-here"
```

To use a different provider (Anthropic via proxy, local models, etc.), also set:

```bash
export OPENAI_BASE_URL="https://your-provider-url/v1"
```

### Run AdZilla

```bash
python cli/siignal_agent.py run --engine adzilla --input examples/adzilla/input/run-brief.md
```

### Run SignalBeast

```bash
python cli/siignal_agent.py run --engine signalbeast --input examples/signalbeast/input/run-brief.md
```

Both engines execute all 7 contexts sequentially and save outputs to a timestamped `runs/` directory.

### Other Commands

```bash
# List all available engines
python cli/siignal_agent.py list-engines

# Inspect a specific engine
python cli/siignal_agent.py info adzilla

# Use a different model
python cli/siignal_agent.py run --engine adzilla --input ./my-brief.md --model gpt-4.1-mini

# Run SignalBeast with a custom model
python cli/siignal_agent.py run --engine signalbeast --input ./my-blog.md --model gpt-4.1-mini
```

---

## API Key Setup (Detailed)

The Siignal CLI agent requires access to an LLM API. It uses the OpenAI SDK format, which is compatible with multiple providers.

### Option 1: OpenAI (Recommended for simplicity)

1. Create an account at [platform.openai.com](https://platform.openai.com)
2. Navigate to API Keys and generate a new key
3. Set the environment variable:
   ```bash
   export OPENAI_API_KEY="sk-..."
   ```

### Option 2: Anthropic (via OpenAI-compatible proxy)

If you prefer Claude models, use a proxy service like LiteLLM or OpenRouter:

```bash
export OPENAI_API_KEY="your-openrouter-key"
export OPENAI_BASE_URL="https://openrouter.ai/api/v1"
```

Then specify the model:
```bash
python cli/siignal_agent.py run --engine adzilla --input ./brief.md --model anthropic/claude-sonnet-4
```

### Option 3: Local Models (Ollama, LM Studio)

For fully local execution with no API costs:

```bash
export OPENAI_API_KEY="not-needed"
export OPENAI_BASE_URL="http://localhost:11434/v1"  # Ollama default
```

```bash
python cli/siignal_agent.py run --engine adzilla --input ./brief.md --model llama3
```

### Persistent Configuration

Add to your shell profile (`~/.bashrc`, `~/.zshrc`):

```bash
export OPENAI_API_KEY="sk-your-key"
```

Or create a `.env` file in the project root (already in `.gitignore`):

```
OPENAI_API_KEY=sk-your-key
OPENAI_BASE_URL=https://api.openai.com/v1
```

---

## How It Works

When you run the CLI agent, it performs the following automated sequence:

1. **Reads the Run Brief** — Your input file containing offer details, audience, objectives, and constraints.
2. **Loads the Routing Table** — Determines the execution order of contexts from `00_router/routing-table.md`.
3. **Executes Each Context** — For every phase (e.g., offer-intake, market-analysis, creative-generation):
   - Reads the context definition, workflow, and prompts
   - Constructs a prompt incorporating all prior outputs as accumulated context
   - Sends the prompt to the LLM API
   - Saves the structured response as a Markdown file
4. **Produces a Manifest** — A JSON file documenting the run metadata, model used, and all outputs generated.

---

## Repository Structure

```
siignal/
├── README.md                          # This file
├── cli/
│   ├── siignal_agent.py               # The CLI agent (Python)
│   └── requirements.txt               # Python dependencies
├── engines/
│   ├── adzilla/                       # AdZilla Advertising Engine
│   ├── blogzilla/                     # Blogzilla Content Engine
│   ├── signalbeast/                   # SignalBeast Recursive Engine
│   └── neural_marketing_engine/       # Neural Marketing Engine
├── examples/
│   └── adzilla/
│       ├── input/run-brief.md         # Example input
│       └── output/                    # Example outputs
├── shared/                            # Shared templates and prompts
├── docs/                              # Additional documentation
├── .gitignore                         # Excludes runtime data
└── LICENSE
```

---

## Engine Pipeline (Recommended Flow)

For maximum output, chain the engines together:

```
[Neural Marketing Engine] → Strategy + Blog + Social Signals
         ↓
    [Blogzilla] → Repurposed content across platforms
         ↓
   [SignalBeast] → 100+ recursive content assets
         ↓
     [AdZilla] → Paid advertising campaigns for amplification
```

---

## Contributing

Siignal is designed to be extensible. To add a new engine:

1. Create a new directory under `engines/`
2. Follow the standard layer architecture (00_router, 02_system-definition, 03_contexts, etc.)
3. Add context folders with `context.md`, `workflow.md`, and `prompts.md`
4. Update the routing table
5. (Optional) Add CLI support in `siignal_agent.py`

---

## License

MIT License. See [LICENSE](./LICENSE) for details.
