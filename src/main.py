import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    x = np.linspace(-5, 5, 100)  # Bosonic coordinate
    theta = np.linspace(-1, 1, 100)  # Grassmann "soul" coordinate
    X, Theta = np.meshgrid(x, theta)
    # Example "superfield" combining bosonic and Grassmann parts
    # Grassmann contribution is linear in Theta
    bosonic_part = np.sin(X)  # Bosonic (commuting) part
    fermionic_part = Theta  # Grassmann (anticommuting) part
    # Combine the two to form a "superfield"
    superfield = bosonic_part + fermionic_part
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Theta, superfield, cmap='viridis', edgecolor='none', alpha=0.8)
    ax.set_title("3D Visualization of a Grassmann-Influenced Superfield", fontsize=14)
    ax.set_xlabel("Bosonic Coordinate (x)")
    ax.set_ylabel("Grassmann Component (θ)")
    ax.set_zlabel("Superfield Value")
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
    plt.show()