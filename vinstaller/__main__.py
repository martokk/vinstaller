import typer
from loguru import logger
from rich.console import Console

from vinstaller import version
from vinstaller.main import Main

# Configure Loguru Logger
logger.add("log.log", level="DEBUG", rotation="50 MB")

# Configure Rich Console
console = Console()

# Configure Typer
app = typer.Typer(
    name="vinstaller",
    help="A vLifeLong Project created by Martokk.",
    add_completion=True,
)


# Print Current Version
def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]vinstaller[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


# Typer Commands
@app.command()
def main(
    profile: str = typer.Option(..., help="Profile to load."),
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the vinstaller package.",
    ),
    simulate: bool = typer.Option(
        False,
        "-s",
        "--simulate",
        help="Simulate installs.",
    ),
) -> None:
    # Start Installer
    logger.info("--------------------------------------------------------")
    logger.info(f"vInstaller Started... {profile=} {simulate=}")

    Main(profile_name=profile, simulate=simulate).run()
    print("\n")
    console.print("[green bold underline]vInstaller Complete![/]")


if __name__ == "__main__":
    app()
