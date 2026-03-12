import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 400)

f = np.cos(x**2)**2 + 0.5*(x**2)
g = np.sin(x**2 + np.pi/2)**2 + x**2

plt.plot(x, f, 'b-', label='f(x)')
plt.plot(x, g, 'r--', label='g(x)')

plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot of f(x) and g(x)")
plt.legend()

plt.show()