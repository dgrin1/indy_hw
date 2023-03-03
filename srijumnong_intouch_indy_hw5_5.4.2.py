# Name: Intouch Srijumnong (Indy)
# worked with JT

import matplotlib.pyplot as plt
from numpy import pi, cos, sin, arange, linspace


def J(m, x):  # Defining function Jm(x) from last week 5.4
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


n_list = [2, 3, 4]  # list of n = 2, 3, 4
x_list = arange(1, 20, 0.1)  # List of x as start from 1 to 20 as asked in 5.4

for y in range(len(n_list)):  # Creating a loop for the calculation of n = 2, 3, 4 for y
    print("y=", y)
    y_list = []
    m = n_list[y]
    error_list = []  # an empty list of for calculation of the error
    theta_list = linspace(0, pi)  # theta from 0 to Pi
    for x in x_list:  # Creating another loop for x
        print("x=", x)
        result = J(m, x)
        y_list.append(result)
        l_result = J(m + 1, x) + J(m - 1, x)  # Left hand side of the Bessel functions
        r_result = ((2 * m) / x) * result  # Right hand side of the Bessel Function
        error = (l_result - r_result) / result  # The fractional error between the two methods
        # error = (l_result - r_result) # The fractional error between the two methods without / J(m, x)
        error_list.append(error)
    plt.plot(x_list, error_list, label=str(m))
    plt.legend()

plt.title("The fractional error between the two methods of Bessel functions")  # Plotting the error as a function of x
plt.xlabel("x")
plt.ylabel("Error")
plt.show()