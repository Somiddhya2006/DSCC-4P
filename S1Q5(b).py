import numpy as np
import matplotlib.pyplot as plt

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[10,11,12],[13,14,15],[16,17,18]])
A=np.array(a)
B=np.array(b)
print("matrix A\n",A)
print("matrix B\n",B)

A_1d=A.ravel()
B_1d=B.ravel()
print("1D array A:\n",A_1d)
print("1D array B:\n",B_1d)

B_1d_squared =np.square(B_1d)
print("B_1d_square\n",B_1d_squared)

plt.plot(B_1d_squared,A_1d)
plt.title("Plot of squared B vs A")
plt.xlabel("B 1D square")
plt.ylabel("A")
plt.grid(True)
plt.legend()
plt.show()