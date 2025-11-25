# Imports de bibliotecas
import numpy as np
import matplotlib.pyplot as plt


# Função para gerar o gráfico da função de 2º grau
def gerar_grafico_segundo_grau(a, b, c):
    x = np.linspace(-10, 10, 300)
    y = a * x**2 + b * x + c

    # Cálculo do vértice
    xv = -b / (2 * a)
    yv = a * xv**2 + b * xv + c

    # Cálculo das Raízes
    delta = b**2 - 4 * a * c
    raizes = []
    if delta > 0:
        r1 = (-b + np.sqrt(delta)) / (2 * a)
        r2 = (-b - np.sqrt(delta)) / (2 * a)
        raizes = [r1, r2]
    elif delta == 0:
        r = -b / (2 * a)
        raizes = [r]

    # Interceptação no eixo Y
    intercepto_y = c

    # Pontos auxiliares
    x1, x2 = -2, 2
    p1 = a * x1**2 + b * x1 + c
    p2 = a * x2**2 + b * x2 + c

    # Geração do gráfico
    plt.plot(x, y, label=f"f(x) = {a}x² + {b}x + {c}", color="black")

    # Vértice Ponto
    plt.scatter(xv, yv, color="purple", s=70, label=f"Vértice ({xv:.2f}, {yv:.2f})")
    plt.text(xv, yv, f" ({xv:.2f}, {yv:.2f})", color="purple")

    # Raízes Pontos
    for r in raizes:
        plt.scatter(r, 0, color="red", s=60, label=f"Raiz ({r:.2f}, 0)")
        plt.text(r, 0, f" ({r:.2f}, 0)", color="red")

    # Interceptação em Y Ponto
    plt.scatter(
        0, intercepto_y, color="green", s=60, label=f"Intercepto (0, {intercepto_y})"
    )
    plt.text(0, intercepto_y, f" (0, {intercepto_y})", color="green")

    # Pontos auxiliares
    plt.scatter([x1, x2], [p1, p2], color="blue", s=60, label="Pontos auxiliares")
    plt.text(x1, p1, f" ({x1}, {p1:.2f})", color="blue")
    plt.text(x2, p2, f" ({x2}, {p2:.2f})", color="blue")

    # Eixos X e Y
    plt.axhline(0, linewidth=0.8, color="gray")
    plt.axvline(0, linewidth=0.8, color="gray")

    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.title(f"Gráfico da Função de 2º Grau")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()
