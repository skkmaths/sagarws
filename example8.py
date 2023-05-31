# programm for computing the dterminant of a given matrix

from itertools import permutations
import numpy as np

#Checks the permutation is even or odd
# if it is even it returns boolean True, else False
def is_permutation_even(permutation):
    inversions = 0
    n = len(permutation)
    for i in range(n):
        for j in range(i + 1, n):
            if permutation[i] > permutation[j]:
                inversions += 1
    return inversions % 2 == 0

n= int( input("Enter the order of the square matrix:"))  # order of the matrix
# create the list of 0 to n
points = [i for i in range(n)]
#matrix = np.identity(3)
matrix = np.empty((n,n))
print("Enter the matrix elements (row-wise):")
for i in range(n):
    for j in range(n):
        matrix[i, j] = float(input(f"Enter element at position ({i + 1}, {j + 1}): "))

det = 0.0

for sigma in permutations(points):
    product = 1.0
    for i in range(n):
        product *=matrix[sigma[i],i]
    if is_permutation_even(sigma):
        det +=product
    else:
        det -=product
print("Determinant of the given matrix is :", det)



