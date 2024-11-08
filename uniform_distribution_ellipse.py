import numpy as np 
import matplotlib.pyplot as plt

def generate_points_in_ellipse(n, a, b):
    """Generate n random points uniformly distributed inside an ellipse."""
    # Generate random points in a square bounding box
    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)

    # Keep points that are inside the ellipse defined by (x/a)^2 + (y/b)^2 <= 1
    points = np.array([(x[i], y[i]) for i in range(n) if (x[i]**2 / a**2 + y[i]**2 / b**2) <= 1])
    # If not enough points generate more until we have n points
    while len(points) < n:
        x = np.random.uniform(-1, 1, n - len(points))
        y = np.random.uniform(-1, 1, n - len(points))
        points = np.append(points, [(x[i], y[i]) for i in range (n - len(points)) if (x[i]**2 / a**2 + y[i]**2 / b**2) <= 1], axis = 0)

    return points[:n]

def plot_ellipse(points, a, b):
    """Plot the points and the ellipse."""
    plt.figure()
    plt.scatter(points[:, 0], points[:, 1], alpha = 0.6)
    ellipse = plt.Circle((0, 0), 1, color = 'red', fill = False)
    plt.gca().add_artist(ellipse)
    plt.xlim(-a, a)
    plt.ylim(-b, b)
    plt.title('Random points in ellipse')
    plt.xlabel('X - axis')
    plt.ylabel('Y - axis')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid()
    plt.show()

# Parameters for the ellipse
a = 2 # Semi major axis
b = 1 # Semi minor axis

# Generate and plot points for different n values
for n in [100, 1000, 10000]:
    points = generate_points_in_ellipse(n, a, b)
    plot_ellipse(points, a, b)

