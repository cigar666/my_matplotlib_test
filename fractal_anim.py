from fractal_by_iteration import *

frac = Fractal(iter_func=lambda z, b: b ** z, max_iter_num=64, convergence_radius=500, z0=1, calc_method=1)
center = np.array([-0.484532, 0.667015])

s_0 = 0.8
s_n = 60000
n = 240
a = np.e ** (np.log(s_n / s_0) / n)
s = np.array([s_0 * a ** i for i in range(n)])

s_i = np.log(s)

# move center
# for i in range(30):
#     frac.save_pic('frac_move_%d.png' % (i+1), center * i/n, s_0, x_num=108 * 10, y_num=192 * 10)

# scale
# for i in range(n):
#     frac.save_pic('frac_scale_%d.png' % (i+1), center, s[i], x_num=108 * 10, y_num=192 * 10)

for i in range(8):
    for j in range(30):
        m = i + j * 8
        frac.save_pic('frac_scale_%d.png' % (m+1), center, s[m], x_num=108 * 10, y_num=192 * 10)

