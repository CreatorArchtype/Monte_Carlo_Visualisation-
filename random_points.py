import numpy as np

N = 10000

x = np.random.rand(N)
y = np.random.rand(N)

points = np.column_stack((x, y))

np.savetxt(
    "random_points.txt",
    points,
    fmt="%.6f",
    header="x y",
    comments=""
)

print("random_points.txt generated successfully")

