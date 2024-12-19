# How to Contribute

Thank you for considering contributing to our project! Here are some guidelines to help you get started.

## Reporting Bugs

> [!CAUTION]
> Do not open up a GitHub issue if the bug is a security vulnerability, and instead open a [draft security advisory](https://github.com/RyanLua/InstaWebhooks/security/advisories/new) instead.

1. Ensure the bug was not already reported by searching on GitHub under [Issues](https://github.com/RyanLua/InstaWebhooks/issues).
2. If you're unable to find an open issue addressing the problem, open a new one. Be sure to include a title and clear description, as much relevant information as possible, and a code sample or an executable test case demonstrating the expected behavior that is not occurring.

## Suggesting Features

1. Check if the feature has already been suggested by searching on GitHub under [Issues](https://github.com/RyanLua/InstaWebhooks/issues).
2. If the feature hasn't been suggested, open a new issue. Provide a clear and detailed explanation of the feature, why it would be useful, and how it should work.

## Coding Conventions

- Follow [PEP 8](https://peps.python.org/pep-0008/) for Python code.
- Write clear, concise commit messages.
- Include comments and docstrings where necessary.

This project uses [Black](https://github.com/psf/black) for code styling and [Pylint](hhttps://github.com/pylint-dev/pylint) for linting.

## Installation

For installing this project, see "[Installation](https://github.com/RyanLua/InstaWebhooks/wiki/Installation)."

This project supports and recommends [installing as a development container](https://github.com/RyanLua/InstaWebhooks/wiki/Installation#from-development-container) for contributing.

## Building Documentation

Our documentation is built using [Sphinx](https://pypi.org/project/Sphinx/). The documentation is written in reStructuredText.

To install the documentation dependencies, run:

```console
$ pip install -r docs/requirements.txt
```

To build the documentation with autobuild (recommended), run:

```console
$ sphinx-autobuild docs/source docs/_build/html
```

To build the documentation without autobuild, run:

```console
$ cd docs
$ make html
```

The built documentation will be in `docs/_build/html`.