import pytest

from src.execution_environment import Environment


def test_as_list():
    actual = Environment.as_list()
    assert 3 == len(actual)


@pytest.mark.parametrize(("param", "expected"), [("dev", "dev")])
def test_get_by(param, expected):
    actual = Environment.get_by(param)
    assert actual.value == expected
