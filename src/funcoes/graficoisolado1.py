import numpy as np
import matplotlib.pyplot as plt


def gerar_grafico_primeiro_grau(a, b):
    x = np.linspace(-10, 10, 200)
    y = a * x + b

    plt.plot(x, y)
    plt.grid(True)
    plt.title(f"f(x) = {a}x + {b}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()
