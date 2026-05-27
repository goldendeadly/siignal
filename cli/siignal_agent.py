#!/usr/bin/env python3
"""
Siignal CLI Agent — Multi-Engine Runner

This script acts as the automated "Operator" for the Siignal ecosystem.
It reads the routing table for a given engine, sequentially executes each context
by sending prompts to an LLM API, and saves the outputs to the appropriate
workspace directories.

Usage:
    python siignal_agent.py run --engine adzilla --input ./examples/adzilla/input/run-brief.md
    python siignal_agent.py run --engine signalbeast --input ./examples/signalbeast/input/run-brief.md

Requirements:
    pip install openai typer rich
"""

import os
import sys
import json
import shutil
from pathlib import Path
from datetime import date
from typing import Optional

try:
    import typer
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from openai import OpenAI
except ImportError:
    print("Missing dependencies. Install with:")
    print("  pip install openai typer rich")
    sys.exit(1)

# ─────────────────────────────────────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────────────────────────────────────

app = typer.Typer(
    name="siignal",
    help="Siignal CLI Agent — Run AI-powered marketing engines end-to-end.",
)
console = Console()

# Root of the monorepo (assumes cli/ is one level below root)
REPO_ROOT = Path(__file__).resolve().parent.parent
ENGINES_DIR = REPO_ROOT / "engines"

# Engine context execution orders (derived from each engine's routing-table.md)
ENGINE_CONTEXTS = {
    "adzilla": [
        "offer-intake",
        "market-analysis",
        "creative-generation",
        "ad-assembly",
        "targeting-plan",
        "performance-tracking",
        "optimisation-expansion",
    ],
    "signalbeast": [
        "context-decoder",
        "core-generation",
        "platform-explosion",
        "tracking-canon",
        "signal-expansion",
        "automation-suggestions",
        "recursion-engine",
    ],
    "neural_marketing_engine": [
        "input-intake",
        "strategy-modeling",
        "blog-generation",
        "signal-expansion",
        "conversion-assets",
        "optimization-recursion",
        "packaging-output",
    ],
    "blogzilla": [
        "source-intake",
        "context-analysis",
        "core-generation",
        "platform-generation",
        "amplification-expansion",
        "tracking-memory",
        "automation-deployment",
    ],
}


# ─────────────────────────────────────────────────────────────────────────────
# LLM Client
# ─────────────────────────────────────────────────────────────────────────────


def get_llm_client() -> OpenAI:
    """Initialize the OpenAI-compatible LLM client."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        console.print(
            "[red]Error:[/red] OPENAI_API_KEY environment variable is not set.\n"
            "Set it with: export OPENAI_API_KEY=your-api-key-here"
        )
        raise typer.Exit(code=1)

    # Use environment base URL if set, otherwise default to OpenAI
    base_url = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
    return OpenAI(api_key=api_key, base_url=base_url)


def call_llm(client: OpenAI, system_prompt: str, user_prompt: str, model: str = "gpt-4.1-mini") -> str:
    """Send a prompt to the LLM and return the response text."""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        max_tokens=4096,
    )
    return response.choices[0].message.content


# ─────────────────────────────────────────────────────────────────────────────
# Engine Logic
# ─────────────────────────────────────────────────────────────────────────────


def load_context_files(engine_path: Path, context_name: str) -> dict:
    """Load the context.md, workflow.md, and prompts.md for a given context."""
    context_dir = engine_path / "03_contexts" / context_name
    files = {}
    for fname in ["context.md", "workflow.md", "prompts.md"]:
        fpath = context_dir / fname
        if fpath.exists():
            files[fname] = fpath.read_text(encoding="utf-8")
        else:
            files[fname] = ""
    return files


def build_system_prompt(engine_name: str, engine_readme: str, master_sop: str) -> str:
    """Build the system prompt that gives the LLM its identity and rules."""
    engine_titles = {
        "adzilla": "AdZilla Advertising Engine",
        "signalbeast": "SignalBeast Recursive Content Deployment System",
        "neural_marketing_engine": "Neural Marketing Engine",
        "blogzilla": "Blogzilla Content Engine",
    }
    title = engine_titles.get(engine_name, engine_name.title())

    return f"""You are the Siignal {title} Agent — an autonomous marketing content generator.
