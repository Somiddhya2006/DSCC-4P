import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5])
y = np.array([0,0.8,0.9,0.1,-0.8,-1.0])

coeff = np.polyfit(x, y, 3)
p = np.poly1d(coeff)

print("Coefficients:", coeff)

x_fit = np.linspace(min(x), max(x), 100)
y_fit = p(x_fit)

plt.plot(x, y, 'ro', label="Data Points")
plt.plot(x_fit, y_fit, 'b-', label="Cubic Fit")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("NumPy polyfit")
plt.legend()

plt.show()