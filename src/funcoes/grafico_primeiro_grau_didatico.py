# Importações necessárias das bibliotecas
import numpy as np
import matplotlib.pyplot as plt


def esperar(mensagem="Pressione Enter para continuar..."):
    try:
        input(mensagem)
    except (KeyboardInterrupt, EOFError):
        print("\n❌ Interrompido pelo usuário.")
        raise SystemExit


# Função para gerar o gráfico didático da função de 1º grau
def gerar_grafico_primeiro_grau_didatico(a, b):
    print("\n==============================================")
    print(" ⚙️  GERADOR DIDÁTICO DO GRÁFICO DE 1º GRAU ⚙️ ")
    print("==============================================")
    print("🔶 A função de 1º grau tem o formato:")
    print("🔸 f(x) = ax + b\n")

    print(f"💠 Coeficiente angular (a): {a}")
    print(f"💠 Coeficiente linear  (b): {b}\n")

    print("➡️  O coeficiente 'a' indica a inclinação da reta:")
    if a > 0:
        print("💠 A reta é CRESCENTE (sobe da esquerda para a direita).")
    elif a < 0:
        print("💠 A reta é DECRESCENTE (desce da esquerda para a direita).")
    else:
        print("💠 A reta é HORIZONTAL (função constante).")

    print("\n➡️  O coeficiente 'b' indica o ponto onde a reta toca o eixo Y.")
    print(f"💠 Intercepto em Y = {b}\n")

    esperar()

    # ------------------------------------------------------------
    # INTERCEPTO EM Y
    # ------------------------------------------------------------
    print("=== Passo 1️⃣ : Intercepto no eixo Y ===")
    y_intercept = b
    print(f"💠 f(0) = {b}")
    print(f"❇️  Intercepto: (0, {y_intercept})\n")

    esperar()

    # ------------------------------------------------------------
    # RAIZ DA FUNÇÃO
    # ------------------------------------------------------------
    print("=== Passo 2️⃣ : Raiz da função ===")
    if a == 0:
        print("‼️  Como a = 0, a função é constante e não possui raiz (exceto se b = 0).")
        raiz = None
    else:
        raiz = -b / a
        print(f"💠 0 = {a}x + {b}")
        print(f"❇️  Raiz encontrada: ({raiz:.2f}, 0)\n")

    esperar()

    # ------------------------------------------------------------
    # PONTOS AUXILIARES
    # ------------------------------------------------------------
    print("=== Passo 3️⃣ : Pontos auxiliares ===")
    x1, x2 = -1, 1
    p1, p2 = a * x1 + b, a * x2 + b
    print(f"💠 f(-1) = {p1}")
    print(f"💠 f(1)  = {p2}\n")

    esperar()

    # ------------------------------------------------------------
    # GRÁFICO
    # ------------------------------------------------------------
    print("=== Passo 4️⃣ : Gerar o gráfico ===")
    print("📈 O gráfico mostrará:")
    print("💠 A reta")
    print("💠 O intercepto em Y")
    print("💠 A raiz (se existir)")
    print("💠 Pontos auxiliares (-1 e 1)\n")

    esperar()

    # Construção do gráfico
    x = np.linspace(-10, 10, 200)
    y = a * x + b

    plt.plot(x, y, label=f"f(x) = {a}x + {b}", color="black")

    # Intercepto em Y
    plt.scatter(0, y_intercept, color="green", label=f"Intercepto (0, {y_intercept})")
    plt.text(0, y_intercept, f" (0, {y_intercept:.2f})", color="green")

    # Raiz
    if raiz is not None:
        plt.scatter(raiz, 0, color="red", label=f"Raiz ({raiz:.2f}, 0)")
        plt.text(raiz, 0, f" ({raiz:.2f}, 0)", color="red")

    # Pontos auxiliares
    plt.scatter([x1, x2], [p1, p2], color="blue", label="Pontos auxiliares")
    plt.text(x1, p1, f" ({x1}, {p1:.2f})", color="blue")
    plt.text(x2, p2, f" ({x2}, {p2:.2f})", color="blue")

    # Eixos
    plt.axhline(0, color="gray", linewidth=0.8)
    plt.axvline(0, color="gray", linewidth=0.8)

    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.title("Função de 1º Grau — Gráfico Didático")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()