You follow the {title} system architecture precisely. Your job is to produce structured
marketing outputs according to the system's Standard Operating Procedure.

SYSTEM OVERVIEW:
{engine_readme[:2000]}

MASTER SOP (abbreviated):
{master_sop[:2000]}

RULES:
- Produce outputs in clean Markdown format.
- Follow the context instructions exactly.
- Be specific, actionable, and data-driven.
- Maintain the resonance mode specified in the run brief throughout all outputs.
- Include a canonical brand line where appropriate.
- Do NOT invent information not present in the inputs; make reasonable inferences only.
- When generating platform-specific content, adapt tone, length, and CTA to each platform's norms.
- Tag all highlights with their type (Framework, Principle, Statistic, Provocation, Meta-Insight).
- Apply CTA tiering (Soft, Engagement, Conversion) appropriate to each platform.
"""


def build_user_prompt(
    context_files: dict,
    run_brief: str,
    previous_outputs: dict,
    context_name: str,
) -> str:
    """Build the user prompt for a specific context execution."""
    prompt_parts = []

    prompt_parts.append(f"## Current Context: {context_name}\n")
    prompt_parts.append(f"### Context Definition\n{context_files.get('context.md', 'N/A')}\n")
    prompt_parts.append(f"### Workflow Instructions\n{context_files.get('workflow.md', 'N/A')}\n")
    prompt_parts.append(f"### Prompts Reference\n{context_files.get('prompts.md', 'N/A')}\n")
    prompt_parts.append(f"## Run Brief (Input)\n{run_brief}\n")

    if previous_outputs:
        prompt_parts.append("## Previous Context Outputs\n")
        for ctx_name, output in previous_outputs.items():
            # Truncate long outputs to stay within token limits
            truncated = output[:3000] if len(output) > 3000 else output
            prompt_parts.append(f"### {ctx_name}\n{truncated}\n")

    prompt_parts.append(
        "\n## Your Task\n"
        "Execute the current context according to the workflow and prompts above. "
        "Produce all expected outputs as described in the context definition. "
        "Format your response as a complete Markdown document ready to be saved as a file."
    )

    return "\n".join(prompt_parts)


def run_engine(engine_name: str, input_path: Path, output_dir: Optional[Path], model: str):
    """Execute any supported engine end-to-end."""
    engine_path = ENGINES_DIR / engine_name
    contexts = ENGINE_CONTEXTS.get(engine_name)

    if not engine_path.exists():
        console.print(f"[red]Error:[/red] Engine not found at {engine_path}")
        raise typer.Exit(code=1)

    if contexts is None:
        console.print(f"[red]Error:[/red] Engine '{engine_name}' is not yet supported by the CLI.")
        console.print(f"Supported engines: {', '.join(ENGINE_CONTEXTS.keys())}")
        raise typer.Exit(code=1)

    # Load run brief
    if not input_path.exists():
        console.print(f"[red]Error:[/red] Input file not found: {input_path}")
        raise typer.Exit(code=1)

    run_brief = input_path.read_text(encoding="utf-8")
    console.print(Panel(
        f"[bold green]{engine_name.title()} Engine[/bold green]\n"
        f"Input: {input_path.name}\n"
        f"Contexts: {len(contexts)} phases\n"
        f"Model: {model}",
        title="Siignal Agent"
    ))

    # Set up output directory
    if output_dir is None:
        slug = input_path.stem.replace(" ", "-").lower()
        output_dir = REPO_ROOT / "runs" / f"run-{date.today().isoformat()}-{engine_name}-{slug}"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load engine docs for system prompt
    engine_readme = (engine_path / "README.md").read_text(encoding="utf-8")
    master_sop = (engine_path / "MASTER_SOP.md").read_text(encoding="utf-8")
    system_prompt = build_system_prompt(engine_name, engine_readme, master_sop)

    # Initialize LLM client
    client = get_llm_client()

    # Execute each context sequentially
    previous_outputs = {}

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        for i, context_name in enumerate(contexts, 1):
            task = progress.add_task(
                f"[cyan]({i}/{len(contexts)}) Running: {context_name}...", total=None
            )

            # Load context files
            context_files = load_context_files(engine_path, context_name)

            # Build prompt
            user_prompt = build_user_prompt(
                context_files, run_brief, previous_outputs, context_name
            )

            # Call LLM
            try:
                result = call_llm(client, system_prompt, user_prompt, model=model)
            except Exception as e:
                console.print(f"[red]Error calling LLM for {context_name}:[/red] {e}")
                raise typer.Exit(code=1)

            # Save output
            output_file = output_dir / f"{i:02d}_{context_name}.md"
            output_file.write_text(result, encoding="utf-8")

            # Store for next context
            previous_outputs[context_name] = result

            progress.update(task, description=f"[green]({i}/{len(contexts)}) Done: {context_name}")
            progress.stop_task(task)

    # Save a run manifest
    manifest = {
        "engine": engine_name,
        "date": date.today().isoformat(),
        "input": str(input_path),
        "model": model,
        "contexts_executed": contexts,
        "outputs": [f"{i:02d}_{ctx}.md" for i, ctx in enumerate(contexts, 1)],
    }
    (output_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    console.print(
        Panel(
            f"[bold green]Run Complete![/bold green]\n\n"
            f"Engine: {engine_name}\n"
            f"Outputs saved to: {output_dir}\n"
            f"Files generated: {len(contexts)}\n"
            f"Manifest: {output_dir / 'manifest.json'}",
            title="Siignal Agent — Results",
        )
    )


# ─────────────────────────────────────────────────────────────────────────────
# CLI Commands
# ─────────────────────────────────────────────────────────────────────────────


@app.command()
def run(
    engine: str = typer.Option("adzilla", help="Engine to run (adzilla, signalbeast, neural_marketing_engine, blogzilla)"),
    input: Path = typer.Option(..., "--input", "-i", help="Path to the run brief input file"),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Output directory (auto-generated if not set)"),
    model: str = typer.Option("gpt-4.1-mini", "--model", "-m", help="LLM model to use"),
):
    """Run a Siignal engine end-to-end on a given input."""
    run_engine(engine, input, output, model)


@app.command()
def list_engines():
    """List all available Siignal engines."""
    console.print("\n[bold]Available Siignal Engines:[/bold]\n")
    engines = [d.name for d in ENGINES_DIR.iterdir() if d.is_dir()]
    for eng in sorted(engines):
        readme = ENGINES_DIR / eng / "README.md"
        desc = ""
        if readme.exists():
            # Extract first heading line as description
            for line in readme.read_text().splitlines():
                if line.startswith("# "):
                    desc = line.lstrip("# ").strip()
                    break
        if eng in ENGINE_CONTEXTS:
            status = f"[green]CLI Ready ({len(ENGINE_CONTEXTS[eng])} contexts)[/green]"
        else:
            status = "[dim]Framework Only[/dim]"
        console.print(f"  {eng:<30} {desc:<40} {status}")
    console.print()


@app.command()
def info(
    engine: str = typer.Argument(..., help="Engine name to inspect"),
):
    """Show details about a specific engine."""
    engine_path = ENGINES_DIR / engine
    if not engine_path.exists():
        console.print(f"[red]Engine '{engine}' not found.[/red]")
        raise typer.Exit(code=1)

    readme = engine_path / "README.md"
    if readme.exists():
        console.print(Panel(readme.read_text(encoding="utf-8")[:3000], title=f"Engine: {engine}"))

    contexts_dir = engine_path / "03_contexts"
    if contexts_dir.exists():
        contexts = sorted([d.name for d in contexts_dir.iterdir() if d.is_dir()])
        console.print(f"\n[bold]Contexts ({len(contexts)}):[/bold]")
        for ctx in contexts:
            console.print(f"  - {ctx}")

    if engine in ENGINE_CONTEXTS:
        console.print(f"\n[bold]Execution Order:[/bold]")
        for i, ctx in enumerate(ENGINE_CONTEXTS[engine], 1):
            console.print(f"  {i}. {ctx}")


# ─────────────────────────────────────────────────────────────────────────────
# Entry Point
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app()
