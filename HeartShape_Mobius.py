import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

s = 0.25 # the parameter to control the size of the mobius band
r = 0.5 # the parameter to control the width of the band

mobius_X = lambda u, v: s * 16 * np.sin(u) ** 3 + v * np.cos(u/2) * np.cos(u)
mobius_Y = lambda u, v: s * (13 * np.cos(u) - 5 * np.cos(2 * u) - 3 * np.cos(3 * u)
                             - np.cos(4 * u)) + v * np.cos(u/2) * np.sin(u)
mobius_Z = lambda u, v: s * 5 * np.sin(u) * (1 - abs(-u/np.pi)) ** 2 + v * np.sin(-u/2)

u = np.linspace(-np.pi, np.pi, 100)
v = np.linspace(-r, r, 16)
U, V = np.meshgrid(u, v)

X, Y, Z = mobius_X(U, V), mobius_Y(U, V), mobius_Z(U, V)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.hot)

plt.show()
