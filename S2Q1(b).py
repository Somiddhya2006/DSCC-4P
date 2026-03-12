import numpy as np 
import matplotlib.pyplot as plt

A=np.arange(20,40)
print("Array A:\n",A)
B=A.reshape(10,2)
print("\nReshaped Array:\n",B)

first=B[:,0]
second=B[:,1]
print("First column:", first)
print("Second column:",second)

plt.plot(second,first)
plt.title("2nd vs 1st")
plt.ylabel("2nd Array")
plt.xlabel("1st Array")
plt.show()