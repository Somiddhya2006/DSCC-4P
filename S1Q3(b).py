import numpy as np 
a=np.arange(12)
print(a)
A=a.reshape(3,4)
print(A)
B=A.T
print(B)

C=np.dot(A,B)
print(C)