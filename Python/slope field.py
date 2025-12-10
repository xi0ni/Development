import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x, y):
    return x**2 * (y - 1)

# Grid points
x = np.arange(-1, 2, 1)  # -1, 0, 1
y = np.arange(0, 4, 1)   # 0, 1, 2, 3
X, Y = np.meshgrid(x, y)

# Compute vector components
U = 1          # Horizontal component
V = f(X, Y)    # Vertical component

# Normalize vectors for uniform arrow length
N = np.sqrt(U**2 + V**2)
U2 = U / N
V2 = V / N

# Plot slope field
plt.figure(figsize=(8, 8))  # Bigger figure for visibility
plt.quiver(X, Y, U2, V2, scale=20, width=0.005, pivot='middle', color='blue')

# Set expanded plot limits
plt.xlim(-1.25, 1.25)
plt.ylim(-0.25, 3.25)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Slope Field (Grid Spacing = 1, Expanded)")
plt.grid(True)

plt.show()
