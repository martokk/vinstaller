"""Tests for hello function."""
# from pathlib import Path

from pathlib import Path
import pytest
from vinstaller.profile import Profile
from unittest.mock import Mock
from vinstaller.main import Main
from vinstaller.profile_loader import ProfileLoader
from vinstaller.view import View


@pytest.fixture
def profile() -> Profile:
    return Profile(
        name="default",
        profile_name="Default",
        profile_path=Path(""),
        dotfiles_repo="",
        dotfiles_profile="test",
        install_order=["first_install_scripts"],
        first_install_scripts=["pyenv"],
        apt_ppas=[],
        apt_packages=["git"],
        pip_packages=[],
        install_scripts=[],
        snap_packages=[],
        flatpak_packages=["brave"],
        pre_install_notes=["test pre_install_notes"],
        post_install_notes=["test post_install_notes"],
    )


@pytest.fixture
def main(profile: Profile) -> Main:
    return Main(profile=profile, simulate=True)


def test_init_main(main: Main) -> None:
    assert main.profile.profile_name == "Default"
    assert type(main.view) is type(View())
    assert main.installer.simulate == True


def test_invalid_install_order_item(main: Main) -> None:
    run_install_order = ["wrong_item"]
    with pytest.raises(ValueError):
        main.run_install_order(install_order=run_install_order)
