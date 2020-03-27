import time
import numpy
from matplotlib import pyplot

def plot_sandpile(sand_num, SIZE, center):

    # maximum number of stackable sand grains that will cause a tople
    # (should be dividable by 4!)
    MAXH = 4

    # first pile
    FPH = sand_num
    MPC = center

    # sand field
    field = numpy.zeros((SIZE[0]+2,SIZE[1]+2))
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
        field[1:,:][toohigh[:-1,:]] += MAXH / 4
        field[:-1,:][toohigh[1:,:]] += MAXH / 4
        field[:,1:][toohigh[:,:-1]] += MAXH / 4
        field[:,:-1][toohigh[:,1:]] += MAXH / 4

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
    pyplot.savefig("sandpiles_%dx%d_num_%d.png" % (SIZE[0],SIZE[1], int(sand_num/500)), frameon=False)


for i in range(165, 1000+1):
    sand_num = i * 500
    SIZE = (600, 600)
    center = (300, 300)
    plot_sandpile(sand_num, SIZE, center)
