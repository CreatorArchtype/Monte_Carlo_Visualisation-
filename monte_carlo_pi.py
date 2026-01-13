import numpy as np
import matplotlib.pyplot as plt

points = np.loadtxt("random_points.txt", skiprows=1)

x = points[:, 0]
y = points[:, 1]

inside = (x**2 + y**2) <= 1

M = np.sum(inside)
N = len(points)
pi_estimate = 4 * M / N
pi_actual = np.pi
error = abs(pi_estimate - pi_actual)

print(f"Total points (N)        : {N}")
print(f"Points inside circle (M): {M}")
print(f"Estimated pi            : {pi_estimate}")
print(f"Actual pi               : {pi_actual}")
print(f"Absolute error          : {error}")


plt.figure()
plt.scatter(x[inside], y[inside], s=1)
plt.scatter(x[~inside], y[~inside], s=1)

theta = np.linspace(0, np.pi / 2, 500)
plt.plot(np.cos(theta), np.sin(theta))

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.gca().set_aspect('equal')

plt.title("Monte Carlo Estimation of π")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

