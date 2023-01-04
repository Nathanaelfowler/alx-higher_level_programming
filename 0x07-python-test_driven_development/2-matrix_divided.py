#!/usr/bin/python3
"""compulsory line"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix."""
    res_matrix = []

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if len(row) == len(matrix[0]):
            new_matrix = []
            for i in row:
                if not isinstance(i, (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                else:
                    new_matrix.append(round(i / div, 2))
            res_matrix.append(new_matrix)
        else:
            raise TypeError("Each row of the matrix must have the same size")
    return res_matrix
