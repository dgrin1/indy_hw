# Name: Intouch Srijumnong (Indy)
# worked with JT

import matplotlib.pyplot as plt
import numpy as np
from numpy import arange, array

# a)

# Given constants
g = 9.8  # m/s
l = 0.1  # m
C = 2.0  # s^-2
O = 5.0  # s^-1


def f(r, t):  # Defining the equation of motion for pendulum
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g / l) * np.sin(theta) + C * np.cos(theta) * np.sin(O * t)
    return array([ftheta, fomega], float)


# Giving initial conditions for step size and limit
a = 0.0
b = 100
N = 10000
h = (b - a) / N
theta_0 = 0
tpoints = arange(a, b, h)  # Returning values for the calculation
thetapoints = []
ypoints = []

x = array([0, 0], float)  # Creating an array for rk4 calculation
for t in tpoints:  # Calculating each value in a loop using rk4
    thetapoints.append(x[0])
    ypoints.append(x[1])
    k1 = h * f(x, t)
    k2 = h * f(x + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(x + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(x + k3, t + h)
    x += (k1 + 2 * k2 + 2 * k3 + k4) / 6

# Plotting theta as a function of time
plt.plot(tpoints, thetapoints)
plt.title("The plot of an angle displacement of a driven pendulum")
plt.xlabel("Time (s)")
plt.ylabel("("r"$\theta)$")
plt.show()

# b)

# Given constants
g = 9.8  # m/s
l = 0.1  # m
C = 2.0  # s^-2
O = 9.48  # s^-1 (best omega for resonance)


def f(r, t):  # Defining the equation of motion for pendulum
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g / l) * np.sin(theta) + C * np.cos(theta) * np.sin(O * t)
    return array([ftheta, fomega], float)


# Giving initial conditions for step size and limit
a = 0.0
b = 100
N = 10000
h = (b - a) / N
theta_0 = 0
tpoints = arange(a, b, h)  # Returning values for the calculation
thetapoints = []
ypoints = []

x = array([0, 0], float)  # Creating an array for rk4 calculation
for t in tpoints:  # Calculating each value in a loop using rk4
    thetapoints.append(x[0])
    ypoints.append(x[1])
    k1 = h * f(x, t)
    k2 = h * f(x + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(x + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(x + k3, t + h)
    x += (k1 + 2 * k2 + 2 * k3 + k4) / 6

# Plotting theta as a function of time
plt.plot(tpoints, thetapoints)
plt.title("The plot of an angle displacement of a resonant driven pendulum")
plt.xlabel("Time (s)")
plt.ylabel("("r"$\theta)$")
plt.show()
