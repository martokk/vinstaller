from pathlib import Path
import typer
from loguru import logger
from rich.console import Console

from vinstaller import version
from vinstaller.main import Main
from vinstaller.profile import Profile
from vinstaller.profile_loader import ProfileLoader


PROFILES_PATH = Path.home() / ".vapps/vinstaller/profiles"
INSTALL_SCRIPTS_PATH = Path.home() / ".vapps/vinstaller/install_scripts"


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

    _profile: Profile = ProfileLoader().get_profile(profile_name=profile, profiles_path=PROFILES_PATH)
    Main(profile=_profile, simulate=simulate).run()
    print("\n")
    console.print("[green bold underline]vInstaller Complete![/]")


if __name__ == "__main__":
    app()
