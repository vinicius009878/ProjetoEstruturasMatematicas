# adicionado agora
import numpy as np
from matplotlib import pyplot as plt
# adicionado agora
def funcao_primeiro_grau(a, b):
    print("\n\n=== Analisador de Função de Primeiro Grau ===")
    print("Forma geral: f(x) = ax + b\n")

    if a == 0:
        print("\nIsso não é uma função de primeiro grau (a deve ser diferente de 0).")
        return

    print("\n=== Resultados ===")

    raiz = -b / a
    print(f"Raiz da função (f(x)=0): x = {raiz:.2f}")


    if a > 0:
        inclinacao_reta = "A função é crescente (a > 0)."
    else:
        inclinacao_reta = "A função é decrescente (a < 0)."

    print(f"\nEquação: f(x) = {a}x + {b}")

    x = float(input("\nDigite um valor para x: "))
    fx = a * x + b
    print(f"f({x}) = {fx:.2f}")

    xv = -b / (2*a)
    print(f"O valor de x do vértice é: {xv:.2f}")
    
    # adicionado agora PARTE DO GRAFICO
    x = np.linspace(-10, 10, 100, dtype=int)
    y = a*x + b

    plt.plot(x, y, label=f"f(x)={a}x+{b}")
    plt.title("Função de 1º Grau")

    # linha dos eixos
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    # Pontos de interseção
    plt.scatter(raiz, 0, color='red', label=f"Interseção com X ({raiz:.2f}, 0)")
    plt.scatter(0, b, color='green', label=f"Interseção com Y (0, {b:.2f})")
    plt.scatter([], [], color='blue', label=f"{inclinacao_reta}")

    # Rótulos dos pontos
    plt.text(raiz, 0, f" ({raiz:.2f}, 0)", color='red', fontsize=9, ha='left', va='bottom')
    plt.text(0, b, f" (0, {b:.2f})", color='green', fontsize=9, ha='left', va='bottom')

     # === CONFIGURAÇÃO DO GRID E ESCALA ===
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xticks(np.arange(-10, 11, 1))  # marcações de -10 até 10, de 1 em 1
    plt.yticks(np.arange(-10, 11, 1))  # idem para o eixo y
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)

    plt.legend()
    plt.grid(True)
    plt.show()
    # adicionado agora