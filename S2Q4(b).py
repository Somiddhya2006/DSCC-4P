import numpy as np 
import matplotlib.pyplot as plt 

V=np.array([1.1,2.1,3.1,4.1,5.1,6.1,7.1,8.1])
P=np.array([5.6,10.4,15.7,20.4,25.5,30.3,35.6,40.5])
print("Velocity:\n",V)
print("\nMomentum:\n",P)

m=np.polyfit(V,P,1)
M=m[0]
c=m[1]
print("Mass:",M)

M_1=np.polyval(m,V)
plt.scatter(V,P,label='Data')
plt.plot(V,M_1,label="Fitted line")
plt.xlabel("Veocity")
plt.ylabel("Momentum")
plt.legend()
plt.show()