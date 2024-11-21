import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

if __name__ == '__main__':
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    x = np.linspace(-5, 5, 100)  # Grassman Number Bosonic coordinate
    theta = np.linspace(-1, 1, 100)  # Grassmann "soul" coordinate
    X, Theta = np.meshgrid(x, theta)
    surf = ax.plot_surface(X, Theta, np.zeros_like(X), cmap='viridis', edgecolor='none', alpha=0.8)
    ax.set_title("3D Visualization of a Grassmann-Influenced Superfield", fontsize=14)
    ax.set_xlabel("Bosonic Coordinate (x)")
    ax.set_ylabel("Grassmann Component (θ)")
    ax.set_zlabel("Superfield Value")
    colorbar = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

    def update(frame):
        # Time-dependent Grassmann evolution
        t = frame * 0.1  # Time variable, adjusted to control the speed of evolution
        # Example "superfield" evolution over time (bosonic and fermionic components)
        bosonic_part = np.sin(X - t)  # Bosonic part evolves with time
        fermionic_part = np.sin(t) * Theta  # Grassmann part depends on time as well
        # Combine the two to form the "superfield"
        superfield = bosonic_part + fermionic_part
        # Update the surface plot data
        ax.clear()
        ax.set_title("3D Visualization of a Grassmann-Influenced Superfield", fontsize=14)
        ax.set_xlabel("Bosonic Coordinate (x)")
        ax.set_ylabel("Grassmann Component (θ)")
        ax.set_zlabel("Superfield Value")
        surf = ax.plot_surface(X, Theta, superfield, cmap='viridis', edgecolor='none', alpha=0.8)
        colorbar.update_ticks()  # Update colorbar to match the new data
        return surf,

    ani = FuncAnimation(fig, update, frames=100, interval=50, blit=False)
    plt.show()