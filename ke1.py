# Comments in Python start with \"#\". The Python interpreter ignores whatever is 
#    after the \"#\" so we can leave human readable notes here.
#
# import functions we'll need later. These modules are kind of the magic of python,
#   they allow for a relatively lightweight language that can be extended easily 
#   to have great power
#   For this example we use PyPlot, a popular graphing package. We also use numpy 
#   which gives access to a lot of math tools.
#
import numpy as np
from matplotlib import pyplot as plt
#
# define a function. This is one of the most important things in programming, writing a bit of code
#    that can be used later. It's a function, in this case a function of two variables.
#
def dx(v, dt): 
    return v*dt

x_1 = dx(3,0.001)   # Use the function
print(f"Our first differential dx = {x_1}")  # Display the result
# set initial conditions
t_0 = 0
x_0 = 0
t_f = 5     # seconds
dt = 0.5    # seconds.     ___ TRY CHANGING THIS YOURSELF ____
v = 2       # meters / second
num_pts = int( (t_f - t_0) / dt )  # int() truncates floating point numbers

# create variables to store our results
t = list(np.zeros(num_pts))
x = list(np.zeros(num_pts))
x[0] = x_0

# add up the baby steps
for i in range(num_pts-1):
    t[i+1] = t[i] + dt
    x[i+1] = x[i] + dx(v, dt)

# graph the result
plt.plot(t,x,'.')
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")
plt.title("Kinematic Equation #1")
plt.show()
print(f"This graph is generated from lists with {len(x)} points.\\nThe variable num_pts = {num_pts}")