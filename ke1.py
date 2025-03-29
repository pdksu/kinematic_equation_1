#!python
# Python 3.9.6
#
#  2025-03-29 Simple differential equation integrator
#     for kinematic equation number 1
#

def dx(v:float, dt:float) -> float:
    return v*dt

if __name__ == '__main__':
    dt = 0.001  # 1 millisecond
    v = 1.5     # in units of m/s
    x_0 = 0.0   # meters
    t_0 = 0.0   # seconds
    t_f = 5     # seconds

    t = t_0
    x = x_0
    while (t<t_f):
        x += dx(v,dt)
        t += dt
        print(f"{t}, {x}")