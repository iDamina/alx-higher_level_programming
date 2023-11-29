#!/usr/bin/python3
"""module for matrix_divided method."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix: A list of lists of ints or floats.
        div: The divisor of the matrix.
    Raises:
        TypeError: If the matrix is not list of lists containing int or floats.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is zero.
    Returns:
        A new matrix representing the result of the division.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be matrix (list of lists) " +
                                "of integers/floats")
    return ([[round(x / div, 2) for x in row] for row in matrix])


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
