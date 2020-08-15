import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


class Fractal(object):

    def __init__(self, iter_func, max_iter_num=64, convergence_radius=2, z0=0, calc_method=0):

        self.iter_func = iter_func
        self.max_iter_num = max_iter_num
        self.convergence_radius = convergence_radius
        self.set_init_z(z0)
        if calc_method == 0:
            self.calc_steps = self.calc_steps_01
        else:
            self.calc_steps = self.calc_steps_02

        self.center = 0, 0
        self.scale = 1
        self.anim_id = 0
        self.save_path = 'E:\\GitHub\\my_matplotlib_test\\fractal_anim\\pictures\\'

    def set_center(self, center):
        self.center = center
        return self

    def set_scale(self, scale):
        self.scale = scale
        return self

    def set_init_z(self, z0=complex(0, 0)):
        self.init_z = z0 # set initial value of z

    def calc_steps_01(self, c):
        z = self.init_z # initial value of z
        num = 0
        while abs(z) < self.convergence_radius and num < self.max_iter_num:
            z = self.iter_func(z, c)
            num += 1
        return num

    def calc_steps_02(self, c):

        z = self.init_z # initial value of z
        num = 0
        while num < self.max_iter_num:
            z = self.iter_func(z, c)
            num += 1
            if abs(z) > 20 * self.convergence_radius:
                return (sigmoid(np.abs(z)) - 0.5) * 40 + 1
        return 0

    # def display_mandelbrot(self, x_num=1000, y_num=1000):
    #
    #     X, Y = np.meshgrid(np.linspace(-2, 2, x_num+1), np.linspace(-2, 2, y_num+1))
    #     C = X + Y * 1j
    #     result = np.zeros((y_num+1, x_num+1))
    #
    #     for i in range(y_num+1):
    #         for j in range(x_num+1):
    #             # print('i = %d, j = %d:\t' % (i, j))
    #             result[i, j] = self.calc_steps(C[i, j])
    #
    #     # clist = color_gradient([YELLOW, GREEN], 10)[1:-1]
    #     # print(clist)
    #     # clist = ['forestgreen','springgreen','yellowgreen','lightsteelblue','deepskyblue']
    #
    #     plt.imshow(result, interpolation='bilinear', cmap=plt.cm.hot, # cmap=mpl.colors.ListedColormap(clist),
    #                vmax=abs(result).max(), vmin=abs(result).min(),
    #                extent=[-2, 2, -2, 2])
    #     plt.show()

    def plot_zoom_in(self, center, scale, ratio=1/1, x_num=1000, y_num=1000):

        X, Y = np.meshgrid(np.linspace(center[0] - 2/scale * ratio, center[0] + 2/scale * ratio, x_num+1),
                           np.linspace(center[1] - 2/scale, center[1] + 2/scale, y_num+1))
        C = X + Y * 1j
        result = np.zeros((y_num+1, x_num+1))

        for i in range(y_num+1):
            for j in range(x_num+1):
                print('i = %d, j = %d:\t' % (i, j))
                result[i, j] = self.calc_steps(C[i, j])
        result = (result - result.min()) / (result.max() - result.min()) * result.max()

        plt.imshow(result, interpolation='bilinear', #cmap=plt.cm.hot,
                  extent=[X.min(), X.max(), Y.min(), Y.max()],
                  vmax=abs(result).max(), vmin=abs(result).min())
        plt.show()
        # plt.savefig()

    def save_pic(self, name, center, scale, x_num=1000, y_num=1000, dpi=600, reverse_color=False):

        ratio = 1920/1080
        X, Y = np.meshgrid(np.linspace(center[0] - 2/scale * ratio, center[0] + 2/scale * ratio, x_num+1),
                           np.linspace(center[1] - 2/scale, center[1] + 2/scale, y_num+1))
        C = X + Y * 1j
        result = np.zeros((y_num+1, x_num+1))

        for i in range(y_num+1):
            for j in range(x_num+1):
                print('i = %d, j = %d:\t' % (i, j))
                result[i, j] = self.calc_steps(C[i, j])
        result = (result - result.min()) / (result.max() - result.min()) * result.max()
        if reverse_color:
            result = result.max() - result

        # fig, ax = plt.subplots()
        plt.imshow(result, interpolation='bilinear', # cmap=plt.cm.winter,
                   origin='lower', extent=[X.min(), X.max(), Y.min(), Y.max()],
                   vmax=abs(result).max(), vmin=abs(result).min(), animated=True)
        plt.subplots_adjust(left=0.0, right=1, wspace=0.25, hspace=0.25, bottom=0.00, top=1)
        plt.savefig(self.save_path+name, dpi=dpi)


class MandelbrotSet(Fractal):
    def __init__(self, iter_func=lambda z, c: (z ** 2 + c), **kwargs):
        Fractal.__init__(self, iter_func=iter_func, **kwargs)


if __name__ == "__main__":

    frac = Fractal(iter_func=lambda z, b: b ** z, max_iter_num=64, convergence_radius=500, z0=1, calc_method=1)
    center = -0.484532, 0.667015
    scale = 1281.8 * 0.8

    # frac.plot_zoom_in(center, scale, ratio=1920/1080, x_num=108 * 2, y_num=192 * 2)
    frac.save_pic('frac_12.png', center=center, scale=scale, x_num=108 * 40, y_num=192 * 40, dpi=750)
