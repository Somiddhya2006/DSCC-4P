import numpy as np 
from scipy.integrate import quad 
def Trap(f,a,b,n):
    x=np.linspace(a,b,n+1)
    h=(b-a)/n
    y=f(x)
    I=(h/2)*(y[0]+y[-1]+ 2*(np.sum(y[1:-1:1])))
    return I
a=0
b=1
f= lambda x: 4*( 1/(1+x**2) )
step=[1,2,3,4]

for n in step:
    result=Trap(f,a,b,n)
    print(f"Step:{n}, Integration={result}")
    
f_1=quad(f,a,b)
print("Verification using scipy:", f_1)