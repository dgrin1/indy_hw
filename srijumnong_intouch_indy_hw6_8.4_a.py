# Name: Intouch Srijumnong (Indy)
# worked with JT

import matplotlib.pyplot as plt
import numpy as np
from numpy import arange, array

# Given constants
l = 0.1  # m (10 cm)
g = 9.8  # m/s


def f(r, t):  # Defining the equation of motion for pendulum (based on Newman Example 8.6)
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g / l) * np.sin(theta)
    return array([ftheta, fomega], float)


# Giving initial conditions for step size and limit
a = 0.0
b = 10.0
N = 10000
h = (b - a) / N
x = [3.124, 0.0]  # in rads for 179 degrees
tpoints = arange(a, b, h)  # Returning values for the calculation
xpoints = []

for t in tpoints:  # Calculating each value in a loop using rk4
    xpoints.append(x[0])
    k1 = h * f(x, t)
    k2 = h * f(x + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(x + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(x + k3, t + h)
    x += (k1 + 2 * k2 + 2 * k3 + k4) / 6

# Plotting theta as a function of time
plt.plot(tpoints, xpoints)
plt.title("The plot of an angle displacement of a pendulum")
plt.xlabel("Time (s)")
plt.ylabel("("r"$\theta)$")
plt.show()
