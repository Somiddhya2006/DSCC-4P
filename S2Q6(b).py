import numpy as np 
import matplotlib.pyplot as plt 

x=np.arange(1,10,0.5)
print("Values of x:\n",x)

fx=(x**2)+x
print("\nValues of f(x):\n",fx)

plt.scatter(x,fx)
plt.plot(x,fx)
plt.ylabel("f(x)")
plt.xlabel("x")
plt.legend()
plt.show()