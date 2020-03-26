# Plotting Seirpinski Triangle with matplotlib

import matplotlib.pyplot as plt
from random import choice
# Defining Transformations for Seirpinski Triangle


def tran1(p):
    x = p[0]
    y = p[1]
    x1 = 0.5*x
    y1 = 0.5*y
    return x1, y1


def tran2(p):
    x = p[0]
    y = p[1]
    x1 = 0.5*x + 0.5
    y1 = 0.5*y + 0.5
    return x1, y1


def tran3(p):
    x = p[0]
    y = p[1]
    x1 = 0.5*x + 1
    y1 = 0.5*y
    return x1, y1


tranfm = [tran1, tran3, tran2]

x_val = [0]
y_val = [0]
a, b = 0, 0

for i in range(10000):  # range(x); bigger the x better the triangle
    trans = choice(tranfm)
    a, b = trans((a, b))
    x_val.append(a)
    y_val.append(b)
# Plotting Seirpinski Triangle
plt.plot(x_val, y_val, 'o')
