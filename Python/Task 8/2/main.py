import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 14, 1000)
delta = np.pi/2
x1 = np.sin(3*t+delta)
y1 = np.sin(2*t)
y2 = np.sin(4*t)
x2 = np.sin(5*t+delta)
y3 = np.sin(4*t)
y4 = np.sin(6*t)

plt.title('Фигуры Лисcажу')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.subplot(1, 4, 1)
plt.plot(x1, y1)
plt.subplot(1, 4, 2)
plt.plot(x1, y2, 0)
plt.subplot(1, 4, 3)
plt.plot(x2, y3)
plt.subplot(1, 4, 4)
plt.plot(x2, y4)
plt.show()
