import math as mt
import numpy as np
from matplotlib import pyplot as plt

def equacao_segundo_grau(a, b, c):
    print("=== Analisador de Equação do Segundo Grau ===")
    print("Forma geral: f(x) = ax² + bx + c\n")

    if a == 0:
        print("\nIsso não é uma equação de segundo grau (a deve ser diferente de 0).")
        return

    print("\n=== Resultados ===")

    delta = b**2 - 4*a*c
    print(f"Δ (Delta) = {delta:.2f}")

    if delta < 0:
        print("A equação não possui raízes reais.")
        x1 = x2 = None
    elif delta == 0:
        x1 = x2 = -b / (2*a)
        print(f"Raiz única: x₁ = x₂ = {x1:.2f}")
    else:
        x1 = (-b + mt.sqrt(delta)) / (2*a)
        x2 = (-b - mt.sqrt(delta)) / (2*a)
        print(f"x₁ = {x1:.2f}")
        print(f"x₂ = {x2:.2f}")
    
    if a > 0:
        inclinacao_reta = "A função é crescente (a > 0)."
    else:
        inclinacao_reta = "A função é decrescente (a < 0)."

    x = float(input("\nDigite um valor para x: "))
    fx = (a * (x**2)) + (x * b) + c
    print(f"f({x}) = {fx:.2f}")

    xv = -b / (2*a)
    if xv is not None:  
        print(f"O valor de x do vértice é: {xv:.2f}")

    yv = -delta / (4*a)
    if yv is not None:
        print(f"O valor de y do vértice é: {yv:.2f}")

    # adicionado
    x = np.linspace(-20, 21, 200, dtype=int)
    y = a*x**2 + b*x + c

    plt.plot(x, y, label=f"f(x)={a}x²+{b}x+{c}")
    plt.title("Função de 2º Grau")

    # linha dos eixos
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    # pontos de interseção
    plt.scatter(x1, 0, color='red', label=f"Interseção com X1 ({x1:.2f}, 0)")
    plt.scatter(x2, 0, color='red', label=f"Interseção com X2 ({x2:.2f}, 0)")
    plt.scatter(0, c, color='green', label=f"Interseção com Y ({b:.2f})")
    plt.scatter([], [], color='blue', label=f"{inclinacao_reta}")
    plt.scatter(xv, yv, color='purple', label=f"X e Y do vértice ({xv}, {yv:.2f})")

    # Rótulos dos pontos
    plt.text(x1, 0, f" ({x1:.2f}, 0)", color='red', fontsize=9, ha='left', va='bottom')
    plt.text(0, x2, f" ({x2:.2f})", color='red', fontsize=9, ha='left', va='bottom')
    plt.text(0, c, f" ({c:.2f})", color='green', fontsize=9, ha='left', va='bottom')
    plt.text(0, yv, f" ({yv:.2f})", color='purple', fontsize=9, ha='left', va='bottom')
    
    # === CONFIGURAÇÃO DO GRID E ESCALA ===
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    plt.xticks(np.arange(-20, 21, 1))  # marcações de -10 até 10, de 1 em 1
    plt.yticks(np.arange(-20, 21, 1))  # idem para o eixo y
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)

    plt.legend()
    plt.grid(True)
    plt.show()
    # adicionado