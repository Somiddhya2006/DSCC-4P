import numpy as np
import matplotlib.pyplot as plt

arr = np.linspace(0, 10, 20)

cumsum_arr = np.cumsum(arr)

print("Original Array:")
print(arr)

print("\nCumulative Sum Array:")
print(cumsum_arr)


plt.plot(arr, cumsum_arr)
plt.title("Cumulative Sum vs Original Array")
plt.xlabel("Original Array Values")
plt.ylabel("Cumulative Sum")
plt.grid(True)
plt.show()