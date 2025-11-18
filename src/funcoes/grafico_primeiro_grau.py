import numpy as np
import matplotlib.pyplot as plt


def gerar_grafico_primeiro_grau(a, b):
    x = np.linspace(-10, 10, 200)
    y = a * x + b

    plt.plot(x, y, label=f"f(x) = {a}x + {b}")

    # ==========================
    #    INTERCEPTO EM Y
    # ==========================
    y_intercept = b
    plt.scatter(
        0, y_intercept, color="green", label=f"Intercepto em Y (0, {y_intercept})"
    )
    plt.text(0, y_intercept, f" (0, {y_intercept:.2f})", color="green", fontsize=9)

    # ==========================
    #    RAIZ (SE EXISTIR)
    # ==========================
    if a != 0:
        raiz = -b / a
        plt.scatter(raiz, 0, color="red", label=f"Raiz ({raiz:.2f}, 0)")
        plt.text(raiz, 0, f" ({raiz:.2f}, 0)", color="red", fontsize=9)

    # ==========================
    #   2 PONTOS ADICIONAIS
    # ==========================
    x1, x2 = -1, 1
    p1 = a * x1 + b
    p2 = a * x2 + b

    plt.scatter([x1, x2], [p1, p2], color="blue", label="Pontos notáveis")
    plt.text(x1, p1, f" ({x1}, {p1:.2f})", color="blue", fontsize=9)
    plt.text(x2, p2, f" ({x2}, {p2:.2f})", color="blue", fontsize=9)

    # ==========================
    #  CONFIGURAÇÕES DO GRÁFICO
    # ==========================
    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)

    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Gráfico da Função de 1º Grau (com pontos marcados)")
    plt.legend()
    plt.show()
