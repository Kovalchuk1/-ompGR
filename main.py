import pandas as pd
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

name = "DS9.txt"
Data = pd.read_csv(name, sep=" ", header=None, names=["x", "y"])
Data2 = pd.DataFrame()

points = np.array(Data)
hull = ConvexHull(points)

ds = plt.figure()
axes = ds.add_axes((0, 0, 1, 1))
plt.axis('off')

axes.scatter(Data["x"], Data["y"], color='black')
plt.xlim([0, 540])
plt.ylim([960, 0])
axes.plot(points[hull.vertices, 0, ], points[hull.vertices, 1], 'b-', lw=4)
plt.savefig('DS9.jpg')

axes2 = ds.add_axes((0, 0, 1, 1))
axes2.plot(points[hull.vertices, 0], points[hull.vertices, 1], 'b-', lw=4)
plt.xlim([0, 540])
plt.ylim([960, 0])
plt.savefig('convexShell.jpg')


