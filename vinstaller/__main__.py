from typing import Optional

from enum import Enum
from random import choice

import typer
from loguru import logger
from rich.console import Console

from vinstaller import version
from vinstaller.example import ExampleClass

# Configure Loguru Logger
logger.add("logs/log_{time}.log", level="TRACE", rotation="20 MB")


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


app = typer.Typer(
    name="vinstaller",
    help="A vLifeLong Project created by Martokk.",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(
            f"[yellow]vinstaller[/] version: [bold blue]{version}[/]"
        )
        raise typer.Exit()


@app.command(name="")
def main(
    name: str = typer.Option(..., help="Person to greet."),
    color: Color
    | None = typer.Option(
        None,
        "-c",
        "--color",
        "--colour",
        case_sensitive=False,
        help="Color for print. If not specified then choice will be random.",
    ),
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the vinstaller package.",
    ),
) -> None:

    example = ExampleClass()

    # Example Entry Point
    color = choice(list(Color)) if color is None else color
    greeting: str = example.print_name(name=name)
    logger.info(f"Simple Logging! {name=}")
    console.print(f"[bold {color}]{greeting}[/]")
    logger.success(f"Printed Name! {name=}")

    # Example #DIV/0 Logging Error (caught by @logger.catch decorator)
    example.example_divide_by_zero()


if __name__ == "__main__":
    app()
