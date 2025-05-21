# Kinematic Equation #2
#  this code is meant to be appended to ke1.py, it will not run on its own
## Now let's add acceleration!

# Remember how we moved through the kinematic equations.
# First we did KE1 with $a=0$.
# Then we added acceleration and wrote a very similar looking equation for KE2, $dv = a\\ dt$,
# which when added up over some long time is just KE2 $\\Delta v = a \\Delta t$,
# but in our new world of adding things up just a little baby piece at a time it looks like this:"
def dv(a,dt):
    return a*dt

# set initial conditions
t_0 = 0
x_0 = 0
t_f = 5     # seconds
dt  = 0.05  # seconds.     ___ TRY CHANGING THIS YOURSELF ____
v_0 = 25    # meters / second
a   = -9.8  # meters / second^2
num_pts = int((t_f - t_0) / dt )  # int() truncates floating point numbers

# create variables to store our results
t = np.zeros(num_pts)
v = np.zeros(num_pts)
x = np.zeros(num_pts)
x[0] = x_0
v[0] = v_0

# add up the baby steps
for i in range(num_pts-1):
    t[i+1] = t[i] + dt
    v[i+1] = v[i] + dv(a, dt)
    x[i+1] = x[i] + dx(v[i], dt)  # NOTICE that (1) you still have access to dx() from earlier
                                  # and (2) now v changes eery step

# or do it the old way, using KE#3
x_theory = x_0 + v_0 * t + (1./2)*a*(t**2)
# graph the result
plt.plot(t,x,'.')
plt.plot(t, x_theory,'r-')
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")
plt.title("Kinematic equation #3")
print(f"This graph is generated from lists with {len(x)} points.\\nThe variable num_pts = {num_pts}")