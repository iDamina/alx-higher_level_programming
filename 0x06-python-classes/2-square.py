#!/usr/bin/python3
""" Square module. """


class Square:
    """ Defines the square module"""

    def __init__(self, size=0):
        """ Initializes a Square instance.

        Args:
            size (int): size of the square.

        Raises:
            TypeError: if size is not integer
            ValueError: if size is < 0

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size  # Private instance attribute 'size'
