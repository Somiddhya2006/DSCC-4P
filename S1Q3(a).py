import numpy as np 
import matplotlib.pyplot as plt 

t=np.array([0,1,2,3,4,5])
T=np.array([30,45,50,52,48,40])
x=2.5
n=len(t)
y=0
for i in range (n):
    L=1
    for j in range (n):
        if i != j:
            L*=(x-t[j])/(t[i]-t[j])
    y+=T[i]*L

print("Temperature at t=2.5 :", y)
plt.plot(t,T,'bo-',label='Given Data')
plt.plot(x,y,'r*', markersize=12, label='Interpolated point') 
plt.xlabel("Time")      
plt.ylabel("Temperature")
plt.legend()
plt.show()