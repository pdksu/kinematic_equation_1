# intro to computer images
#   In a computer, images are two dimensional arrays of numbers.
#   This is a step up in complexity from the one-dimensional arrays we have seen so far.
# There will be some important computer syntax.
#
import numpy as np
import matplotlib.pyplot as plt

# defining a vector vs an array
x = np.zeros(10)  # This is a vector (1D array)
X = np.zeros((10, 10))  # This is a 2D array (matrix)

for i in range(10):
    x[i] = i  # Fill the vector with values 0 to 9
    X[i,:] = i # Fill each row of the 2D array with values 0 to 9
print("Vector x:", x)
print("2D Array X:\n", X)
# Plotting the vector
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x, marker='o', label='Vector x')
plt.title('Vector x')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid()
# Plotting the 2D array
plt.subplot(1, 2, 2)
plt.imshow(X, cmap='viridis', aspect='auto')
plt.title('2D Array X')
plt.colorbar(label='Value')
plt.xlabel('Column Index')
plt.ylabel('Row Index')
plt.tight_layout()
plt.show()

# In images it is handy to have access to the index values for x and y.

Y = np.transpose(x) # Transpose x to create a 2D array with one row
# then we can calculate the distance from the origin with the pythagorean theorem
r = np.sqrt(X**2 + Y**2)  # Calculate the distance from the origin for each point in X and Y
# Plotting the distance from the origin
plt.figure(figsize=(5, 5))
plt.imshow(r, cmap='hot', aspect='auto')
plt.title('Distance from Origin')
plt.colorbar(label='Distance')
plt.xlabel('Column Index')
plt.ylabel('Row Index')
plt.tight_layout()
plt.show()

# Your turn. i
#    * Make an image array r with the center in the middle of the image
#    * Make another image circ which is 1 where r is less than 5 and 0 otherwise
#  display circ.