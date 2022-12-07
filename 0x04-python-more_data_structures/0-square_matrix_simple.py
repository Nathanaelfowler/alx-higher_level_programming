#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    new_matrix = len(matrix)
    new_matrix = list(map(lambda x: x ** 2, matrix))
    return new_matrix
