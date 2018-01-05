import matplotlib.pyplot as plt
import numpy as np

m = 10
M = 20


def f(c):
    k = 0
    u = 0

    while abs(u) <= M and k <= m:
        k += 1
        u = u ** 2 + c

    if k > m or abs(u) <= M:
        return m + 1
    else:
        return k - 1


def tracer():
    LX = np.arange(-2, 2, 4 / 401)
    LY = [f(x) for x in LX]
    plt.plot(LX, LY)


def tab(n):
    x = np.arange(-2, 0.5, 2.5 / n)
    y = np.arange(-1.1, 1.1, 2.2 / n)

    t = np.zeros((n, n))
    for a in range(n):
        for b in range(n):
            t[a, b] = f(x[a] + y[b] * 1j)
    return t


def tracerim(n):
    plt.imshow(tab(n))
