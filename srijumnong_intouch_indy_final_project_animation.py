# Name: Intouch Srijumnong (Indy)

import matplotlib.pyplot as plt
from numpy import array, arange, linspace
from matplotlib import animation, rc, rcParams

# Animating strange attractor in 3D

# Constants
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

# Returning values for the calculation
tpoints = arange(a, b, h)
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

# Animating using matplotlib

# Defining variable functions for the animation
fig = plt.figure()
ax = plt.subplot(projection="3d")

# Setting and labeling axes
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_zlim(0, 50)
ax.grid()
ax.set_xlabel("x(t)")
ax.set_ylabel("y(t)")
ax.set_zlabel("z(t)")
ax.set_title("Lorenz Equations: Strange attractor animation")
line, = ax.plot3D([], [], [], "b")
point, = ax.plot3D([], [], [], ".k")


def drawframe(n):  # Defining animating function in 3D for Lorenz equations
    x = xpoints[n]
    y = ypoints[n]
    z = zpoints[n]
    line.set_data_3d(xpoints[0:n], ypoints[0:n], zpoints[0:n])
    point.set_data_3d(x, y, z)
    angle = (360 / 10000) * n + 45
    ax.view_init(30, angle)
    return line, point


# Setting animation parameters
animate = animation.FuncAnimation(fig, drawframe, frames=10000, interval=1, blit=True)
rcParams["animation.embed_limit"] = 2 ** 128
rc("animation", html="html5")

animate
plt.show()