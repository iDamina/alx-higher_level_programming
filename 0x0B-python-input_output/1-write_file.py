#!/usr/bin/python3
"""Defining write_file function with two arguments."""


def write_file(filename="", text=""):
    """Write filename with UTF8 text format.

    Args:
        filename (str): The name of the file to write.
            text (str): The text to write to the file.
        Returns:
            The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
