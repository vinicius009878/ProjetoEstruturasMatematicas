# Importações das libs
import numpy as np
import matplotlib.pyplot as plt


def gerar_grafico_segundo_grau_didatico(a, b, c):
    print(
        "\n===================== GRÁFICO DIDÁTICO — FUNÇÃO DE 2º GRAU ====================="
    )
    print(f"Função: f(x) = {a}x² + {b}x + {c}\n")

    # 1 — Identificação dos coeficientes
    print("1️⃣  Identificando os coeficientes:")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")

    if a == 0:
        print("\n⚠ A função NÃO é de 2º grau porque a = 0.")
        return

    print("\nComo a ≠ 0 → É uma FUNÇÃO QUADRÁTICA!\n")

    # 2 — Calcular o Delta
    print("2️⃣  Calculando o discriminante (Δ):")
    print("Fórmula: Δ = b² − 4ac")
    delta = b**2 - 4 * a * c

    print(f"Δ = ({b})² − 4 * {a} * {c}")
    print(f"Δ = {delta:.2f}\n")

    # 3 — Determinando as raízes
    print("3️⃣  Encontrando as raízes:")

    raizes = []
    if delta < 0:
        print("Δ < 0 → A função NÃO possui raízes reais.")
    elif delta == 0:
        print("Δ = 0 → A função possui UMA raiz real (raiz dupla).")
        raiz = -b / (2 * a)
        print(f"Raiz: x = {raiz:.2f}")
        raizes = [raiz]
    else:
        print("Δ > 0 → A função possui DUAS raízes reais.")
        r1 = (-b + np.sqrt(delta)) / (2 * a)
        r2 = (-b - np.sqrt(delta)) / (2 * a)
        print(f"x₁ = {r1:.2f}")
        print(f"x₂ = {r2:.2f}")
        raizes = [r1, r2]

    print()

    # 4 — Vértice da parábola
    print("4️⃣  Calculando o vértice (Xv e Yv):")
    xv = -b / (2 * a)
    yv = a * xv**2 + b * xv + c
    print(f"Xv = {xv:.4f}")
    print(f"Yv = {yv:.4f}")

    if a > 0:
        print("\nA parábola é ✨ ABERTA PARA CIMA ✨ (a > 0).")
    else:
        print("\nA parábola é 🔻 ABERTA PARA BAIXO 🔻 (a < 0).")

    # 5 — Interceptação no eixo Y
    print("\n5️⃣  Intercepto no eixo Y:")
    print(f"Quando x = 0 → f(0) = {c}\n")

    # 6 — Pontos auxiliares
    print("6️⃣  Calculando dois pontos auxiliares:")
    x1, x2 = -2, 2
    p1 = a * x1**2 + b * x1 + c
    p2 = a * x2**2 + b * x2 + c
    print(f"Ponto 1: x = -2 → f(-2) = {p1:.2f}")
    print(f"Ponto 2: x = 2  → f(2) = {p2:.2f}\n")

    print("Gerando gráfico...\n")

    # 7 — Geração do Gráfico
    X = np.linspace(-10, 10, 400)
    Y = a * X**2 + b * X + c

    plt.figure(figsize=(10, 6))

    # Curva principal da função
    plt.plot(X, Y, color="black", label="Função Quadrática")

    # Vértice da parábola
    plt.scatter(xv, yv, color="purple", s=70, label=f"Vértice ({xv:.2f}, {yv:.2f})")
    plt.text(xv, yv, f" ({xv:.2f}, {yv:.2f})", color="purple")

    # Raízes com label apenas uma vez
    if len(raizes) > 0:
        plt.scatter(
            raizes, [0] * len(raizes), color="red", s=70, label="Raízes (vermelho)"
        )
        for r in raizes:
            plt.text(r, 0, f" ({r:.2f}, 0)", color="red")

    # Interceptação em Y
    plt.scatter(0, c, color="green", s=70, label=f"Intercepto em Y (0, {c})")
    plt.text(0, c, f" (0, {c})", color="green")

    # Pontos auxiliares
    plt.scatter(
        [x1, x2], [p1, p2], color="blue", s=70, label="Pontos auxiliares (azul)"
    )
    plt.text(x1, p1, f" ({x1}, {p1:.2f})", color="blue")
    plt.text(x2, p2, f" ({x2}, {p2:.2f})", color="blue")

    # Eixos
    plt.axhline(0, linewidth=0.8, color="gray")
    plt.axvline(0, linewidth=0.8, color="gray")

    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.title("Gráfico Didático — Função de 2º Grau")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()
