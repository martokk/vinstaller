from dataclasses import dataclass
from pathlib import Path


@dataclass
class Profile:
    # Profile
    name: str
    profile_name: str
    profile_path: Path
    dotfiles_repo: str
    dotfiles_local: str
    dotfiles_profile: str

    # Install
    install_order: list[str]
    first_install_scripts: list[str]
    apt_ppas: list[str]
    apt_packages: list[str]
    pip_packages: list[str]
    install_scripts: list[str]
    snap_packages: list[str]
    flatpak_packages: list[str]
    pre_install_notes: list[str]
    post_install_notes: list[str]
