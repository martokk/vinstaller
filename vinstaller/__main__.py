import typer
from loguru import logger
from rich.console import Console
from vinstaller import version

# from vinstaller.old_main import FreshInstall

# Configure Loguru Logger
logger.add("log.log", level="TRACE", rotation="50 MB")

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
) -> None:

    # Entry Point
    logger.info(f"Entry Point! {profile=}")
    # FreshInstall(profile_name=_args.profile).run()


if __name__ == "__main__":
    app()
