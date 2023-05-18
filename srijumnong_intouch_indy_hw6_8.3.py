# Name: Intouch Srijumnong (Indy)
# worked with JT

import numpy as np
from numpy import array, arange
import matplotlib.pyplot as plt

# a

# Given constants
sigma = 10
R = 28  # for r avoiding introducing errors due to parameter names
B = 8 / 3  # for b


def f(r, t):  # Defining Lorenz equations for x, y, z
    x = r[0]
    y = r[1]
    z = r[2]
    fx = sigma * (y - x)
    fy = R * x - y - x * z
    fz = x * y - B * z
    return array([fx, fy, fz], float)


# Giving initial conditions for step size and limit
a = 0
b = 50
N = 10000
h = (b - a) / N

tpoints = arange(a, b, h)  # Returning values for the calculation
xpoints = []
ypoints = []
zpoints = []

# Creating an array for rk4 calculation
r = array([0, 1, 0], float)  # Given x, y, z = 0, 1, 0 as initial condition
for t in tpoints:  # Calculating each value in a loop using rk4
    xpoints.append(r[0])
    ypoints.append(r[1])
    zpoints.append(r[2])
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4) / 6

# Plotting
plt.plot(tpoints, ypoints)
plt.title("Lorenz Equations: Plot of y as a function time")
plt.xlabel("t")
plt.ylabel("y")
plt.show()

# b

plt.plot(xpoints, zpoints)
plt.title("Lorenz Equations: Strange attractor")
plt.xlabel("x")
plt.ylabel("z")
plt.show()
