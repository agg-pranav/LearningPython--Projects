# Plotting Random Walk using matplotlib
import matplotlib.pyplot as plt
from random import choice

# Random Walk Values
y_val = list()

# Starting Random Walk from Y = 15
init_val = 15
y_val.append(init_val)

# Random Walk Values
counnter = 0
for i in range(1, 1000):
    x = [1, -1]
    c = choice(x)
    y_val.append(y_val[counnter] + c)
    counnter = counnter + 1

# Random Walk Plot
plt.plot(y_val)
plt.title("Random Walk")
plt.xlabel("No of steps")
plt.ylabel("Direction from Origin")
