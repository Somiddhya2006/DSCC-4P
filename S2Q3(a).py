import numpy as np 
import matplotlib.pyplot as plt

x=np.arange(0,2.1,0.2)
y=np.sin(x**2)
print("Data of x:",x)
print("Data of y:",y)
t=0.9
n=len(x)
z=0
for i in range (n):
    L=1
    for j in range (n):
        if i!=j:
            L*=(t-x[j])/(x[i]-x[j])
    z+=L*y[i]
print("Value of y at x=0.9 using Lagrange interpolation",z)
plt.plot(x,y,'bo-',label="Given Data")
plt.plot(t,z,'r*',markersize=12,label="Interpolated point")
plt.xlabel("Values of x")
plt.ylabel("Valuies of y")
plt.legend()
plt.show()