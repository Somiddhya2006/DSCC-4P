import numpy as np 
import matplotlib.pyplot as plt 
x=np.array([1,3,5,7,8,9,10,12,13])
y=np.array([50,-30,-20,20,5,1,30,80,-10])
n=len(x)
t=6
z=0
for i in range (n):
    l=1
    for j in range (n):
        if i!=j:
            l*=(t-x[j])/(x[i]-x[j])
    z+=y[i]*l
print("Value of y at x=6:", z)        

plt.plot(x,y,'-bo',label="Given Data")
plt.plot(t,z,'*r',markersize=12,label="Interpolated Point")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Lagrange Interpolation")
plt.show()
