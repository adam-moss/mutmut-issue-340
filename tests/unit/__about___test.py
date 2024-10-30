from typing import Any
from typing import get_args
from typing import get_origin

import pytest
from typing_extensions import ParamSpec

from mutmut_issue_340 import __about__


@pytest.mark.parametrize(
    ("attribute_name", "datatype"),
    [
        ("__package_name__", str),
        ("__version__", str),
        ("__author__", list[str]),
        ("__license__", str),
        ("__description__", str),
        ("__keywords__", list[str]),
        ("__url__", str),
        ("__docs_url__", str),
    ],
)
def test_about_datatypes(
    attribute_name: str,
    datatype: type[ParamSpec],
) -> None:
    assert hasattr(__about__, attribute_name)

    attribute_value: Any = getattr(__about__, attribute_name)

    if get_origin(datatype) is list:
        assert isinstance(attribute_value, list)

        if len(attribute_value) > 0:
            data_types: tuple[Any, ...] = get_args(datatype)

            assert all(
                isinstance(list_item, data_types) for list_item in attribute_value
            )
    else:
        assert isinstance(attribute_value, datatype)


@pytest.mark.parametrize(
    ("attribute_name", "protocol"),
    [("__url__", "https://"), ("__docs_url__", "https://")],
)
def test_about_url_protocol(attribute_name: str, protocol: str) -> None:
    assert getattr(__about__, attribute_name).startswith(protocol)
