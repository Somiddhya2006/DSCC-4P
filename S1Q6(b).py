import numpy as np
import matplotlib.pyplot as plt

# Range of x values
x = np.linspace(-np.pi, np.pi)

# Functions
y1 = 2 * x * np.sin(2 * x)
y2 = 0.5 * x * np.sinh(x / 2)
y3 = 0.5 * x * np.cosh(x / 2)

# Create subplots in a row
fig, axs = plt.subplots(1, 3, figsize=(12,4))

# First plot
axs[0].plot(x, y1)
axs[0].set_xlabel("x")
axs[0].set_ylabel("y")
axs[0].set_title("My Plot")

# Second plot
axs[1].plot(x, y2)
axs[1].set_xlabel("x")
axs[1].set_ylabel("y")
axs[1].set_title("My Plot")

# Third plot
axs[2].plot(x, y3)
axs[2].set_xlabel("x")
axs[2].set_ylabel("y")
axs[2].set_title("My Plot")

plt.tight_layout()
plt.show()