# Name: Intouch Srijumnong (Indy)
# worked with JT and Emma

import numpy as np
from math import pi
from numpy.linalg import eigh
import matplotlib.pyplot as plt

# b
print("Part b")
# Given constants
em = 9.1094e-31  # in kg
hb = 6.582119514e-16  # in eV * s
e = 1.6022e-19  # in C
L = 5.0e-10  # in m
a = 10  # in eV

# Input statements
m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))


# Define the Hamiltonian function for calculation
def Hmn(m, n):
    if n == m:
        return (np.pi * hb * n) ** 2 / (2 * em * L ** 2) * e + a / 2
    elif (m + n) % 2 == 1:
        return -8 * a / (np.pi ** 2) * m * n / (m ** 2 - n ** 2) ** 2
    else:
        return 0


print("Answer: ", Hmn(m, n))

# c
print("Part c")
# Given initial condition for a 10*10 array
N = 10
H = np.zeros((N, N), float)

# Create the loop for calculating the function
for x in range(N):
    for y in range(N):
        H[x, y] = Hmn(x + 1, y + 1)  # Matrix allowance

# Finding the eigenvalues
energy = np.linalg.eigvalsh(H)
print(energy)

# part d
print("part d")
# Given initial condition for a 100*100 array
N = 100
print(energy)
# No changes in answer

# part e
print("Part e")
N = 100

# Defining Hamiltonian matrix
Hamiltonian = np.zeros((N, N), float)
for i in range(N):
    for j in range(N):
        Hamiltonian[i, j] = Hmn(i + 1, j + 1)

# Psi in eigenstates
_, psi = eigh(Hamiltonian)


# Fourier sine series of the wavefunction
# Calculating the sum eigenstates with weights (psi[m,n])
def solve_psi(n, x_list):
    wavefunction = sum([psi[n, i] * np.sin(pi * (i + 1) * x_list / L) for i in range(N)])
    return np.sqrt(2 / L) * wavefunction


# Defining wavefunctions in the three states for the graph
xs = np.linspace(0, L, N)
ground = solve_psi(0, xs)
first = solve_psi(1, xs)
second = solve_psi(2, xs)

# Plotting
plt.plot(xs, ground ** 2, label="Ground State")
plt.plot(xs, first ** 2, label="First State")
plt.plot(xs, second ** 2, label="Second State")
plt.xlabel("x (distance)")
plt.ylabel("y (probability density)")
plt.title("The Plot of Probability Density in Three States")
plt.legend()
plt.show()
