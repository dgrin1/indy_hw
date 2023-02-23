# Name: Intouch Srijumnong (Indy)
# worked with JT

import matplotlib.pyplot as plt
from numpy import pi, sqrt, linspace, cos, sin, mgrid


# a
def J(m, x):  # Defining function Jm(x)
    def f(theta):
        return cos(m * theta - x * sin(theta))

    N = 1000
    a = 0
    b = pi
    h = (b - a) / N
    s = f(a) + f(b) + 4 * f(b - h)  # Using Simpson rule for the integration calculation
    for k in range(1, N // 2):  # Float object cannot be interpreted as an integer so need to put N // 2
        s += 4 * f(a + (2 * k - 1) * h) + 2 * f(a + 2 * k * h)
    I = h / 3 * s / pi  # The Simpson equation according to Newman p. 146 - 147
    return I


x = linspace(0, 20, 1000)  # Plotting from x = 0 to x = 20 for 1,000 values
plt.plot(x, J(0, x), label="J0")
plt.plot(x, J(1, x), label="J1")
plt.plot(x, J(2, x), label="J2")
plt.xlim(0, 20)  # Adjusting the frame of the graph
plt.title("The plot of the Bessel functions of J0, J1, and J2")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# b
x, y = mgrid[-1:1:100j, -1:1:100j]  # Creating a 2d array of grid values for the density plot as complex numbers
r = sqrt(x ** 2 + y ** 2)  # r is the distance in the focal plane from the center of the diffraction pattern
wavelength = 0.5  # in m
k = 2 * pi / wavelength  # in m^-1
I = (J(1, r * k) / k / r) ** 2  # I is the intensity of the light in this diffraction pattern

# print(I)
# print(np.max(I), np.min(I))
# print(mgrid)

plt.imshow(I, origin="lower", cmap="gray", vmax=0.01, extent=(-0.5, 0.5, -0.5, 0.5))
# Adjusting the frame of the plot according to the grid values
plt.title("The density plot of the light intensity of the circular diffraction pattern")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.show()
