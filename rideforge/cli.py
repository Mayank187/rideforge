import typer
from rideforge import __version__

app = typer.Typer(name="rideforge", help="AI-powered motorcycle trip planner.")


@app.command()
def hello(name: str = typer.Option("rider", help="Your name.")):
    """Print a welcome message and confirm RideForge is running."""
    typer.echo(f"Hey {name}, welcome to RideForge v{__version__}!")
    typer.echo("Your AI-powered motorcycle trip planner is ready.")


@app.command()
def version():
    """Show the current RideForge version."""
    typer.echo(f"RideForge v{__version__}")


if __name__ == "__main__":
    app()
