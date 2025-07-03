"""Initalizer module for pointing towards main module."""

import sys

__version__ = "0.1.4"


if __name__ == "__main__":
    from instawebhooks.__main__ import main

    sys.exit(main())
