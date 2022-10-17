import subprocess
from pathlib import Path

from rich import print
from rich.console import Console

from vinstaller.view import View

console = Console()


class Installer:
    def __init__(self, simulate=True) -> None:
        self.view = View()
        self.simulate = simulate

    def install_apt_ppas(self, apt_ppas: list[str]) -> bool:
        print(self.view.build_install_panel(title="Install Apt PPA Repos", list_items=apt_ppas))

        _continue = console.input(
            "[magenta bold]Press [yellow](y/Y)[/yellow] to continue installing these packages:[/] "
        )
        if _continue.lower() != "y":
            return False

        for ppa in apt_ppas:
            if self.simulate:
                print(f'subprocess.call(["sudo", "add-apt-repository", f"ppa:{ppa}"])')
            else:
                subprocess.call(["sudo", "add-apt-repository", f"ppa:{ppa}"])

        if self.simulate:
            print('subprocess.call(["sudo", "apt", "update"])')
            print('subprocess.call(["sudo", "apt", "upgrade"])')
        else:
            subprocess.call(["sudo", "apt", "update"])
            subprocess.call(["sudo", "apt", "upgrade"])
        return True

    def install_packages(self, package_manager: str, packages: list[str], simulate=True) -> bool:
        packages = sorted(packages)
        print(
            self.view.build_install_panel(
                title=f"Install {package_manager.title()} Packages",
                list_items=packages,
            )
        )

        _continue = console.input(
            "[magenta bold]Press [yellow](y/Y)[/yellow] to continue installing these packages:[/] "
        )
        if _continue.lower() != "y":
            return False

        _silent = console.input(
            "[magenta bold]Press [yellow](y/Y)[/yellow] to install [yellow]SILENTLY[/yellow] (no user input):[/] "
        )

        if package_manager == "apt":
            install_command = ["sudo", "apt", "install"]
        elif package_manager == "pip":
            install_command = ["sudo", "pip", "install"]
        elif package_manager == "snap":
            install_command = ["sudo", "snap", "install"]
        elif package_manager == "flatpak":
            install_command = ["sudo", "flatpak", "install"]
        else:
            raise ValueError(f"Unknown package_manager. {package_manager=}")

        for package in packages:
            install_command.extend(package.split(" "))
        if _silent.lower() == "y":
            install_command.append("-y")

        if simulate:
            print(f"subprocess.call({install_command})")
        else:
            subprocess.call(install_command)
        return True

    def install_scripts(self, scripts: list[str]) -> bool:
        print(self.view.build_install_panel(title="Running Install Scripts", list_items=scripts))

        _continue = console.input("[magenta bold]Press [yellow](y/Y)[/yellow] to run these scripts:[/] ")
        if _continue.lower() != "y":
            return False

        for install_script in scripts:
            script_path = Path("./fresh_install/install_scripts") / f"{install_script}.sh"
            install_command = ["bash", script_path]
            print(f"Running Install Script [blue]'{install_script}'[/]:")
            if self.simulate:
                print(f"subprocess.call({install_command})")
            else:
                subprocess.call(install_command)
        return True
