import numpy as np
import matplotlib.pyplot as plt
import math

def Trap(f,a,b,n):
    h=(b-a)/n
    x=np.linspace(a,b,n+1)
    y=f(x)
    return h*(0.5*y[0] + np.sum(y[1:n]) + 0.5*y[n])

a=0
b=np.pi/2.0
n=1000

m_v=np.arange(0,1.1,0.1)
k_v=[]

for m in m_v:
    f=lambda x:1/np.sqrt(1-m*(np.sin(x)**2))
    k=Trap(f,a,b,n)
    k_v.append(k)

for m,k in zip(m_v,k_v):
    print("m=",round(m,1),"K(m)=",k)

plt.plot(m_v,k_v,marker='o')
plt.title("Complete Elliptical Integral K(m)")
plt.xlabel("m")
plt.ylabel("K(m)")
plt.grid(True)
plt.show()