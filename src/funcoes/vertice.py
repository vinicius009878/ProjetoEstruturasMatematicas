# Função auxiliar para pausar até o usuário pressionar Enter
def esperar(mensagem="Pressione Enter para continuar..."):
    try:
        input(mensagem)
    except (KeyboardInterrupt, EOFError):
        print("\n❌ Interrompido pelo usuário.")
        raise SystemExit


# Função para calcular o vértice da função de 2º grau
def calcular_xv_yv(a, b, c):
    print("\n=== 📝 Cálculo Didático do Vértice da Função de 2º Grau 📝 ===")
    print("🔶 Forma geral: f(x) = ax² + bx + c\n")

    # Verificação
    if a == 0:
        print("⚠️ Não existe vértice, pois a = 0 (não é função de 2º grau).")
        return

    # Passo 1
    print("=== Passo 1️⃣ : Confirmar função quadrática ===")
    print("‼️  Como a ≠ 0, trata-se de uma função do 2º grau.\n")
    esperar()

    # Cálculo Do Xv
    print("=== Passo 2️⃣ : Calcular o X do vértice ===")
    print("🔶 Fórmula:  Xv = -b / (2a)")
    print(f"🔄️ Substituindo: Xv = -({b}) / (2 * {a})\n")

    xv = -b / (2 * a)
    print(f"❇️  Xv = {xv:.4f}\n")
    esperar()

    # Cálculo Do Yv
    print("=== Passo 3️⃣ : Calcular o Y do vértice ===")
    print("🔶 Fórmula:  Yv = a·Xv² + b·Xv + c")
    print(f"🔄️ Substituindo: Yv = {a} * ({xv}²) + {b} * ({xv}) + {c}\n")

    yv = a * xv**2 + b * xv + c
    print(f"❇️  Yv = {yv:.4f}\n")
    esperar()

    # Resultado Final
    print("=== ✅ Resultado Final ===")
    print(f"\n❇️  Vértice da parábola:  ({xv:.4f}, {yv:.4f})\n")

    if a > 0:
        print("‼️  O vértice é um ponto de MÍNIMO (a > 0).\n")
    else:
        print("‼️  O vértice é um ponto de MÁXIMO (a < 0).\n")
