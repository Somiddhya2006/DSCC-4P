import numpy as np 
import matplotlib.pyplot as plt
def simp(f,a,b,n):
    if n%2!=0:
        raise ValueError("n must be even")
    n+=1
    x=np.linspace(a,b,n+1)
    y=f(x)
    h=(b-a)/n
    I= (h/3)*(y[0]+y[-1]+4*np.sum(y[1:-1:2])+2*np.sum(y[2:-2:2]))
    return I
def erf(x,n=100):
    if x==0:
        return 0
    f=lambda t: np.exp(-t**2)
    n=100
    if x>0:
        val=simp(f,0,x,n)
    else:
        val=-simp(f,0,-x,n)
    I= (2/np.sqrt(np.pi))*val
    return I

x_val=np.linspace(-3,3,100)
for x in x_val:
    print(f"x={x:.2f}, erf(x)={erf(x):.5f}")
y_val=[erf(x) for x in x_val]

plt.plot(x_val,y_val)
plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.title("erf(x) vs x")
plt.xlabel("x")
plt.ylabel("erf(x)")
plt.show()        
        