# pytest-modified-env

[![Build Status](https://github.com/wemake-services/pytest-modified-env/workflows/test/badge.svg?branch=master&event=push)](https://github.com/wemake-services/pytest-modified-env/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/wemake-services/pytest-modified-env/branch/master/graph/badge.svg)](https://codecov.io/gh/wemake-services/pytest-modified-env)
[![Python Version](https://img.shields.io/pypi/pyversions/pytest-modified-env.svg)](https://pypi.org/project/pytest-modified-env/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Pytest plugin to fail a test if it leaves modified `os.environ` afterwards.

Example:

```python
import os

def test_that_modifies_env() -> None:
    os.environ['CUSTOM_ENV'] = '1'
```

With `pytest-modified-env` plugin installed, this test will fail.
Because it adds `CUSTOM_ENV` inside a test and does not clean it up.

In theory it can affect other tests and tests should be isolated!


## Installation

```bash
pip install pytest-modified-env
```


## Extras

In some cases test still might modify the env in this way. 
But, it needs an explicit approval for that:

```python
import os
import pytest

@pytest.mark.modify_env()
def test_that_modifies_env() -> None:
    os.environ['CUSTOM_ENV'] = '1'
```

This test won't fail, eventhough it adds `CUSTOM_ENV`,
because it has `modifies_env` marker.


## License

[MIT](https://github.com/wemake-services/pytest-modified-env/blob/master/LICENSE)
