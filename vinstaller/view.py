from rich import box, print
from rich.columns import Columns
from rich.console import Console, Group
from rich.panel import Panel
from rich.text import Text

from vinstaller import version

console = Console()


class View:
    @staticmethod
    def display_start_header(profile_name: str) -> None:
        print(f"[cyan bold underline]vInstaller v{version}[/]")
        print(f"\t- profile_name: {profile_name}\n")

    @staticmethod
    def display_step(step: int, text: str) -> None:
        print(f"\n[yellow bold underline]Step {step}[/][bold]: {text}[/]")

    @staticmethod
    def display_install(
        install_status: bool,
        success_text="Successfully Installed.",
        fail_text="Issue while installing.",
    ) -> None:
        if install_status:
            print(f"[bold green]{success_text}[/]\n")
        else:
            print(f"[bold red]{fail_text}[/]\n")

    @staticmethod
    def build_panel(list_items: list[str], title: str) -> Panel:
        list_items = [f"- {list_item}" for list_item in list_items]
        return Panel(
            renderable=Group(
                Columns(list_items, column_first=True, padding=(0, 5)),
            ),
            title=f"[yellow bold underline]{title}[/]",
            box=box.SQUARE,
            title_align="left",
            width=80,
            border_style="white",
            style="blue",
        )

    @staticmethod
    def build_install_panel(list_items: list[str], title: str) -> Panel:
        return Panel(
            renderable=Group(
                Text("The following will be installed:", style="default"),
                Columns(list_items, column_first=True, padding=(0, 5)),
            ),
            title=f"[yellow bold underline]{title}[/]",
            box=box.SQUARE,
            title_align="left",
            width=80,
            border_style="white",
            style="blue",
        )
