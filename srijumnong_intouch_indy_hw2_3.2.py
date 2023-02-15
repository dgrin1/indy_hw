import numpy as np
import matplotlib.pyplot as plt

# a)
theta = np.linspace(0, 2*np.pi, 1000) #1000 plot values between 0 and 2pi
x = 2*np.cos(theta) + np.cos(2*theta)
y = 2*np.sin(theta) - np.sin(2*theta)
plt.plot(x, y)
plt.title("Deltoid curve")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# b)
theta = np.linspace(0, 10*np.pi, 1000) #1000 plot values between 0 and 10pi
r = theta**2
x = r*np.cos(theta)
y = r*np.sin(theta)
plt.plot(x, y)
plt.title("Galilean spiral")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


# c)
theta = np.linspace(0, 24*np.pi, 10000) #10000 instead of 1000 plot values between 0 and 24pi for a more accurate plot
r = np.exp(np.cos(theta)) - 2*np.cos(4*theta) + np.sin(theta/12)**5
x = r*np.cos(theta)
y = r*np.sin(theta)
plt.plot(x, y)
plt.title("Fey’s function")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
