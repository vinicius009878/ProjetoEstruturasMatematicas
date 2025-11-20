import sympy as sp

# Símbolo simbólico
x = sp.symbols("x")


def esperar(msg="Pressione ENTER para continuar..."):
    """Pausa a execução até o usuário apertar Enter."""
    try:
        input(msg)
    except:
        pass


def formatar_expr(expr):
    """Formata expressão de forma legível, substituindo ** por ^"""
    return str(expr).replace("**", "^").replace("*", "·")


def le_numero(msg, tipo=float, permitir_neg=True):
    """Lê um número do usuário. tipo pode ser float, int ou sp.Rational."""
    while True:
        try:
            s = input(msg).strip()
            if tipo is int:
                v = int(s)
            elif tipo is float:
                v = float(s)
            elif tipo is sp.Rational:
                if "/" in s:
                    num, den = s.split("/")
                    v = sp.Rational(int(num.strip()), int(den.strip()))
                else:
                    try:
                        v = sp.Rational(int(s))
                    except ValueError:
                        v = sp.nsimplify(float(s))
            else:
                v = tipo(s)

            if not permitir_neg and v < 0:
                print("❌ Valor negativo não permitido. Tente novamente.")
                continue
            return v

        except ValueError:
            print("❌ Entrada inválida. Digite um número válido.")
        except Exception as e:
            print(f"❌ Erro ao ler entrada: {e}")


# ----------------------------------------------------------
# DERIVADA DE 1º GRAU
# ----------------------------------------------------------


def derivada_1grau(a, b):
    func = a * x + b

    print("\n" + "=" * 70)
    print("📝 PASSO A PASSO DA DERIVAÇÃO — FUNÇÃO DE 1º GRAU")
    print("=" * 70)

    # Passo 1
    print("\n1️⃣ Função original:")
    print(f"   f(x) = {formatar_expr(func)}")
    esperar()

    # Passo 2
    print("\n2️⃣ Identificar os termos:")
    print(f"   • Termo linear: {formatar_expr(a*x)}")
    print(f"   • Termo constante: {formatar_expr(b)}")
    esperar()

    # Passo 3
    print("\n3️⃣ Aplicar a regra do expoente:")
    print("   📖 Se f(x) = k·x^n, então f'(x) = k·n·x^(n-1)\n")
    print(f"   • d/dx({formatar_expr(a*x)}) = {formatar_expr(a)}")
    print(f"   • d/dx({formatar_expr(b)}) = 0")
    esperar()

    # Passo 4
    deriv = sp.diff(func, x)
    print("\n4️⃣ Derivada total:")
    print(f"   f'(x) = {formatar_expr(deriv)}")
    esperar()

    # Final
    print("\n" + "=" * 70)
    print("✅ RESULTADO FINAL:")
    print("=" * 70)
    print(f"\nDerivada: f'(x) = {formatar_expr(deriv)}")
    print("\n💡 A derivada de uma função de 1º grau é sempre o coeficiente 'a'.")
    print("=" * 70 + "\n")


# ----------------------------------------------------------
# DERIVADA DE POLINÔMIO
# ----------------------------------------------------------


def derivada_polinomial(a, exp_a, b, exp_b, c):
    func = a * x**exp_a + b * x**exp_b + c

    print("\n" + "=" * 70)
    print("📝 PASSO A PASSO DA DERIVAÇÃO — FUNÇÃO POLINOMIAL")
    print("=" * 70)

    # Passo 1
    print("\n1️⃣ Função original:")
    print(f"   f(x) = {formatar_expr(func)}")
    esperar()

    # Passo 2
    print("\n2️⃣ Identificar os termos:")
    print(f"   • Primeiro termo: {formatar_expr(a * x**exp_a)}")
    print(f"   • Segundo termo:  {formatar_expr(b * x**exp_b)}")
    print(f"   • Termo constante: {formatar_expr(c)}")
    esperar()

    # Passo 3
    print("\n3️⃣ Aplicar a regra do expoente:")
    print("   📖 Se f(x) = k·x^n, então f'(x) = k·n·x^(n-1)\n")

    # Derivando primeiro termo
    print("   --- Derivando o primeiro termo ---")
    deriv_a = a * exp_a
    exp_a_novo = exp_a - 1
    print(f"   {formatar_expr(a)} × {exp_a} = {formatar_expr(deriv_a)}")
    print(f"   Novo expoente: {exp_a} - 1 = {exp_a_novo}")
    esperar()

    # Derivando segundo termo
    print("\n   --- Derivando o segundo termo ---")
    deriv_b = b * exp_b
    exp_b_novo = exp_b - 1
    print(f"   {formatar_expr(b)} × {exp_b} = {formatar_expr(deriv_b)}")
    print(f"   Novo expoente: {exp_b} - 1 = {exp_b_novo}")
    esperar()

    # Derivada do termo constante
    print("\n   --- Derivando o termo constante ---")
    print(f"   Derivada de {formatar_expr(c)} = 0")
    esperar()

    # Passo 4 — Resultado
    deriv = sp.simplify(sp.diff(func, x))
    print("\n4️⃣ Resultado final:")
    print(f"   f'(x) = {formatar_expr(deriv)}")
    esperar()

    # Final
    print("\n" + "=" * 70)
    print("✅ RESULTADO FINAL:")
    print("=" * 70)
    print(f"Função original: f(x) = {formatar_expr(func)}")
    print(f"Derivada final: f'(x) = {formatar_expr(deriv)}")
    print("=" * 70 + "\n")


# ----------------------------------------------------------
# Função principal usada no main
# ----------------------------------------------------------


def calcular_derivada(a, exp_a, b, exp_b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    exp_a = int(exp_a)
    exp_b = int(exp_b)

    derivada_polinomial(a, exp_a, b, exp_b, c)
