import numpy as np 
arr=np.linspace(1,5,9)
A=arr.reshape(3,3)
print("Array A:\n",A)

brr=np.linspace(1,9,9)
B=brr.reshape(3,3)
print("\nArray B:\n", B)

AB=np.dot(A,B)
ab=AB.T
print("\nTranspose of AB:\n", ab)
a=A.T
b=B.T
axb=np.dot(b,a)
print("\nTraspose of B . Transpose of A:\n", axb)
e=np.equal(ab,axb)
print(e)