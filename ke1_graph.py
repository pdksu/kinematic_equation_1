#!python
# Python 3.9.6
#
#  2025-03-29 Simple differential equation integrator
#     for kinematic equation number 1
#
from time import time
import matplotlib.pyplot as plt
from numpy import linspace

def dx(v:float, dt:float) -> float:
    return v*dt

if __name__ == '__main__':
    # -- kinematics setup --
    dt = 0.005  # time step in seconds
    v = 1.5     # in units of meters
    x_0 = 0.0   # meters
    t_0 = 0.0   # seconds
    t_f = 5     # seconds
    t = linspace(t_0, t_f, round((t_f-t_0)/dt)) # t array
    x = t-t # same sized array but full of zeros
    t_last = t[0]
    t[0], x[0] = t_0, x_0

    #-- calculate motion --
    idx = 0
    x[0] = x_0
    while(t_last < t_f):
        idx += 1
        x[idx] = x[idx-1] + dx(v, dt)
        t_last = t[idx]
        # the t's were already filled in by the linspace() command above

    
    #-- display setup --
    plot_animation_duration = 5 # seconds for drawing the whole curve
    plot_delay = plot_animation_duration / len(t) # time to wait between points
    plot_delay = max(0.001, plot_delay - 0.001) # machine needs 10 ms to update
    print(f"delay={plot_delay}, npts = {len(t)}")

    plt.ion()  # turns on interactive mode
    graph, = plt.plot(t,x,'.')   # set up graph 'o' for bigger points
    plt.xlabel("Time (s)")
    plt.ylabel("Distance (m)")
    t_start = time()
    for i, t_i in enumerate(t):  # show an increasing number of points
        graph.set_xdata(t[:i])
        graph.set_ydata(x[:i])
        plt.draw()
        plt.pause(plot_delay)

    t_end = time()
    print(f"Elapsed time {t_end-t_start}. Off target by {100*((t_end-t_start)/plot_animation_duration - 1)} percent")
    plt.ioff()                  # turn off interactive mode
    plt.show()                  # necessary to avoid closing the plot window