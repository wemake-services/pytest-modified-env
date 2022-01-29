import os

import pytest


def test_regular() -> None:
    """Does not do anything."""
    assert object()


def test_cleans_up_env() -> None:
    """This test add new env value and removes it."""
    os.environ['NEW_ENV'] = '1'

    assert os.environ['NEW_ENV'] == '1'

    os.environ.pop('NEW_ENV')


@pytest.mark.modify_env()
def test_allowed() -> None:
    """It has a marker."""
    os.environ['MARKER_ENV'] = '1'



def test_expected_to_fail() -> None:
    """
    This test modifies the env.

    This test also does not have a marker to allow it.
    Moreover, we test that `xfail` works.
    """
    os.environ['NO_CLEAN_UP'] = '1'
