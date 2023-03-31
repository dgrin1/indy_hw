# Name: Intouch Srijumnong (Indy)
# based on squarewell.py and Example 8.9 in Newman p.395

from numpy import array, arange

# Given constants
m = 9.1094e-31  # Mass of electron in kg
hbar = 1.0546e-34  # Js
a = 1e-11  # Angstrom
e = 1.6022e-19  # Electron charge in C
V0 = 50 * e  # J
x_0 = -10 ** -10  # The interval of the wavefunction
x_f = 10 ** -10
psi_0 = 0.0  # psi = 0 at both boundaries

N = 1000
h = (x_f - x_0) / N  # A fixed step ((b-a)/N)


# a)
def psi(E):  # Defining the wavefunction with the harmonic potential function
    def f(r, x):
        def V(x):
            return V0 * x ** 2 / a ** 2

        psi = r[0]
        phi = r[1]
        return array([phi, (2 * m / hbar ** 2) * (V(x) - E) * psi], float)

    r = array([psi_0, 1.0], float)  # Creating an array of the wavefunction
    wavefunction = []
    for x in arange(x_0, x_f, h):  # Calculating the wavefunction for the given potential function using rk4
        wavefunction.append(r[0])
        k1 = h * f(r, x)
        k2 = h * f(r + 0.5 * k1, x + 0.5 * h)
        k3 = h * f(r + 0.5 * k2, x + 0.5 * h)
        k4 = h * f(r + k3, x + h)
        r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return array(wavefunction, float)


def secant(E1, E2):  # Defining the main program to find the energy using the secant method
    target = e / 1000  # Target accuracy in eV
    wavefunction = psi(E1)
    psi2 = wavefunction[N - 1]
    while abs(E1 - E2) > target:  # Calculating the energies from the wavefunction with given potential function
        wavefunction = psi(E2)
        psi1, psi2 = psi2, wavefunction[N - 1]
        E1, E2 = E2, E2 - psi2 * (E2 - E1) / (psi2 - psi1)
    return E2 / e, wavefunction


# The energies of the ground state and the first two excited states of the functions
E0, psi0 = secant(0, 0.5 * e)
E1, psi1 = secant(200 * e, 400 * e)
E2, psi2 = secant(500 * e, 700 * e)
print("The energies of the ground state and the first two excited states of the harmonic oscillator are")
print("E_0 = ", E0, "eV")
print("E_1 = ", E1, "eV")
print("E_2 = ", E2, "eV")


# b)
def psi(E):  # Defining the wavefunction with the harmonic potential function
    def f(r, x):
        def V(x):
            return V0 * x ** 4 / a ** 4

        psi = r[0]
        phi = r[1]
        return array([phi, (2 * m / hbar ** 2) * (V(x) - E) * psi], float)

    r = array([psi_0, 1.0], float)  # Creating an array of the wavefunction
    wavefunction = []
    for x in arange(x_0, x_f, h):  # Calculating the wavefunction for the given potential function using rk4
        wavefunction.append(r[0])
        k1 = h * f(r, x)
        k2 = h * f(r + 0.5 * k1, x + 0.5 * h)
        k3 = h * f(r + 0.5 * k2, x + 0.5 * h)
        k4 = h * f(r + k3, x + h)
        r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return array(wavefunction, float)


def secant(E1, E2):  # Defining the main program to find the energy using the secant method
    target = e / 1000  # Target accuracy in eV
    wavefunction = psi(E1)
    psi2 = wavefunction[N - 1]
    while abs(E1 - E2) > target:  # Calculating the energies from the wavefunction with given potential function
        wavefunction = psi(E2)
        psi1, psi2 = psi2, wavefunction[N - 1]
        E1, E2 = E2, E2 - psi2 * (E2 - E1) / (psi2 - psi1)
    return E2 / e, wavefunction


# The energies of the ground state and the first two excited states of the functions
E0, psi0 = secant(0, 0.5 * e)
E1, psi1 = secant(400 * e, 600 * e)
E2, psi2 = secant(900 * e, 1100 * e)
print("The energies of the ground state and the first two excited states of the anharmonic oscillator are")
print("E_0 = ", E0, "eV")
print("E_1 = ", E1, "eV")
print("E_2 = ", E2, "eV")
