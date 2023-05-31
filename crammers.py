import numpy as np
from determinant import *

def compute_inverse(matrix):
    n = len(matrix)
    cofactor = np.zeros((n,n))
    determinant = det(matrix)
    if determinant == 0:
        raise ValueError("Matrix is not invertible.")
    inverse = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            cofactor[i,j] = det ( np.delete( np.delete(matrix, i, axis=0), j, axis = 1 ) )
    inverse = cofactor.T/determinant
    
    return inverse

def solve_cramers(matrix,b):
    n = len(matrix)
    x = np.zeros(n)
    mat = np.zeros((n,n))
    for i in range(n):
        mat = matrix.copy()    # there will be error if you simply usie mat = matrix
        mat[:,i] = b
        #print(matrix)
        print(mat)
        x[i] = det(mat)/det(matrix)
    return x

m = np.identity(3)
b = np.array([1,1,1])
print(solve_cramers(m,b))