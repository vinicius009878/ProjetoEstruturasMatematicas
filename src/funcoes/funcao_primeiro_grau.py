import numpy as np
from matplotlib import pyplot as plt


def esperar(mensagem="Pressione Enter para continuar..."):
    try:
        input(mensagem)
    except (KeyboardInterrupt, EOFError):
        print("\nInterrompido pelo usuário.")
        raise SystemExit


def funcao_primeiro_grau(a, b):
    print("\n=== Analisador Didático da Função de 1º Grau ===")
    print("Forma geral: f(x) = ax + b\n")

    if a == 0:
        print("⚠ Isso não é uma função de primeiro grau, pois a = 0.")
        return

    # -------------------------
    # PASSO 1
    # -------------------------
    print("=== Passo 1: Identificar os coeficientes ===")
    print(f"a = {a}")
    print(f"b = {b}\n")
    esperar()

    # -------------------------
    # RAIZ DA FUNÇÃO (PASSO 2)
    # -------------------------
    print("=== Passo 2: Calcular a raiz da função ===")
    print("Usamos a fórmula:  x = -b / a\n")
    print(f"Substituindo os valores:")
    print(f"x = -({b}) / {a}")

    raiz = -b / a
    print(f"x = {raiz:.2f}  →  Esta é a raiz da função.\n")
    esperar()

    # -------------------------
    # CRESCENTE OU DECRESCENTE (PASSO 3)
    # -------------------------
    print("=== Passo 3: Analisar o comportamento da função ===")

    if a > 0:
        print("Como a > 0, a função é CRESCENTE.\n")
        comportamento = "Função crescente (a > 0)"
    else:
        print("Como a < 0, a função é DECRESCENTE.\n")
        comportamento = "Função decrescente (a < 0)"
    esperar()

    # -------------------------
    # CALCULAR f(x) (PASSO 4)
    # -------------------------
    print("=== Passo 4: Calcular f(x) para um valor escolhido ===")
    esperar("Quando estiver pronto para inserir o valor de x, pressione Enter...")

    while True:
        try:
            x_input = float(input("Digite um valor para x: "))
            break
        except ValueError:
            print("Entrada inválida. Digite um número (por exemplo: 2 ou -3.5).")

    print("\nUsamos a fórmula f(x) = ax + b")
    print(f"Substituindo: f({x_input}) = {a} * {x_input} + {b}")

    fx = a * x_input + b
    print(f"Resultado: f({x_input}) = {fx:.2f}\n")
    esperar()

    # -------------------------
    # GRÁFICO (PASSO 5)
    # -------------------------
    print("=== Passo 5: Gerar o gráfico ===")
    print("O gráfico mostrará:")
    print("• A reta da função")
    print("• O ponto onde ela corta o eixo X (raiz)")
    print("• O ponto onde ela corta o eixo Y (b)\n")
    esperar()

    x = np.linspace(-10, 10, 100)
    y = a * x + b

    plt.plot(x, y, label=f"f(x) = {a}x + {b}")

    plt.title("Função de 1º Grau (Gráfico Didático)")

    # Eixos
    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)

    # Pontos importantes
    plt.scatter(raiz, 0, color="red", label=f"Raiz ({raiz:.2f}, 0)")
    plt.scatter(0, b, color="green", label=f"Intercepto em Y (0, {b:.2f})")

    # Labels dos pontos
    plt.text(raiz, 0, f"  ({raiz:.2f}, 0)", color="red", fontsize=9)
    plt.text(0, b, f"  (0, {b:.2f})", color="green", fontsize=9)

    # Descrição do comportamento
    plt.scatter([], [], color="blue", label=comportamento)

    # Configurações do gráfico
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.legend()

    plt.show()
