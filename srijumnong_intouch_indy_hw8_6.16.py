# Name: Intouch Srijumnong (Indy)
# worked with JT

# Constant
G = 6.674e-11  # m^3 * kg^-1 * s^-2
M = 5.974e24  # kg
m = 7.348e22  # kg
R = 3.844e8  # m
w = 2.662e-6  # s^-1


# a
# Define Newton's universal law of gravitation as given
def G_law(r):
    return (G * M / r ** 2) - (G * m / (R - r) ** 2) - (w ** 2 * r)


# b
# Using secant method to solve for distance r
def secant():
    r1 = 3.0e4  # Starting values for secant method
    r2 = 3.0e6
    for x in range(20):
        r = r2 - G_law(r2) * (r2 - r1) / (G_law(r2) - G_law(r1))
        r1 = r2
        r2 = r
    return (r)


distance = secant()
print("L1 = ", distance, "meters away from Earth")
