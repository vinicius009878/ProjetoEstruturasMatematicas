import math as mt
import numpy as np
from matplotlib import pyplot as plt


def esperar(mensagem="Pressione Enter para continuar..."):
    try:
        input(mensagem)
    except (KeyboardInterrupt, EOFError):
        print("\n❌ Interrompido pelo usuário.")
        raise SystemExit


def equacao_segundo_grau(a, b, c):
    print("\n=== 📝 Analisador Didático da Função de 2º Grau 📝 ===")
    print("🔶 Forma geral: f(x) = ax² + bx + c\n")

    if a == 0:
        print("⚠️ Isso não é uma função de segundo grau, pois a = 0.")
        return

    # -------------------------
    # PASSO 1
    # -------------------------
    print("=== Passo 1️⃣ : Identificar os coeficientes ===")
    print(f"💠 a = {a}")
    print(f"💠 b = {b}")
    print(f"💠 c = {c}\n")
    esperar()

    # -------------------------
    # DELTA (PASSO 2)
    # -------------------------
    print("=== Passo 2️⃣ : Calcular o discriminante (Delta) ===")
    print("🔶 Usamos a fórmula:  Δ = b² - 4ac\n")

    print("🔄️ Substituindo:")
    print(f"💠 Δ = ({b})² - 4 * {a} * {c}")
    delta = b**2 - 4 * a * c
    print(f"❇️  Δ = {delta:.2f}\n")
    esperar()

    # -------------------------
    # RAÍZES (PASSO 3)
    # -------------------------
    print("=== Passo 3️⃣ : Encontrar as raízes ===")

    if delta < 0:
        print("‼️  Como Δ < 0, a equação NÃO possui raízes reais.\n")
        x1 = x2 = None

    elif delta == 0:
        print("‼️  Como Δ = 0, a equação possui apenas uma raiz real:\n")

        print("🔶 Fórmula: x = -b / (2a)")
        print(f"🔄️ Substituindo: x = -({b}) / (2 * {a})")

        x1 = x2 = -b / (2 * a)
        print(f"❇️  Raiz única: x = {x1:.2f}\n")

    else:
        print("‼️  Como Δ > 0, a equação possui duas raízes reais distintas:\n")

        print("🔶 Fórmula geral das raízes:")
        print("🔸 x₁ = (-b + √Δ) / (2a)")
        print("🔸 x₂ = (-b - √Δ) / (2a)\n")

        print("🔄️ Substituindo:\n")
        print(f"💠 x₁ = (-{b} + √{delta:.2f}) / (2 * {a})")
        print(f"💠 x₂ = (-{b} - √{delta:.2f}) / (2 * {a})")

        x1 = (-b + mt.sqrt(delta)) / (2 * a)
        x2 = (-b - mt.sqrt(delta)) / (2 * a)

        print(f"\n❇️  x₁ = {x1:.2f}")
        print(f"❇️  x₂ = {x2:.2f}\n")

    esperar()

    # -------------------------
    # VÉRTICE (PASSO 4)
    # -------------------------
    print("=== Passo 4️⃣ : Calcular o vértice (Xv e Yv) ===")

    print("🔶 Usamos:")
    print("🔸 Xv = -b / (2a)")
    print("🔸 Yv = -Δ / (4a)\n")

    print("🔄️ Substituindo:")
    print(f"💠 Xv = -({b}) / (2 * {a})")
    xv = -b / (2 * a)
    print(f"❇️  Xv = {xv:.2f}")

    print(f"💠 Yv = -({delta:.2f}) / (4 * {a})")
    yv = -delta / (4 * a)
    print(f"❇️  Yv = {yv:.2f}\n")

    esperar()

    # -------------------------
    # CONCAVIDADE (PASSO 5)
    # -------------------------
    print("=== Passo 5️⃣ : Analisar a concavidade ===")

    if a > 0:
        abertura = "‼️  A parábola é voltada PARA CIMA (a > 0)."
    else:
        abertura = "‼️  A parábola é voltada PARA BAIXO (a < 0)."

    print(abertura + "\n")
    esperar()

    # -------------------------
    # CALCULAR f(x) (PASSO 6)
    # -------------------------
    print("=== Passo 6️⃣: Calcular f(x) para um valor escolhido ===")
    esperar("🧑‍💻 Pressione Enter para inserir um valor de x...")

    while True:
        try:
            x_input = float(input("✍️  Digite um valor para x: "))
            break
        except ValueError:
            print("❌ Entrada inválida. Digite um número válido.")

    print("\n🔶 Usamos: f(x) = ax² + bx + c")
    print(f"🔄️ Substituindo: f({x_input}) = {a} * ({x_input}²) + {b} * {x_input} + {c}")

    fx = a * (x_input**2) + b * x_input + c
    print(f"❇️  Resultado: f({x_input}) = {fx:.2f}\n")
    esperar()

    # -------------------------
    # GRÁFICO (PASSO 7)
    # -------------------------
    print("=== Passo 7️⃣ : Gerar o gráfico ===")
    print("📈 O gráfico mostrará:")
    print("💠 A parábola")
    print("💠 As raízes (se existirem)")
    print("💠 O vértice")
    print("💠 O ponto onde toca o eixo Y (c)\n")
    esperar()

    x = np.linspace(-20, 20, 400)
    y = a * x**2 + b * x + c

    plt.plot(x, y, label=f"{a}x² + {b}x + {c}")
    plt.title("Função de 2º Grau (Gráfico Didático)")

    # Eixos
    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)

    # Raízes
    if x1 is not None:
        plt.scatter(x1, 0, color="red", label=f"Raiz x₁ = {x1:.2f}")
        plt.text(x1, 0, f" ({x1:.2f}, 0)", color="red", fontsize=9)

    if x2 is not None and x2 != x1:
        plt.scatter(x2, 0, color="red", label=f"Raiz x₂ = {x2:.2f}")
        plt.text(x2, 0, f" ({x2:.2f}, 0)", color="red", fontsize=9)

    # Intercepto em Y
    plt.scatter(0, c, color="green", label=f"Intercepto em Y = {c}")
    plt.text(0, c, f" (0, {c:.2f})", color="green", fontsize=9)

    # Vértice
    plt.scatter(xv, yv, color="purple", label=f"Vértice ({xv:.2f}, {yv:.2f})")
    plt.text(xv, yv, f" ({xv:.2f}, {yv:.2f})", color="purple", fontsize=9)

    # Concavidade
    plt.scatter([], [], color="blue", label=abertura)

    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    plt.legend()

    plt.show()
