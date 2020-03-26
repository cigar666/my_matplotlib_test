import time
import numpy
from matplotlib import pyplot

"""
代码主要参考了：https://github.com/esdalmaijer/abelian_sandpile/blob/master/abelian_sandpile.py
在源代码基础上，将规则改为了满8粒沙粒就往邻近的8个格子散开（将8个沙粒均分给周围八个格子，每格一粒）
"""

# size of the pile-space (each pixel is a pile)
SIZE = (400, 400)

# maximum number of stackable sand grains that will cause a tople

MAXH = 8

# first pile
FPH = 500000
MPC = (200, 200)

# sand field
field = numpy.zeros((SIZE[0]+2, SIZE[1]+2))
field[MPC[0]+1, MPC[1]+1] += FPH

# starting time and iteration
i = 0
t0 = time.time()

# run until a stable state is reached
while numpy.max(field) >= MAXH:

    # find the highest pile
    toohigh = field >= MAXH

    # decrease piles
    field[toohigh] -= MAXH

    # increase piles
    field[1:, :][toohigh[:-1, :]] += MAXH / 8
    field[:-1, :][toohigh[1:, :]] += MAXH / 8
    field[:, 1:][toohigh[:, :-1]] += MAXH / 8
    field[:, :-1][toohigh[:, 1:]] += MAXH / 8

    field[1:, 1:][toohigh[:-1, :-1]] += MAXH / 8
    field[:-1, :-1][toohigh[1:, 1:]] += MAXH / 8
    field[:-1, 1:][toohigh[1:, :-1]] += MAXH / 8
    field[1:, :-1][toohigh[:-1, 1:]] += MAXH / 8

    # reset the overspill
    field[0:1,:] = 0
    field[1+SIZE[0]:,:] = 0
    field[:,0:1] = 0
    field[:,1+SIZE[1]:] = 0

    # increase number of iterations
    i += 1

# ending time
t1 = time.time()
print("%d iterations in %.2f seconds" % (i, t1-t0))

# show piles
field = field[1:1+SIZE[0], 1:1+SIZE[1]]
fig = pyplot.figure(figsize=(20.0, 20.0), dpi=150.0, frameon=False)
ax = pyplot.Axes(fig, [0, 0, 1, 1])
ax.set_axis_off()
fig.add_axes(ax)
ax.imshow(field / numpy.max(field), # cmap=pyplot.cm.hot,
          vmin=0, vmax=1)
pyplot.savefig("sandpiles_max8_%d_%dx%d.png" % (FPH, SIZE[0],SIZE[1]), frameon=False)
pyplot.show()
