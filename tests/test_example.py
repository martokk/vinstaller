"""Tests for hello function."""
import pytest

from vinstaller.example import ExampleClass


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("Jeanette", "Hello Jeanette from click! See __main__.py"),
        ("Raven", "Hello Raven from click! See __main__.py"),
        ("Maxine", "Hello Maxine from click! See __main__.py"),
        ("Matteo", "Hello Matteo from click! See __main__.py"),
        ("Destinee", "Hello Destinee from click! See __main__.py"),
        ("Alden", "Hello Alden from click! See __main__.py"),
        ("Mariah", "Hello Mariah from click! See __main__.py"),
        ("Anika", "Hello Anika from click! See __main__.py"),
        ("Isabella", "Hello Isabella from click! See __main__.py"),
    ],
)
def test_print_name(name, expected):
    """Example test with parametrization."""
    assert ExampleClass().print_name(name) == expected
