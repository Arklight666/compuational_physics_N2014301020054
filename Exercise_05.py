import pylab as pl

import math as mt

class cannon_shells:
    def __init__(self, initial_velocity = 0.7, g = 0.0098, range = 0, height = 0,\
                 time_step = 0.01, initial_angle = 30.0, da = 5.0):
        self.v = [initial_velocity]
        self.a = [initial_angle]
        self.g = g
        self.dt = time_step
        self.da = da
        self.x = [range]
        self.y = [height]

    def run(self):
        _a = self.a[0]
        while(_a <= 60):
            _a += self.da
            self.a.append(self.a[-1] + self.da)
            t = 2 * mt.sin(_a / 180.0 * mt.pi) * self.v[0]/self.g
            vx = mt.cos(_a / 180.0 * mt.pi) * self.v[0]
            vy = mt.sin(_a / 180.0 * mt.pi) * self.v[0]
            _time = 0
            xi = [0]
            yi = [0]
            while(_time < t):
                xi.append(xi[-1] + self.dt * vx)
                yi.append(yi[-1] + self.dt * vy)
                vx = vx
                vy = vy - self.g * self.dt
                _time += self.dt
            self.x = self.x + xi
            self.y = self.y + yi

    def show_results(self):
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 16,
        }
        pl.title('The trajectory of a cannon shell')
        pl.text(0.95 * self.x[-1], 0.95 * max(self.y),\
                'No drag', fontdict=font)
        pl.plot(self.x,self.y)
        pl.xlabel('x($km$)')
        pl.ylabel('y($km$)')
        pl.show()

a = cannon_shells()
a.run()
a.show_results()
