#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    tmp_loc = []
    for x in matrix:
        tmp_loc.append(list(map(lambda x: x**2, x)))
    return (tmp_loc)
