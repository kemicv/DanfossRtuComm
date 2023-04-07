import time
import matplotlib.pyplot as plt
import numpy as np

# line 1 points
x1 = [10,20,30]
y1 = [20,40,10]
# plotting the line 1 points
#plt.plot(x1, y1, label = "line 1")
# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
# plotting the line 2 points
plt.plot(x1,y1, label = "line 1")
plt.plot(x1,y2,label="line 2")

plt.show()

########

#Sets a range to plot 0,30 is x-axis and 0,5 is y-axis
from matplotlib.animation import FuncAnimation
from random import randrange

fig = plt.figure(figsize=(6, 3))
x = [0]
y = [0]

ln, = plt.plot(x, y, '-')
plt.axis([0, 30, 0, 5])

def update(frame):
    x.append(x[-1] + 1)
    y.append(randrange(0, 5))

    ln.set_data(x, y)
    return ln,

animation = FuncAnimation(fig, update, interval=500)
plt.show()