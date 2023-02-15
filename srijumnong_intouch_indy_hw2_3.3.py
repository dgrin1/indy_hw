#worked with JT
import numpy as np
import matplotlib.pyplot as plt
from pylab import show, gray
from numpy import loadtxt

data = loadtxt("C:/Users/beein/Downloads/stm.txt", float)
plt.imshow(data, origin="lower")
gray()
show()

