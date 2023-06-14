#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in matrix:
        row_square = []
        for col in row:
            square_col = col * col
            row_square.append(square_col)

        square_matrix.append(row_square)

    return (square_matrix)
