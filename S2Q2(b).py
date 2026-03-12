import numpy as np

A=np.array([5,2,6])
theta=np.deg2rad(180)
print("Array A:",A)

R=np.array([[1,0,0],[0,np.cos(theta),-np.sin(theta)],[0,np.sin(theta),np.cos(theta)]])
print("\nArray R:\n",R)
T=np.dot(A,R)
T_1=np.linalg.norm(T)
print("New Array T:\n",T)
print("\nMagnitude of T:\n", T_1)