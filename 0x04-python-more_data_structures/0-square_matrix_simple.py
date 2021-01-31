#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_mtx = matrix.copy()
    size = len(square_mtx)
    for ind in range(size):
        square_mtx[ind] = list(map(lambda n: n**2, square_mtx[ind]))
    return (square_mtx)
