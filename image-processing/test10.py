# https://okumuralab.org/~okumura/python/mandelbrot.html
import matplotlib.pyplot as plt

def mandel(c):
    z = 0
    x = [0]
    y = [0]
    for i in range(50):
        z = z ** 2 - c
        if abs(z) > 50:
            break
        x.append(z.real)
        y.append(z.imag)
    plt.clf()
    plt.axis('off')
    plt.plot(x, y, "--", dashes=[1])
    plt.axis('equal')

# mandel(0.4 + 0.4j)
# mandel(0.5 + 0.5j)
# mandel(0.1 + 0.5j)
mandel(0.45 + 0.51j)
