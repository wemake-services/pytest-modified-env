# pytest-modified-env

[![wemake.services](https://img.shields.io/badge/%20-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services)
[![Build Status](https://github.com/wemake-services/pytest-modified-env/workflows/test/badge.svg?branch=master&event=push)](https://github.com/wemake-services/pytest-modified-env/actions?query=workflow%3Atest)
[![Python Version](https://img.shields.io/pypi/pyversions/pytest-modified-env.svg)](https://pypi.org/project/pytest-modified-env/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Pytest plugin to fail a test if it leaves modified `os.environ` afterwards.

Example:

```python
import os

def test_that_modifies_env() -> None:
    os.environ['CUSTOM_ENV'] = '1'
```

With `pytest-modified-env` plugin installed, this test will fail:

```
___________________________ test_that_modifies_env ____________________________
test_that_modifies_env:4: in pytest_runtest_call
E   RuntimeError: os.environ was changed
```

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
