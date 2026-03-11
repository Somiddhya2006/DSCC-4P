import numpy as np
import matplotlib.pyplot as plt

I = np.array([0.1,0.2,0.3,0.5,0.7,1.0,1.2,1.5])
V = np.array([1.2,2.5,3.7,6.2,8.5,12.3,14.8,18.5])

# Linear fit V = R*I + c
p = np.polyfit(I, V, 1)
R = p[0]
c = p[1]

V_fit = np.polyval(p, I)

print("Resistance R =", R, "Ohms")

plt.scatter(I, V, label="Data")
plt.plot(I, V_fit, color='red', label="Fitted line")
plt.xlabel("Current (A)")
plt.ylabel("Voltage (V)")
plt.title("V-I Characteristics")
plt.legend()
plt.grid(True)
plt.show()