import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
 
 
fig = plt.figure()
ax = plt.axes(xlim=(-1.2, 1.2), ylim=(-1.2, 1.2))
plt.grid()
line, = ax.plot([], [], lw=2)
 
def init():
    line.set_data([], [])
    return line,
def animate(i):
    t = np.linspace(-15.71, 15.71, 1000)
    x = np.sin((i/1000)*t)
    y = np.sin(t)
    line.set_data(x, y)
    return line,
 
anim = FuncAnimation(fig, animate, init_func=init,
                               frames=1000, interval=24, blit=True)
plt.show()