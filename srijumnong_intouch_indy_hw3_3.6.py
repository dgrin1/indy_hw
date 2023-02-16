# worked with Emma
import numpy as np
import matplotlib.pyplot as plt

r = 1
x = 0.5

for i in range(1000):  # iterate the logistic map 1,000 times in a loop
    x = r * x * (1 - x)
plt.figure(figsize=(10, 10))  # plot the figure labeled r and x and adjust the frame
plt.ylim(-0.1, 1.1)
plt.title("Feigenbaum plot")
plt.xlabel("r")
plt.ylabel("x")

while r <= 4:  # repeat the whole calculation for values of r from 1 to 4
    x_list = []  # list of x values in a loop from r = 1 to 4
    for i in range(1000):
        x = r * x * (1 - x)
        x_list.append(x)  # append list of x values to the end of the loop
    r += 0.01  # added in steps of 0.01
    r_list = []
    r_list.append(r)  # append list of r values for the plot
    plt.scatter(r_list * len(x_list), x_list, color="blue", s=0.5)

plt.show()
