import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# import matplotlib.animation as animation


iter_func = lambda z, c: (z ** 2 + c) # iteration function

def calc_steps(c, max_iter_num=128):
    z = complex(0, 0) # initial value of z
    num = 0
    while abs(z) < 2 and num < max_iter_num:
        z = iter_func(z, c)
        num += 1
    return num

def display_mandelbrot(x_num=1000, y_num=1000):

    X, Y = np.meshgrid(np.linspace(-2, 2, x_num+1), np.linspace(-2, 2, y_num+1))
    C = X + Y * 1j
    result = np.zeros((y_num+1, x_num+1))

    for i in range(y_num+1):
        for j in range(x_num+1):
            # print('i = %d, j = %d:\t' % (i, j))
            result[i, j] = calc_steps(C[i, j])

    # clist = color_gradient([YELLOW, GREEN], 10)[1:-1]
    # print(clist)
    # clist = ['forestgreen','springgreen','yellowgreen','lightsteelblue','deepskyblue']

    plt.imshow(result, interpolation='bilinear', cmap=plt.cm.hot, # cmap=mpl.colors.ListedColormap(clist),
               vmax=abs(result).max(), vmin=abs(result).min(),
               extent=[-2, 2, -2, 2])
    plt.show()

# def plot_partial_domain(X, Y):
#     x_num, y_num= len(X)-1, len(Y)-1
#     C = X + Y * 1j
#
#     result = np.zeros((y_num+1, x_num+1))
#
#     for i in range(y_num+1):
#         for j in range(x_num+1):
#             print('i = %d, j = %d:\t' % (i, j))
#             result[i, j] = calc_steps(C[i, j])
#
#     fig, ax = plt.subplots()
#     im = ax.imshow(result, interpolation='bilinear', cmap=plt.cm.hot, #cmap=plt.cm.RdYlBu,
#                    origin='lower', extent=[X.min(), X.max(), Y.min(), Y.max()],
#                    vmax=abs(result).max(), vmin=abs(result).min())
#     plt.show()

def plot_zoom_in(center, scale, x_num=1000, y_num=1000):

    X, Y = np.meshgrid(np.linspace(center[0] - 2/scale, center[0] + 2/scale, x_num+1),
                       np.linspace(center[1] - 2/scale, center[1] + 2/scale, y_num+1))
    C = X + Y * 1j
    result = np.zeros((y_num+1, x_num+1))

    for i in range(y_num+1):
        for j in range(x_num+1):
            print('i = %d, j = %d:\t' % (i, j))
            result[i, j] = calc_steps(C[i, j])
    result = (result - result.min())/ (result.max() - result.min()) * result.max()

    plt.imshow(result, interpolation='bilinear', cmap=plt.cm.hot,
              extent=[X.min(), X.max(), Y.min(), Y.max()],
              vmax=abs(result).max(), vmin=abs(result).min())
    plt.show()

if __name__ == "__main__":

    # display_mandelbrot(400, 400)

    # center = (-0.107728667, 0.9067207955)
    # scale = 1000000000
    center = (-0.7132010808817, 0.2998118878397)
    scale = 1e12

    plot_zoom_in(center, scale)
