import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path

from config_ops import *

TAU = 2 * np.pi
PI = np.pi
DEGREES = TAU/360

def gcd(a, b):
    while (b!=0):
        temp = a % b
        a = b
        b = temp
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

func_rotate = lambda t, r0=1, w0=1, phi_0=0, P0=0+0*1j: r0 * np.exp(1j * (w0 * t + phi_0)) + P0

def my_curve(t, r_list, w_list, phi_list, P_list):

    AC, CD = r_list[2], r_list[3]
    get_A = lambda t_: func_rotate(t_, r_list[0], w_list[0], phi_list[0], P_list[0])
    get_B = lambda t_: func_rotate(t_, r_list[1], w_list[1], phi_list[1], P_list[1])
    get_D = lambda t_: np.sqrt(AC ** 2 + CD ** 2) * np.exp(1j * (np.angle(get_B(t_) - get_A(t_)) + np.angle(AC + 1j * CD))) + get_A(t_)
    return get_D(t)

def my_curve_rotate(t, r_list, w_list, phi_list, P_list):

    AC, CD = r_list[2], r_list[3]
    get_A = lambda t_: func_rotate(t_, r_list[0], w_list[0], phi_list[0], P_list[0])
    get_B = lambda t_: func_rotate(t_, r_list[1], w_list[1], phi_list[1], P_list[1])
    get_D = lambda t_: (np.sqrt(AC ** 2 + CD ** 2) * np.exp(1j * (np.angle(get_B(t_) - get_A(t_)) + np.angle(AC + 1j * CD))) + get_A(t_)) * np.exp(w_list[2] * t * 1j)
    return get_D(t)

class Container(object):
    def __init__(self, **kwargs):
        digest_config(self, kwargs)

    def add(self, *items):
        raise Exception(
            "Container.add is not implemented; it is up to derived classes to implement")

    def remove(self, *items):
        raise Exception(
            "Container.remove is not implemented; it is up to derived classes to implement")

class MyCurve(Container):

    CONFIG = {
        'P_list': [complex(-4, 2.5), complex(3, -1)],
        'r_list': [4, 1, 6.4, -2.4],
        'phi_list': [120 * DEGREES, 30 * DEGREES],
        'T': [29, -31, 31 * 5],
        'rotate_or_not': True,
        'precision_factor': 2,
    }

    def plot_my_curve(self):
        w = 1
        w_list = TAU/self.T[0] * w, TAU/self.T[1] * w, TAU/self.T[2] * w

        if self.rotate_or_not:
            t_total = lcm(lcm(self.T[0], self.T[1]), self.T[2])
            N = int(t_total * 1000 * self.precision_factor)
            print('t_total: %.2f' % t_total)
            # curve = ParametricFunction(function=lambda t: complex_to_R3(my_curve_rotate(t, self.r_list, w_list, self.phi_list, self.P_list)), t_min=0, t_max=t_total, color=BLUE_D, stroke_width=1.2, step_size=t_total/1000/self.precision_factor).set_height(7.2).move_to(ORIGIN)
            t = np.linspace(0, t_total, N+1)
            c = my_curve_rotate(t, self.r_list, w_list, self.phi_list, self.P_list)
            x, y = c.real, c.imag

        else:
            t_total = lcm(self.T[0], self.T[1])
            N = int(t_total * 1000 * self.precision_factor)
            print('t_total: %.2f' % t_total)
            t = np.linspace(0, t_total, N+1)
            c = my_curve(t, self.r_list, w_list, self.phi_list, self.P_list)
            x, y = c.real, c.imag
        fig, ax = plt.subplots()
        ax.plot(x, y, linewidth =0.5)
        ax.set_aspect('equal', 'box')
        plt.show()

if __name__ == "__main__":

    mc = MyCurve(rotate_or_not=True)
    mc.plot_my_curve()

