import typer
from rich.console import Console
from rich.panel import Panel

from software_factory.core.orchestrator import DAGOrchestrator

app = typer.Typer(
    name="software-factory",
    help="Ultimate AI Builder Platform - Meta-Orchestrator for Antigravity",
    add_completion=False,
)
console = Console()

@app.command()
def scaffold_app(
    prompt: str = typer.Argument(..., help="What application do you want to build?"),
    output_dir: str = typer.Option("./output", "--output", "-o", help="Where to generate the artifacts"),
):
    """
    Generate an application architecture and blueprint based on a prompt.
    """
    console.print(Panel.fit(
        f"[bold blue]Starting Software Factory Orchestrator[/bold blue]\n[white]Goal:[/] {prompt}",
        title="Software Factory",
        border_style="green"
    ))
    
    orchestrator = DAGOrchestrator(output_dir=output_dir)
    orchestrator.run(goal=prompt)

@app.command()
def version():
    """Print the current version."""
    console.print("Software Factory v0.1.0")

if __name__ == "__main__":
    app()
