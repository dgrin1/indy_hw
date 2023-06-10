# Name: Intouch Srijumnong (Indy)

from numpy import linspace, array, arange
import matplotlib.pyplot as plt

# Feigenbaum Plot

# Constants
r = 1
x = 0.5

for i in range(1000):  # iterate the logistic map 1,000 times in a loop
    x = r * x * (1 - x)
plt.figure(figsize=(10, 10))  # plot the figure labeled r and x and adjust the frame
plt.ylim(-0.1, 1.1)
plt.title("Feigenbaum plot")
plt.xlabel("r")
plt.ylabel("x")

while r <= 4:  # repeat the whole calculation for values of r from 1 to 4
    x_list = []  # list of x values in a loop from r = 1 to 4
    for i in range(1000):
        x = r * x * (1 - x)
        x_list.append(x)  # append list of x values to the end of the loop
    r += 0.01  # added in steps of 0.01
    r_list = [r]
    plt.scatter(r_list * len(x_list), x_list, color="b", s=0.5)

plt.show()

# Lorenz Strange Attractor

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

# Plotting
plt.plot(tpoints, ypoints, color="b")
plt.title("Lorenz Equations: Plot of y as a function time")
plt.xlabel("t")
plt.ylabel("y")
plt.show()

plt.plot(tpoints, xpoints, color="r")
plt.title("Lorenz Equations: Plot of x as a function time")
plt.xlabel("t")
plt.ylabel("x")
plt.show()

plt.plot(tpoints, zpoints, color="g")
plt.title("Lorenz Equations: Plot of z as a function time")
plt.xlabel("t")
plt.ylabel("z")
plt.show()


plt.plot(xpoints, zpoints, color="b")
plt.title("Lorenz Equations: Strange attractor phase in x-z plane")
plt.xlabel("x")
plt.ylabel("z")
plt.show()

plt.plot(xpoints, ypoints, color="r")
plt.title("Lorenz Equations: Strange attractor phase in x-y plane")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

plt.plot(ypoints, zpoints, color="g")
plt.title("Lorenz Equations: Strange attractor phase in y-z plane")
plt.xlabel("y")
plt.ylabel("z")
plt.show()