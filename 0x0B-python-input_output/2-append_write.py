#!/usr/bin/python3
"""Defines the append_write function."""


def append_write(filename="", text=""):
    """Appends filename with UTF8 text file formating."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
