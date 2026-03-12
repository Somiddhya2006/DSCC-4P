import numpy as np 
from scipy.integrate import quad
def Simp(f,a,b,n):
    x=np.linspace(a,b,n+1)
    h=(b-a)/n
    y=f(x)
    I=(h/3.0)*(y[0]+y[-1]+ 4*(np.sum(y[1:-1:2]))+2*(np.sum(y[2:-2:2])))
    return I
a=0
b=2
f= lambda x: x**3+(2*x**2)+3
step=[1,2,4,6]

for n in step:
    result=Simp(f,a,b,n)
    print(f"Step:{n}, Integration={result}")
f_1=quad(f,a,b)  
print("Verification using scipy:",f_1)