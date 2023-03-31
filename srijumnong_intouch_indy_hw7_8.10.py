# Name: Intouch Srijumnong (Indy)
# worked with JT

from numpy import array, arange, sqrt, power
import matplotlib.pyplot as plt

# Giving initial condition
m_sun = 1.989e30  # kg
G = 66377.002  # in m^3/ kg*yr^2
x_0 = 4e12  # m
y_0 = 0
v_x = 0
v_y = 15778476000  # m/yr (500 m/s)


# a)

def f(r, t):  # Defining the equation given for the comet by creating arrays for variable sets
    # turning the second-order equation into four first-order equations
    x = r[0]
    vx = r[1]
    y = r[2]
    vy = r[3]
    d = sqrt(x ** 2 + y ** 2)  # d for radius distance in m
    return array([vx, - G * m_sun * x / d ** 3, vy, - G * m_sun * y / d ** 3], float)  #


# b) Using the fourth order Runge-Kutta with a fixed step size

N = 500000  # Large number of N points is needed for the accuracy of the trajectory
t_f = 165  # yr (using the orbital period of Neptune)
t_0 = 0
h = (t_f - t_0) / N  # A fixed step ((b-a)/N)
tpoints = arange(t_0, t_f, h)
xpoints = []
ypoints = []
x = array([x_0, v_x, y_0, v_y], float)
for t in tpoints:  # Solving the function with rk4 for given condition
    xpoints.append(x[0])
    ypoints.append(x[2])
    k1 = h * f(x, t)
    k2 = h * f(x + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(x + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(x + k3, t + h)
    x += (k1 + 2 * k2 + 2 * k3 + k4) / 6

# Plotting the trajectory
plt.plot(array(xpoints), array(ypoints))
plt.title("The plot of the trajectory of the comet")
plt.xlabel("x (km)")
plt.ylabel("y (km)")
plt.show()

# c) With an adaptive step size
delta = 1000  # Given target accuracy in m/yr


def step(x, t, h):
    def rk4_step(x, t, h):
        # x = current positions and velocities
        # t = current time
        # h = step size
        k1 = h * f(x, t)
        k2 = h * f(x + 0.5 * k1, t + 0.5 * h)
        k3 = h * f(x + 0.5 * k2, t + 0.5 * h)
        k4 = h * f(x + k3, t + h)
        return (k1 + 2 * k2 + 2 * k3 + k4) / 6  # the change of positions and velocities for total t+h

    # Using an adaptive step in rk4_step for h in 2 steps
    step_h1 = rk4_step(x, t, h)
    step_h2 = rk4_step(x + step_h1, t + h, h)

    # Using an adaptive step in rk4_step for 2h in 1 step
    step_h1_h2 = step_h1 + step_h2
    step_2h = rk4_step(x, t, 2 * h)

    # Calculation error estimation for step sizes
    delta_x1 = step_h1_h2[0]
    delta_x2 = step_2h[0]
    delta_y1 = step_h1_h2[2]
    delta_y2 = step_2h[2]
    error = sqrt((delta_x1 - delta_x2) ** 2 + (delta_y1 - delta_y2) ** 2) / 30
    rho = h * delta / error
    factor = power(rho, 1 / 4)  # Defining factor for the multiplication of step size

    # Creating the condition for an adapted step size for given target accuracy
    if rho >= 1:
        t = t + 2 * h  # adapted t for adapted
        if factor > 2:  # limiting the step size
            h *= 2
        else:
            h *= factor
        return step_h1_h2, h, t
    else:  # If fail to statisfy given target accuracy, recalculate with smaller step size
        return step(r, t, factor * h)


h = (t_f - t_0) / 250000  # Giving initial step size
tpoints = []
xpoints2 = []
ypoints2 = []
r = array([x_0, v_x, y_0, v_y], float)  # Giving initial conditions
t = t_0

# Plotting the variables
while t < t_f:
    tpoints.append(t)
    xpoints2.append(r[0])
    ypoints2.append(r[2])
    delta_r, h, t = step(r, t, h)
    r += delta_r

plt.plot(array(xpoints2), array(ypoints2))
plt.title("The plot of the trajectory of the comet with the target accuracy of 1 km/yr ")
plt.xlabel("x (km)")
plt.ylabel("y (km)")
plt.show()

# d)
# Plotting with dots showing the position of the comet at each rk4 step around a single orbit
plt.plot(array(xpoints), array(ypoints))
plt.plot(array(xpoints2)[::20], array(ypoints2[::20]), "ro")
plt.title("The plot of the trajectory of the comet with position dots around an orbit")
plt.xlabel("x (km)")
plt.ylabel("y (km)")
plt.show()

