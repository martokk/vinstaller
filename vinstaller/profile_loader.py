from typing import Any

import os
from pathlib import Path

import yaml
from loguru import logger

from vinstaller.profile import Profile


class ProfileLoader:
    @staticmethod
    def _get_profile_paths(profiles_path: Path) -> list[Path]:
        """Gets list of Paths to available profiles in 'profiles' folder."""
        print(f"{profiles_path=} {os.listdir(profiles_path)=}")
        return [Path(profiles_path) / profile_path for profile_path in os.listdir(profiles_path)]

    def _get_profile_path(self, profile_name: str, profiles_path: Path) -> Path:
        """Gets profile path from a profile_name"""
        profile_paths = self._get_profile_paths(profiles_path=profiles_path)
        for profile_path in profile_paths:
            if profile_path.stem.lower() == profile_name.lower():
                return profile_path
        raise ValueError(f"Profile does not exist. {profile_name=}")

    @staticmethod
    def _load_yaml_file(yaml_file: Path) -> dict[str, Any]:
        """Load yaml_file as a dict"""
        with open(yaml_file) as file:
            return yaml.safe_load(file)

    def get_profile(self, profile_name: str, profiles_path: Path) -> Profile:
        """Load a profile by profile_name"""
        try:
            profile_path = self._get_profile_path(profile_name=profile_name, profiles_path=profiles_path)
        except ValueError as e:
            logger.critical(e)
            exit(1)

        profile_data = self._load_yaml_file(yaml_file=profile_path)
        profile = Profile(**profile_data, profile_name=profile_name, profile_path=profile_path)
        logger.success(f"Profile loaded: '{profile.name}'; {profile.profile_path=}; {profile.profile_name=}")
        return profile
