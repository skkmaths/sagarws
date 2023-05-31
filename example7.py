
# Matrix inverse

import numpy as np

# Read the matrix dimensions from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initialize an empty matrix
matrix = np.empty((rows, cols))

# Read the matrix elements from the user
print("Enter the matrix elements (row-wise):")
for i in range(rows):
    for j in range(cols):
        matrix[i, j] = float(input(f"Enter element at position ({i + 1}, {j + 1}): "))

# Calculate the inverse of the matrix
try:
    inverse = np.linalg.inv(matrix)
    print("\nInverse Matrix:")
    print(inverse)
except np.linalg.LinAlgError:
    print("The matrix is not invertible.")

print( "The the square of the matrix is :", matrix@matrix)


