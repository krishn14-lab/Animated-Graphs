import math
import numpy as np
import matplotlib.pyplot as plt

def sin_taylor():
    n = 0
    y = 0
    while True:
        x = yield
        y += ((-1)**n)*(x**(2*n + 1))/math.factorial(2*n + 1)

        n += 1
        yield y

sin_x = sin_taylor()

x_val = np.linspace(-50, 50, 500)   

for i in range(1,51):
    sin_x.send(None)
    y = sin_x.send(x_val)

    plt.style.use('dark_background')

    plt.plot(x_val, np.sin(x_val), color = 'cyan')
    plt.plot(x_val, y, color = 'orange')

    plt.ylim(-10, 10)
    plt.axhline(0, color = 'black', linewidth = 1.0)
    plt.savefig(f"temp_img/img-{i}", dpi = 300)

    plt.cla()
