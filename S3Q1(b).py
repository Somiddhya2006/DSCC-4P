import numpy as np 
import matplotlib.pyplot as plt

A=np.linspace(0,2*np.pi,9)
print("Array A:\n",A)

B=np.cos(A)
print("\nArray B\n",B)
print("\nSize of B:",np.size(B))

plt.plot(A,B)
plt.title("0 to 2pi vs corresponding Cosine ")
plt.ylabel("Cosine Values")
plt.xlabel("0 to 2pi")
plt.show()