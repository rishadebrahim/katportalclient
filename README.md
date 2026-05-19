katportalclient
===============

[![Doc Status](https://readthedocs.org/projects/katportalclient/badge/?version=latest)](http://katportalclient.readthedocs.io/en/latest)
[![PyPI Version](https://img.shields.io/pypi/v/katportalclient.svg)](https://pypi.python.org/pypi/katportalclient)
[![Python Versions](https://img.shields.io/pypi/pyversions/katportalclient.svg)](https://pypi.python.org/pypi/katportalclient/)
[![Unit tests](https://github.com/rishadebrahim/katportalclient/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/rishadebrahim/katportalclient/actions/workflows/unit-tests.yml)

A client for simple access to **katportal**, via websocket and HTTP connections.
The HTTP methods allow once-off requests, like the current list of schedule blocks.
For continuous updates, use the Pub/Sub methods, which work over a websocket.

Dependencies
------------
Details can be found in `setup.py` but basically it is only:

- [katversion](https://pypi.org/project/katversion/)
- [tornado](http://www.tornadoweb.org) is used as the web framework and for its asynchronous functionality.

**Note:** `setup.py` depends on katversion, so make sure that is installed before installing the package.

Unit tests
----------

Unit tests are run by the GitHub Actions workflow in
`.github/workflows/unit-tests.yml` on pushes and pull requests. The workflow
runs `python -m pytest katportalclient/test/test_client.py` against Python 3.8
and 3.9.

The latest local test run in this workspace used:

```bash
.venv/bin/python -m pytest katportalclient/test/test_client.py
```

Result: `56 passed, 56 warnings`.

Install
-------

```bash
pip install katportalclient
```

Example usage
-------------

See the `examples` folder for code that demonstrates some usage scenarios.
