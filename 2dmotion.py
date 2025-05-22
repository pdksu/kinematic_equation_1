# 2 dimensional motion
#
# We will start with the ball rolling off the table, a problem
# that we did over and over this year.
#
# One important thing to plan, when writing a program, is the data structure.
# Now that we have 2 dimensions, our x --> a vector with 2 components.
# We will use numpy arrays to do for this.
# We will also use numpy arrays to do the math, so we can do
# vector math, like adding two vectors together.

import numpy as np
from matplotlib import pyplot as plt

def dv(a: np.array, dt: float) -> np.array:
    """
    Calculate the change in velocity given acceleration and time step.
    Notice that we have added type hints to the function.
    This is a good idea, it helps us remember what the function does.
    The syntax of type hints is:
    def function_name(variable_name: type) -> return_type:
    """
    return a*dt # type hinting is not enforced, but it is a good idea. Also cool, multiply a vector by a scalar, super easy.
def dx(v: np.array, dt: float) -> np.array:
    """
    Calculate the change in position given velocity and time step.
    """
    return v*dt # Just like before...

def roll_off_table(H: float, v_0: np.array, dt: float) -> tuple:
    """
    Main function to find time and position that ball hits the floor.
    """
    # set initial conditions
    t_0 = 0
    x_0 = np.array([0, H])  # Starting position at the origin
    num_pts = 10000  # Number of points to calculate, just a wild guess

    # create variables to store our results
    t = np.zeros(num_pts)
    v = np.zeros((num_pts, 2))  # 2D velocity vector
    x = np.zeros((num_pts, 2))  # 2D position vector
    x[0] = x_0
    v[0] = v_0
    a = np.array([0, -9.8])  # Acceleration due to gravity in the y direction

    # add up the baby steps
    for i in range(num_pts-1):
        t[i+1] = t[i] + dt
        v[i+1] = v[i] + dv(a, dt) 
        x[i+1] = x[i] + dx(v[i], dt)
        if x[i+1, 1] < 0:   # Check if the ball has hit the ground
            break
    # Graph the result

    return t[:i+1], x[:i+1,:]  # Return the time and position when the ball hits the ground

def main():
    # Set initial conditions
    H = 0.92  # Height of the table in meters
    v_0 = np.array([0.5, 0])  # Initial velocity vector (5 m/s in x direction)
    dt = 0.01  # Time step in seconds

    # Call the function to roll off the table
    t, x = roll_off_table(H, v_0, dt)

    plt.plot(t, x[:,1], '.')
    plt.xlabel("Time (s)")
    plt.ylabel("Height (m)")
    plt.title("Ball rolling off the table")
    plt.axhline(0, color='red', linestyle='--')  # Ground level
    plt.show()
    # Print the results
    print(f"Time of flight: {t[-1]:.2f} seconds")
    print(f"Position when it hits the ground: {x[-1,0]}")

if __name__ == "__main__":
    main()
# This code is meant to be run as a script, not as a module.
# It will not run on its own, it needs to be run from the command line.

