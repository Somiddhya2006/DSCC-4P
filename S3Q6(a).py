import numpy as np

# Coefficient matrix A
A = np.array([
    [2,  1, -1,  3],
    [1, -2,  4, -1],
    [3,  3, 1,  2],
    [4, -1,  5, -3]
], dtype=float)

# Right-hand side vector b
b = np.array([8, -3, 10, 6], dtype=float)

# Number of equations
n = len(b)

# Augmented matrix
Aug = np.hstack((A, b.reshape(-1,1)))

# Gauss Elimination with Partial Pivoting
for i in range(n):
    # Partial Pivoting
    max_row = np.argmax(abs(Aug[i:, i])) + i
    Aug[[i, max_row]] = Aug[[max_row, i]]

    # Elimination
    for j in range(i+1, n):
        factor = Aug[j, i] / Aug[i, i]
        Aug[j, i:] = Aug[j, i:] - factor * Aug[i, i:]

# Back Substitution
x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = (Aug[i, -1] - np.dot(Aug[i, i+1:n], x[i+1:n])) / Aug[i, i]

print("Solution using Gauss Elimination:", x)

# Verification using NumPy linalg
x_verify = np.linalg.solve(A, b)
print("Solution using NumPy linalg:", x_verify)