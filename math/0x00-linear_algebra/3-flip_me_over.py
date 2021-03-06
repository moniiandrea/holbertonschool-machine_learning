#!/usr/bin/env python3
def matrix_transpose(matrix):
    '''
    matrix_transpose: returns the transpose of a 2D matrix
    '''
    matrix_T = []
    for i in range(len(matrix[0])):
        new_mat = []
        for j in matrix:
            new_mat.append(j[i])
        matrix_T.append(new_mat)
    return matrix_T

# matrix_transpose = __import__('3-flip_me_over').matrix_transpose

mat1 = [[1, 2], [3, 4]]
print(mat1)
print(matrix_transpose(mat1))
mat2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]
print(mat2)
print(matrix_transpose(mat2))