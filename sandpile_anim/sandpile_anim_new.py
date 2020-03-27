import time
import numpy
from matplotlib import pyplot



def get_sandpile_field(add_sand_num, add_center, field, MAXH = 4):

    field[add_center[0]+1, add_center[1]+1] += add_sand_num

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
    t1 = time.time()
    print("%d iterations in %.2f seconds" % (i, t1-t0))
    return field

    # ending time

# size of the pile-space (each pixel is a pile)
SIZE = (600, 600)

init_sand_num = 441 * 500
final_sand_num = 400000
center = (300, 300)

init_field = numpy.zeros((SIZE[0]+2,SIZE[1]+2))
field = get_sandpile_field(init_sand_num, center, init_field)

sand_num = init_sand_num
add_num = 500

while sand_num < final_sand_num:
    field = get_sandpile_field(add_num, center, field)
    sand_num += add_num
    # show piles
    field_on_screnn = field[1:1+SIZE[0], 1:1+SIZE[1]]
    fig = pyplot.figure(figsize=(20.0, 20.0), dpi=150.0, frameon=False)
    ax = pyplot.Axes(fig, [0, 0, 1, 1])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(field_on_screnn / numpy.max(field_on_screnn), # cmap=pyplot.cm.hot,
              vmin=0, vmax=1)
    pyplot.savefig("sandpiles_%dx%d_num_%d.png" % (SIZE[0], SIZE[1], int(sand_num/add_num)), frameon=False)


