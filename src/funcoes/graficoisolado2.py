import numpy as np
import matplotlib.pyplot as plt


def gerar_grafico_segundo_grau(a, b, c):
    x = np.linspace(-10, 10, 300)
    y = a * x**2 + b * x + c

    plt.plot(x, y)
    plt.grid(True)
    plt.title(f"f(x) = {a}x² + {b}x + {c}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()
