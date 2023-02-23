# Name: Intouch Srijumnong (Indy)
# worked with JT

from numpy import linspace, exp
import matplotlib.pyplot as plt
from gaussxw import gaussxwab


def gaussint(function, b):  # Creating an integration function from Gaussian quadrature
    x, w = gaussxwab(N, a, b)  # Using an alternative function gaussxwab(N,a,b) in Newman p. 170 for the mapping
    s = 0.0
    for k in range(N):
        s += w[k] * function(x[k])
    return s


# a
V = 1e-6  # in m^3
rho = 6.022e28  # in m^-3
thetaD = 428  # in K
kB = 1.380649e-23  # J/K
N = 50  # sample points
a = 0


def f(x):  # Defining the function of the heat capacity of a solid
    return (9 * V * rho * kB * (T / thetaD) ** 3) * (x ** 4 * exp(x)) / (exp(x) - 1) ** 2


# b
S = []
T_int = linspace(5, 500)  # Temperature from 5 K to 500 K for 50 sample points
for T in T_int:  # Creating a loop for the temperature to be integrated
    b = thetaD / T
    S.append(gaussint(f, b))  # Using the Gaussian quadrature to integrate the function

plt.plot(T_int, S, color="red")  # Plotting the integrated interval of the temperature
plt.xlim(5, 500)  # Adjusting the frame of the graph
plt.title("The heat capacity of a solid aluminum as a function of temperature")
plt.xlabel("Temperature (K)")
plt.ylabel("The heat capacity (J/K)")
plt.show()
