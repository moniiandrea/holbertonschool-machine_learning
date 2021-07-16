#!/usr/bin/env python3
# Function matrix_shape(matrix)

def matrix_shape(matrix):
    '''
    matrix_shape: calculates the shape of a matrix
    '''
    mat = matrix
    shape = []
    while type(mat) == list:
        shape.append(len(mat))
        mat = mat[0]
    return shape

#matrix_shape = __import__('2-size_me_please').matrix_shape

mat1 = [[1, 2], [3, 4]]
print(matrix_shape(mat1))
mat2 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
        [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]]
print(matrix_shape(mat2))
mat3 = [[2,3,4],[3,1,8],[8,9,7]]
print(matrix_shape(mat3))