"""Tests for hello function."""
# from pathlib import Path

# import pytest

# from vinstaller.main import Profile, ProfileLoader

# PROFILES_PATH = Path("../vinstaller/profiles")


# @pytest.mark.parametrize(
#     ("profile_name", "expected"),
#     [
#         ("default", type(Profile)),
#     ],
# )
# def test_load_profile(profile_name: str, expected: type):
#     assert type(ProfileLoader().get_profile(profile_name=profile_name, profiles_path=PROFILES_PATH)) is Profile


# @pytest.mark.parametrize(
#     ("profile_name", "expected"),
#     [
#         ("missing_profile", type(Profile)),
#     ],
# )
# def test_load_missing_profile(profile_name: str, expected: type):
#     with pytest.raises(SystemExit):
#         ProfileLoader().get_profile(profile_name=profile_name, profiles_path=PROFILES_PATH)
