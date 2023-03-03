# Name: Intouch Srijumnong (Indy)
# worked with JT and Ben
from math import pi, factorial
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
from gaussxw import gaussxwab


# Importing Gaussian quadrature integration from the previous homework
def gaussint(function, b):  # Creating an integration function from Gaussian quadrature
    x, w = gaussxwab(N, a, b)  # Using an alternative function gaussxwab(N,a,b) in Newman p. 170 for the mapping
    s = 0.0
    for k in range(N):
        s += w[k] * function(x[k])
    return s


def H(n, x):  # Defining the Hermite polynomial given in the problem
    if n == 0:
        return 1
    elif n == 1:
        return 2 * x
    else:
        return 2 * x * H(n - 1, x) - 2 * (n - 1) * H(n - 2, x)


def wave(n, x):  # Defining the wavefunction of the one-dimensional quantum harmonic oscillator given in the problem
    return np.exp(-x ** 2 / 2) * H(n, x) / np.sqrt(2 ** n * factorial(n) * np.sqrt(pi))


# Part a
xmin, xmax, dx = -4, +4, 0.01  # Defining x limit from -4 to 4
x = np.arange(xmin, xmax + dx, dx)  # Creating an array of the range of x

for n in range(0, 4):  # Looping the rang of n for plotting
    psi = wave(n, x)
    plt.plot(x, psi, label=f"n = {n}")  # Labeling n = 0, 1, 2, 3

plt.xlim(xmin, xmax)  # Plotting the graph for n = 0, 1, 2, 3
plt.title("The harmonic oscillator wavefunctions for n = 0, 1, 2, and 3")
plt.xlabel("x")
plt.ylabel("$\psi_n(x)$")
plt.legend()
plt.show()

# Part b
n = 30  # Given n = 30
xmin, xmax, dx = -10, +10, 0.01  # Defining x limit from -10 to 10
x = np.arange(xmin, xmax + dx, dx)  # Creating an array of the range of x
psi = wave(n, x)

plt.plot(x, psi)  # Plotting the graph for n = 30
plt.xlim(xmin, xmax)
plt.xlabel("x")
plt.ylabel("$\psi_{30}(x)$")
plt.title("The harmonic oscillator wavefunctions for n = 30")
plt.show()

# Part c
N = 100  # Given N = 100 points
n = 5  # Given n = 5
a = -1  # Giving appropriate a and b for calculating the positions and weights in gaussint()
b = 1


def f(z):  # Defining the root-mean-square position of the quantum uncertainty given in the problem
    coeff = ((z / (1 - z ** 2)) ** 2) * (1 + z ** 2) / ((1 - z ** 2) ** 2)  # Coefficient og the term
    wf = wave(n, (z / (1 - z ** 2)))  # The wave function in the term
    return coeff * np.abs(wf) ** 2


val = gaussint(f, b)  # Evaluating the integral using Gaussian quadrature on 100 points
print("The uncertainty for n = 5 is", np.sqrt(val))  # Printing the root-mean-square position of the particle
