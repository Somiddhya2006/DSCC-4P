import numpy as np

A = np.linspace(1, 10, 10)

print("Array A:")
print(A)

B = A.reshape(5, 2)

print("\nArray B (5x2):")
print(B)

print("\nSum along columns:")
print(np.sum(B, axis=0))

print("\nSum along rows:")
print(np.sum(B, axis=1))

print("\n Product along columns:")
print(np.prod(B, axis=0))

print("\n Product along rows:")
print(np.prod(B, axis=1))


print("\nMean of B:", np.mean(B))
print("Maximum value in B:", np.max(B))
print("Minimum value in B:", np.min(B))
print("Standard Deviation of B:", np.std(B))
print("Variance of B:", np.var(B))