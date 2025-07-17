import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-1, 1, 50)
y = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(x, y)


theta =10
n = 180 / theta


def ctheta(X, Y):

    return np.arctan2(Y, X)


psi = (X**2 + Y**2)**(n/2) * np.sin(n *ctheta(X, Y))


dy = y[1] - y[0]
dx = x[1] - x[0]
U = np.gradient(psi, dy, axis=0)  
V = -np.gradient(psi, dx, axis=1)  


plt.figure(figsize=(6, 6))
plt.streamplot(X, Y, U, V, color='blue', linewidth=1, density=1.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'Streamlines from Stream Function ψ = (x² + y²)^{n/2} sin({n}θ)')
plt.grid(True)


plt.show()

# Optionally save the plot to a file
# plt.savefig('streamlines.png')