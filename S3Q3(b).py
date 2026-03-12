import numpy as np

A = np.arange(1, 25).reshape(4, 6)
print("Matrix A:\n", A)

first_row = A[0]

max_val = np.max(first_row)
min_val = np.min(first_row)

max_index = np.argmax(first_row)
min_index = np.argmax(first_row)

print("Maximum of first row:", max_val, "Index:", max_index)
print("Minimum of first row:", min_val, "Index:", min_index)