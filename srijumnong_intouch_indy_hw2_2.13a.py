import numpy as np


# According to the factorial funtion
# def factorial(n):
# if n == 1:
# return 1
# else:
# return n*factorial(n-1)

# Approach the problem in same format above
def C(n):
    if n == 0:
        return 1
    else:
        return (4 * n - 2) / (n + 1) * C(n - 1)


print(C(100))
