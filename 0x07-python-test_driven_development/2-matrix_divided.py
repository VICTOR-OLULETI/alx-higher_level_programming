#!/usr/bin/python3
""" Division of matrix division
Definition:
    matrix: list of list
    numbers: float or int
    divisor: float or int
"""


def matrix_divided(matrix, div=1):
    """
    Returns: a new matrix with each element divided by 'div'
    Args:
        matrix (list of list)
        div (int or float)
    The list in the matrix are of the same length
    """
    new_matrix = []
    err_message = 'matrix must be a matrix (list of lists) of integers/floats'

    if not isinstance(matrix, list):
        raise TypeError(err_message)

    if len(matrix):
        length = len(matrix[0])
    else:
        return new_matrix

    if (type(div) not in [int, float]):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")


    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(err_message)

        if (len(row) != length):
            raise TypeError("Each row of the matrix must have the same size")

        for i in row:
            if (type(i) not in [int, float]):
                raise TypeError(err_message)
        new_matrix.append([round(num / div, 2) for num in row])
    if (div == 1):
        return (matrix)

    return (new_matrix)
