import numpy as np 
def simp(f,a,b,n):
    if n%2!=0:
        raise ValueError("n must be even for Simpson's 1/3 rule")
    x=np.linspace(a,b,n+1)
    y=f(x)
    h=(b-a)/n
    I=(h/3.0)*(y[0]+y[-1]+4*np.sum(y[1:-1:2])+2*np.sum(y[2:-2:2]))
    return I
f=lambda x:np.sin(x)
a=0
b=np.pi

step=[4,10,20]
for n in step:
    result=simp(f,a,b,n)
    print(f"n={n},Integral={result}")