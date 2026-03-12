import numpy as np

f=lambda x: 4*x**3 + 1

a=1
b=4

step=[2,5,10]

def Trap(f,a,b,n):
    h=(b-a)/n
    x=np.linspace(a,b,n+1)
    y=f(x)
    I=h*((y[0]+y[-1])/2 + np.sum(y[1:-1]))
    return I

for n in step:
    t=Trap(f,a,b,n)
    print(f"n={n}, Integral={t}")