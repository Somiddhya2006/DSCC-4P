import numpy as np

even = np.arange(2, 20, 2).reshape(3, 3)
odd = np.arange(1, 18, 2).reshape(3, 3)

commutator = np.dot(even, odd) - np.dot(odd, even)

print(commutator)