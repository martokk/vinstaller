import os
from pathlib import Path

from rich import print
from rich.console import Console
from vinstaller.installer import Installer

from vinstaller.profile import Profile
from vinstaller.profile_loader import ProfileLoader
from vinstaller.view import View

console = Console()
# logger.add("log.log", level="TRACE", rotation="50 MB")

PROFILES_PATH = Path.home() / ".vapps/vinstaller/profiles"
INSTALL_SCRIPTS_PATH = Path.home() / ".vapps/vinstaller/install_scripts"


class Main:
    def __init__(self, profile_name: str) -> None:
        self.profile: Profile = ProfileLoader().get_profile(profile_name=profile_name, profiles_path=PROFILES_PATH)
        self.view = View()
        self.installer = Installer(simulate=True)
        self.install_symlinks()
        self.run()

    def install_symlinks(self):
        source_path = Path("vinstaller")
        destination_path = Path.home() / ".vapps/vinstaller"

        if not Path(destination_path / "profiles").exists():
            os.symlink(Path(source_path / "profiles").absolute(), Path(destination_path / "profiles"))

        if not Path(destination_path / "install_scripts").exists():
            os.symlink(Path(source_path / "install_scripts").absolute(), Path(destination_path / "install_scripts"))

    def run(self) -> None:
        self.view.display_start_header(profile_name=self.profile.name)
        self.run_install_order(install_order=self.profile.install_order)

    def run_install_order(self, install_order: list[str]) -> None:
        for install_type in install_order:
            match install_type:
                case "pre_install_notes":
                    self.run_pre_install_notes()
                case "first_install_scripts":
                    self.run_first_install_scripts()
                case "apt_ppas":
                    self.run_apt_ppas()
                case "apt_packages":
                    self.run_apt_packages()
                case "pip_packages":
                    self.run_pip_packages()
                case "install_scripts":
                    self.run_install_scripts()
                case "snap_packages":
                    self.run_snap_packages()
                case "flatpak_packages":
                    self.run_flatpak_packages()
                case "post_install_notes":
                    self.run_post_install_notes()
                case _:
                    raise ValueError("'{install_type}' is not a valid install type.")

    def run_pre_install_notes(self) -> None:
        if not self.profile.pre_install_notes:
            return
        print(self.view.build_panel(title="Pre Install Notes", list_items=self.profile.pre_install_notes))
        _ = console.input("[magenta bold]Press Enter key to continue[/]")

    def run_first_install_scripts(self) -> None:
        install_status = self.installer.install_scripts(scripts=self.profile.first_install_scripts)
        self.view.display_install(install_status=install_status, success_text="First Install Scripts installed!")

    def run_install_scripts(self) -> None:
        install_status = self.installer.install_scripts(scripts=self.profile.install_scripts)
        self.view.display_install(install_status=install_status, success_text="First Install Scripts installed!")

    def run_apt_ppas(self) -> None:
        install_status = self.installer.install_apt_ppas(apt_ppas=self.profile.apt_ppas)
        self.view.display_install(install_status=install_status, success_text="Apt PPA Repos installed!")

    def run_apt_packages(self) -> None:
        install_status = self.installer.install_packages(package_manager="apt", packages=self.profile.apt_packages)
        self.view.display_install(install_status=install_status, success_text="Apt Packages installed!")

    def run_pip_packages(self) -> None:
        install_status = self.installer.install_packages(package_manager="pip", packages=self.profile.pip_packages)
        self.view.display_install(install_status=install_status, success_text="PIP Packages installed!")

    def run_snap_packages(self) -> None:
        install_status = self.installer.install_packages(package_manager="snap", packages=self.profile.snap_packages)
        self.view.display_install(install_status=install_status, success_text="Snap Packages installed!")

    def run_flatpak_packages(self) -> None:
        install_status = self.installer.install_packages(
            package_manager="flatpak", packages=self.profile.flatpak_packages
        )
        self.view.display_install(install_status=install_status, success_text="Flatpak Packages installed!")

    def run_post_install_notes(self):
        if not self.profile.post_install_notes:
            return
        print(self.view.build_panel(title="Post Install Notes", list_items=self.profile.post_install_notes))
        _ = console.input("[magenta bold]Press Enter key to continue[/]")