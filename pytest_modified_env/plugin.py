import os
from typing import Iterator, Mapping

import pytest
from _pytest import config, nodes  # noqa: WPS436


def pytest_configure(config: config.Config) -> None:  # noqa: WPS442
    """
    Hook to be executed on import.

    We use it define custom markers.
    """
    config.addinivalue_line(
        'markers',
        (
            'modify_env: when marked with this marker, ' +
            'we allow this test to modify env'
        ),
    )


@pytest.hookimpl(hookwrapper=True, tryfirst=True)  # noqa: WPS110
def pytest_runtest_call(item: nodes.Item) -> Iterator[None]:  # noqa: WPS110
    """
    Custom pytest hook implementation that fires for all tests before they run.

    Docs: https://docs.pytest.org/en/6.2.x/reference.html
    See: _pytest.hookspec.pytest_runtest_call
    """
    if item.get_closest_marker('modify_env'):
        yield
        return  # This test can modify env, user declared it

    old_environ = _prepare_env()

    yield

    recent = _prepare_env()
    if old_environ != recent:
        # TODO: better `dict` diff:
        raise RuntimeError('os.environ was changed')


def _prepare_env() -> Mapping[str, str]:
    environ = os.environ.copy()
    # This value always changes:
    environ.pop('PYTEST_CURRENT_TEST', None)
    return environ
