from os import environ
from os import getenv
from typing import TYPE_CHECKING
from typing import Any

from hypothesis import Verbosity
from hypothesis import settings
from hypothesis.errors import InvalidArgument

from mutmut_issue_340.__about__ import __version__

if TYPE_CHECKING:
    import pytest

settings.register_profile("ci", max_examples=1000)
settings.register_profile("debug", max_examples=10, verbosity=Verbosity.verbose)

header_msgs: list[str] = [f"Using:\n- mutmut_issue_340: {__version__}\n"]
warning_msgs: list[str] = []

hypothesis_profile: str = "default"

if getenv("HYPOTHESIS_PROFILE"):
    try:
        hypothesis_profile = getenv("HYPOTHESIS_PROFILE", "default")

        settings.load_profile(getenv("HYPOTHESIS_PROFILE", ""))

    except InvalidArgument:
        warning_msgs += f"- requested hypothesis profile '{getenv('HYPOTHESIS_PROFILE')}' was not loaded, continuing with 'default'.\n"
elif getenv("CI"):
    hypothesis_profile = "ci"

    settings.load_profile("ci")

header_msgs += f"- hypothesis profile: {hypothesis_profile}\n"


def pytest_report_header(config: "pytest.Config") -> str | list[str]:  # noqa: ARG001
    if len(warning_msgs) > 0:
        return f'{"".join(header_msgs)}\nWARNING:\n{"".join(warning_msgs)}'

    return f'{"".join(header_msgs)}'


def pytest_sessionstart(session: "pytest.Session") -> None:  # noqa: ARG001
    """
    Call after the Session object has been created and before performing collection and entering the run test loop.

    Args:
        session (pytest.Session): The pytest session object.

    """
    ...


def pytest_sessionfinish(
    session: "pytest.Session",  # noqa: ARG001
    exitstatus: "int | pytest.ExitCode",  # noqa: ARG001
) -> None:
    """
    Call after whole test run finished, right before returning the exit status to the system.

    Args:
        session (pytest.Session): The pytest session object.
        exitstatus (int | pytest.ExitCode): The status which pytest will return to the system.

    """
    ...
