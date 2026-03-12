import numpy as np 
a=np.arange(20)
print(a)
A=a.reshape(5,4)
print(A)
B=A.T
print(B)

C=np.dot(A,B)
print(C)