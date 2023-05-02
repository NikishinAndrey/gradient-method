import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.animation as animation

os.environ['MPLBACKEND'] = 'tkagg'

x = []
y = []
z = []

with open('../../CLionProjects/gradient/cmake-build-debug/result.txt') as f:
    for line in f:
        line = line.rstrip(',') 
        elements = line.split(',')
        x.append(float(elements[0]))
        y.append(float(elements[1]))
        z.append(float(elements[2]))

def f(x):
    return 2 * x[0] ** 2 + 3 * x[1] ** 2 - 4 * x[0] * x[1] + 5 * x[0] - 6 * x[1] + 7

N = 100
xx_0 = [8, 8]

x_plt = np.arange(-10.0, 10.0, 0.1)
y_plt = np.arange(-10.0, 10.0, 0.1)
X, Y = np.meshgrid(x_plt, y_plt)
Z = f([X, Y])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='coolwarm', alpha=0.8)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.view_init(elev=30, azim=-130)
point = ax.scatter(xx_0[0], xx_0[1], f(xx_0), c='red')

xx = xx_0


def update(num):
    point._offsets3d = ([x[num]], [y[num]], [z[num]])
    return point


ani = animation.FuncAnimation(fig, update, frames=N, interval=40)

ani.save('animation.mp4', writer=animation.FFMpegWriter(fps=20))
