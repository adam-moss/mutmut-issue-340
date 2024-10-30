"""Tests for the __main__ module."""

from collections.abc import Generator
from typing import Any
from unittest.mock import Mock
from unittest.mock import patch

import pytest

from mutmut_issue_340.__main__ import main


@pytest.fixture
def mock_getenv() -> Generator[Mock, Any, None]:
    """Fixture to mock the os.getenv function."""
    with patch("mutmut_issue_340.__main__.getenv") as getenv_mock:
        yield getenv_mock


@pytest.fixture
def mock_console() -> Generator[Mock, Any, None]:
    """Fixture to mock the rich.Console class."""
    with patch("mutmut_issue_340.__main__.Console") as console_mock:
        yield console_mock.return_value


# Start testing main function
def test_main_with_unset_variable(
    mock_getenv: Mock,
    mock_console: Mock,
) -> None:
    """Test main function when the environment variable is not set."""
    mock_getenv.return_value = None

    assert main() == 1

    mock_getenv.assert_called_once()
    mock_console.print.assert_called_once()


def test_main_with_set_variable(
    mock_getenv: Mock,
    mock_console: Mock,
) -> None:
    """Test main function when the environment variable is set."""
    mock_getenv.return_value = "some_value"

    assert main() == 0

    mock_getenv.assert_called_once()
    mock_console.print.assert_not_called()


if __name__ == "__main__":
    pytest.main()
