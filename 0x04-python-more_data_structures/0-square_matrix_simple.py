#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        print()
    new_matrix = []
    new_matrix = [[1]] * len(matrix)#creating new matrix as the same size of matrix
    row_index = 0#indexing no. of row
    for row in matrix:
        new_matrix[row_index] = [x**2 for x in row]#x represents the numbers on a particular row index
        row_index += 1
    return new_matrix
