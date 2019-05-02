import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as anm
import numpy as np
import math as mt
import pdb

"""
Matplotlib Animation Example

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""
class Movie_2d:

    def __init__(self, fun, dt, t_max, loc, vel, domain, mass, radius=10):
        self.dt = dt
        self.fps = int(mt.floor(1 / dt))
        self.n_max = int(mt.floor(t_max / dt))
        self.loc = np.copy(loc)
        self.vel = np.copy(vel)
        self.domain = domain
        self.mass = mass
        self.radius = radius
        self.fun = fun

        self.fig = plt.figure()
        self.fig.subplots_adjust(left=0.1, bottom=0.1, right=.9, top=.9)

        self.ax = self.fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(domain[0]), ylim=domain[1])
        for el in range(loc.shape[0]):
            self.circ = plt.Circle(self.loc[el, :], self.radius, color='r', fill=False, linewidth=2)
            self.ax.add_patch(self.circ)

        self.frame = plt.Rectangle([0, 0], domain[0][1] - domain[0][0], domain[1][1] - domain[1][0], fc='none')
        self.ax.add_patch(self.frame)

    def generate_frame(self, i):
       # pdb.set_trace()
        loc, vel = self.fun(self.dt, self.mass, self.radius, self.loc, self.vel, self.domain)
        #pdb.set_trace()
        for el in range(loc.shape[0]):
            self.circ.set_center(loc[el, :])
        return self.circ, self.frame

    def animate(self, name):
        animation = anm.FuncAnimation(self.fig, self.generate_frame, frames=self.n_max, interval=10, blit=True)

        fps = self.fps
        try:
            animation.save(name + '.mp4', fps=fps, extra_args=['-vcodec', 'libx264'])
        except ValueError:
            print("\n mp4 file can not be created, will try to create html")
            try:
                animation.save(name + '.html', fps=fps, extra_args=['-vcodec', 'libx264'])
            except:
                print("\n html also can not be created")

class Plot_2d:

    def __init__(self, dt, t_max, loc1_0, loc2_0, vel1_0, vel2_0,
                 domain, radius, m1=1, m2=1, nr=4, nc=5):
        self.fig = plt.figure()
        self.nr = nr
        self.nc = nc
        self.dt = dt
        self.t_max = t_max
        self.loc1_0 = loc1_0
        self.loc2_0 = loc2_0
        self.vel1_0 = vel1_0
        self.vel2_0 = vel2_0
        self.domain = domain
        self.radius = radius
        self.m1 = m1
        self.m2 = m2


    def simulation(self):
        tt = 0
        ii = 0
        loc1, loc2 = self.loc1_0, self.loc2_0
        vel1, vel2 = self.vel1_0, self.vel2_0
        while tt <= t_max:
            [loc1, loc2], [vel1, vel2] = \
                simulation_step(dt=self.dt, m1=self.m1, m2=self.m2, radius=self.radius,
                                loc1_0=loc1, loc2_0=loc2, v1_0=vel1, v2_0=vel2,
                                domain=self.domain)
            tt += dt
            if ii % 5 == 0:
                #pdb.set_trace()
                self.plotting(ii/5+1, loc1.copy(), loc2.copy(), vel1.copy(), vel2.copy())
            ii += 1
        plt.show()

    def plotting(self, ii, loc1, loc2, vel1, vel2):
        ax = self.fig.add_subplot(self.nr, self.nc, ii, aspect='equal')
        # ax = plt.gca()
        # ax.quiver(r1[0], r1[1], r12[0], r12[1], angles='xy', scale_units='xy', scale=1, color="k", width=1.e-3)
        # ax.quiver(0, 0, r1[0], r1[1], angles='xy', scale_units='xy', scale=1, color="k", width=1.e-3)
        # ax.quiver(0, 0, r2[0], r2[1], angles='xy', scale_units='xy', scale=1, color="k", width=1.e-3)
        # ax.quiver(r1[0], r1[1], v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color="g")
        # ax.quiver(r2[0], r2[1], v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color="g")
        # ax.quiver(r1[0], r1[1], v1n[0], v1n[1], angles='xy', scale_units='xy', scale=1, color="y")
        # ax.quiver(r2[0], r2[1], v2n[0], v2n[1], angles='xy', scale_units='xy', scale=1, color="y")
        # ax.quiver(r1[0], r1[1], v1s[0], v1s[1], angles='xy', scale_units='xy', scale=1, color="y")
        # ax.quiver(r2[0], r2[1], v2s[0], v2s[1], angles='xy', scale_units='xy', scale=1, color="y")
        #
        # ax.quiver(r1[0], r1[1], u1[0], u1[1], angles='xy', scale_units='xy', scale=1, color="b")
        # ax.quiver(r2[0], r2[1], u2[0], u2[1], angles='xy', scale_units='xy', scale=1, color="b")
        # ax.quiver(r1[0], r1[1], u1n[0], u1n[1], angles='xy', scale_units='xy', scale=1, color="c")
        # ax.quiver(r2[0], r2[1], u2n[0], u2n[1], angles='xy', scale_units='xy', scale=1, color="c")
        # ax.quiver(r1[0], r1[1], u1s[0], u1s[1], angles='xy', scale_units='xy', scale=1, color="c")
        # ax.quiver(r2[0], r2[1], u2s[0], u2s[1], angles='xy', scale_units='xy', scale=1, color="c")

        # ax.quiver(X, Y, V, U, angles='xy', scale_units='xy', scale=1, color="b")
        c1 = plt.Circle(loc1, self.radius, color='r', fill=False)
        c2 = plt.Circle(loc2, self.radius, color='r', fill=False)
        ax.set_xlim([0, 100])
        ax.set_ylim([0, 100])
        # ax.set_aspec("equal")
        ax.add_patch(c1)
        ax.add_patch(c2)
