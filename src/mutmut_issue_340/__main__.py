"""Provide the entrypoint for the application."""

from os import getenv

from rich.console import Console
from rich.panel import Panel


def _check_env_var(variable_name: str, expected_value: str | None = None) -> bool:
    """
    Check if an expected environment variables is set.

    Args:
        variable_name (str): The name of the environment variable.
        expected_value (str | None, optional): The expected value of the environment variable. Defaults to None.

    Returns:
        bool: when the environment variable exists and has the expected value.

    """

    variable_value: str | None = getenv(variable_name)

    if variable_value is None:
        return False

    if len(variable_value) == 0:
        return False

    return not (expected_value and variable_value != expected_value)


def main() -> int:
    """
    Provide the entrypoint for the application.

    Returns:
        int: the application exit code.

    """

    if not _check_env_var("REQUESTS_CA_BUNDLE"):
        stderr = Console(stderr=True)

        stderr.print(
            Panel(
                "The required environment variable REQUESTS_CA_BUNDLE is empty or not set.\n\nDue to the TLS inspection utilised this application cannot function without it.",
                border_style="red",
                title="Failed",
                title_align="left",
            ),
        )

        return 1

    return 0


if __name__ == "__main__":
    main()
