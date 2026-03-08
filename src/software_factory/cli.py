import typer
import os
import urllib.request
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
def init():
    """
    Initialize the Software Factory Antigravity workflow locally.
    Creates the .agents/workflows directory and downloads the SF-software-factory.md file.
    """
    workflow_dir = os.path.join(os.getcwd(), ".agents", "workflows")
    os.makedirs(workflow_dir, exist_ok=True)
    
    workflow_path = os.path.join(workflow_dir, "SF-software-factory.md")
    url = "https://raw.githubusercontent.com/eybersjp/software-factory/master/SF-software-factory.md"
    
    console.print(f"[cyan]Initializing Software Factory in {workflow_dir}...[/]")
    try:
        urllib.request.urlretrieve(url, workflow_path)
        console.print(Panel("[bold green]Successfully installed the Antigravity Workflow![/]\n\nYou can now type `/SF-software-factory` in this workspace.", border_style="green"))
    except Exception as e:
        console.print(f"[bold red]Failed to download workflow:[/] {e}")

@app.command()
def version():
    """Print the current version."""
    console.print("Software Factory v0.1.0")

if __name__ == "__main__":
    app()
