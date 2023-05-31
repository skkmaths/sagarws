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

def det(matrix):
    n = len(matrix)
    points = [i for i in range(n)]
    determinant = 0.0
    for sigma in permutations(points):
        product = 1.0
        for i in range(n):
            product *=matrix[sigma[i],i]
        if is_permutation_even(sigma):
            determinant +=product
        else:
            determinant -=product
    return determinant


    
