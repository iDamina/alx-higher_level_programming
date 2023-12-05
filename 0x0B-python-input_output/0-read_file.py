#!/usr/bin/python3
"""Defining a text read_file function."""


def read_file(filename=""):
    """reads file contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
