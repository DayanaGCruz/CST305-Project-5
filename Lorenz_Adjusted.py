# CST-307: Principles of Modeling 
# WF1100A Dr. Citro
# Program provided by instructor and adjusted 
# Self-Organized Criticality: Project 5: Lorenz_Adjusted.py
# 11/12/2023

#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

# Define Lorenz system
def lorenz(x, y, z, r, s=10, b=2.667):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot
#--------------------
# Solve for 1000 points per r change and display 1D and 3D models
def solve(r):
	dt = 0.01 # Step size 
	num_steps = 10000

	# Need one more for the initial values
	xs = np.empty(num_steps + 1)
	ys = np.empty(num_steps + 1)
	zs = np.empty(num_steps + 1)
	
	# Set initial values 
	# Adjusted to file sizes in KB
	xs[0], ys[0], zs[0] = (5.6, 8.8, 7.4)

	# Step through "time", calculating the partial derivatives at the 	current point
	# and using them to estimate the next point
	for i in range(num_steps):
    		x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], r)
    		xs[i + 1] = xs[i] + (x_dot * dt)
    		ys[i + 1] = ys[i] + (y_dot * dt)
    		zs[i + 1] = zs[i] + (z_dot * dt)


	# Plot
	plt.figure(1)
	plt.plot(xs)
	plt.xlabel("T Axis")
	plt.ylabel("X Axis")
	plt.title("r = {}".format(r))
	plt.figure(2)
	plt.plot(ys)
	plt.xlabel("T Axis")
	plt.ylabel("Y Axis")
	plt.title("r = {}".format(r))
	plt.figure(3)
	plt.plot(zs)
	plt.xlabel("T Axis")
	plt.ylabel("Z Axis")
	plt.title("r = {}".format(r))
	fig = plt.figure(4)
	ax = fig.add_subplot(111, projection = '3d')
	ax = plt.gca()

	ax.plot(xs, ys, zs, lw=0.5)
	ax.set_xlabel("X Axis")
	ax.set_ylabel("Y Axis")
	ax.set_zlabel("Z Axis")
	ax.set_title("Lorenz Attractor: r = {}".format(r))

	plt.show()

#--------------------
# Find solution set for various r values
solve(3)
solve(15)
solve(30)