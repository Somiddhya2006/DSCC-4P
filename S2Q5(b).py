import numpy as np
import matplotlib.pyplot as plt

A=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])

B=np.array([[8,3,11],
            [7,4,2],
            [9,7,8]])

print("Matrix A:\n",A)
print("\nMatrix B:\n",B)

C=A+B
print("\nMatrix C = A + B:\n",C)

A1=A.flatten()
C1=C.flatten()

plt.plot(A1,C1,'o-')
plt.xlabel("A (1D array)")
plt.ylabel("C (1D array)")
plt.title("Plot of C vs A")
plt.grid()

plt.show()