import matplotlib.pyplot as plt
from numpy import loadtxt
import numpy as np

# a
data = loadtxt("C:/Users/beein/Downloads/millikan.txt", float)
# print(data)
x = data[:, 0]
y = data[:, 1]  # Arrays of x and y
plt.plot(x, y, "o", label="Data")  # Plot with one dot for each point
# The problem asks to give the x and y coordinates, so I label the axis as x and y
# not as frequency (Hz) and kinetic energy (J) for the actual experiment
plt.title("Millikan.txt data")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# b
N = len(x)  # Return x for N value

Ex = np.sum(x) / N
Ey = np.sum(y) / N
Exx = np.sum(x ** 2) / N
Exy = np.sum(x * y) / N
m = (Exy - Ex * Ey) / (Exx - Ex ** 2)
c = (Exx * Ey - Ex * Exy) / (Exx - Ex ** 2)

print("The slope m of the best-fit line is", m)
print("The intercept c of the best-fit line is", c)


# c
def f(x):
    return m * x + c


yfit = f(x)
plt.plot(x, y, "o", label="Data")  # Plotting the data
plt.plot(x, yfit, label="Fit line")  # Plotting the fit line
plt.title("Millikan.txt data and fit line")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# d
e = 1.602E-19
h = m * e
phi = -c
print("The experimental value for Planck’s constant h is", h, "Js")
print("The work function phi is", -c, "V")

# Experimental photoelectric effect plot
plt.plot(x, y, "o", label="Data")  # Plotting the data
plt.plot(x, yfit, label="Fit line")  # Plotting the fit line
plt.title("Photoelectric effect plot")
plt.xlabel("Frequency of the incident light (Hz)")
plt.ylabel("The maximum kinetic energy of the emitted electrons (J)")
plt.legend()
plt.show()
