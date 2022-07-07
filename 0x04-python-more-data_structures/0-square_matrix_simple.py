#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newList = [[num ** 2 for num in elem] for elem in matrix]
    return (newList)
