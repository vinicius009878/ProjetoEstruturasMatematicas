import sympy as sp

# Símbolo simbólico
x = sp.symbols("x")


def formatar_expr(expr):
    """Formata expressão de forma legível, substituindo ** por ^"""
    return str(expr).replace("**", "^").replace("*", "·")


def le_numero(msg, tipo=float, permitir_neg=True):
    """Lê um número do usuário. tipo pode ser float, int, ou sp.Rational (string aceita)."""
    while True:
        try:
            s = input(msg).strip()
            if tipo is int:
                v = int(s)
            elif tipo is float:
                v = float(s)
            elif tipo is sp.Rational:
                # Tenta entrar como racional 'a/b' ou inteiro
                if "/" in s:
                    num, den = s.split("/")
                    v = sp.Rational(int(num.strip()), int(den.strip()))
                else:
                    # Tenta int primeiro, senão float convertido para racional aproximado
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


def derivada_1grau(a, b):
    """Calcula e mostra passo a passo a derivada de ax + b."""
    func = a * x + b

    print("\n" + "=" * 70)
    print("📝 PASSO A PASSO DA DERIVAÇÃO")
    print("=" * 70)

    # Passo 1: Mostrar a função
    print("\n1️⃣ Função original:")
    print(f"   f(x) = {formatar_expr(func)}")

    # Passo 2: Identificar os termos
    print("\n2️⃣ Identificar os termos:")
    print(f"   • Termo linear: {formatar_expr(a*x)}")
    print(f"   • Termo constante: {formatar_expr(b)}")

    # Passo 3: Aplicar regra do expoente
    print("\n3️⃣ Aplicar a regra do expoente (ou regra do poder):")
    print("   📖 Se f(x) = k·x^n, então f'(x) = k·n·x^(n-1)")
    print()
    print(f"   • d/dx({formatar_expr(a*x)}) = {formatar_expr(a)}·d/dx(x)")
    print(f"                        = {formatar_expr(a)}·1")
    print(f"                        = {formatar_expr(a)}")
    print()
    print(f"   • d/dx({formatar_expr(b)}) = 0  (constante)")

    # Passo 4: Somar as derivadas
    deriv = sp.simplify(sp.diff(func, x))
    print("\n4️⃣ Derivada total (soma das derivadas parciais):")
    print(f"   f'(x) = {formatar_expr(a)} + 0")
    print(f"   f'(x) = {formatar_expr(deriv)}")

    # Resultado final
    print("\n" + "=" * 70)
    print("✅ RESULTADO FINAL:")
    print("=" * 70)
    print("\nFunção original:")
    print(f"   f(x) = {formatar_expr(func)}")
    print("\nDerivada:")
    print(f"   f'(x) = {formatar_expr(deriv)}")
    print("\n💡 Interpretação: A derivada de uma função de 1º grau é sempre")
    print("   o coeficiente angular (a), que representa a taxa de variação constante.")
    print("=" * 70 + "\n")


def derivada_polinomial(a, exp_a, b, exp_b, c):
    """Calcula e mostra passo a passo a derivada de ax^n + bx^m + c."""
    func = a * x**exp_a + b * x**exp_b + c

    print("\n" + "=" * 70)
    print("📝 PASSO A PASSO DA DERIVAÇÃO")
    print("=" * 70)

    # Passo 1: Mostrar a função
    print("\n1️⃣ Função original:")
    print(f"   f(x) = {formatar_expr(func)}")

    # Passo 2: Identificar os termos
    print("\n2️⃣ Identificar os termos:")
    print(f"   • Primeiro termo: {formatar_expr(a * x**exp_a)}")
    print(f"   • Segundo termo: {formatar_expr(b * x**exp_b)}")
    print(f"   • Termo constante: {formatar_expr(c)}")

    # Passo 3: Aplicar regra do expoente
    print("\n3️⃣ Aplicar a regra do expoente (ou regra do poder):")
    print("   📖 Se f(x) = k·x^n, então f'(x) = k·n·x^(n-1)")
    print()

    # Cálculo dos termos derivados
    deriv_a = a * exp_a
    exp_a_novo = exp_a - 1
    deriv_b = b * exp_b
    exp_b_novo = exp_b - 1

    # Derivada do primeiro termo
    print("   --- Derivando o primeiro termo ---")
    print(f"   Termo original: {formatar_expr(a * x**exp_a)}")
    print(
        f"   Multiplica o coeficiente pelo expoente: {formatar_expr(a)} × {int(exp_a)} = {formatar_expr(deriv_a)}"
    )
    print(f"   Diminui 1 do expoente: {int(exp_a)} - 1 = {int(exp_a_novo)}")
    if exp_a_novo == 0:
        print(f"   Termo derivado: {formatar_expr(deriv_a)}")
    elif exp_a_novo == 1:
        print(f"   Termo derivado: {formatar_expr(deriv_a)}·x")
    else:
        print(f"   Termo derivado: {formatar_expr(deriv_a)}·x^{int(exp_a_novo)}")
    print()

    # Derivada do segundo termo
    print("   --- Derivando o segundo termo ---")
    print(f"   Termo original: {formatar_expr(b * x**exp_b)}")
    print(
        f"   Multiplica o coeficiente pelo expoente: {formatar_expr(b)} × {int(exp_b)} = {formatar_expr(deriv_b)}"
    )
    print(f"   Diminui 1 do expoente: {int(exp_b)} - 1 = {int(exp_b_novo)}")
    if exp_b_novo == 0:
        print(f"   Termo derivado: {formatar_expr(deriv_b)}")
    elif exp_b_novo == 1:
        print(f"   Termo derivado: {formatar_expr(deriv_b)}·x")
    else:
        print(f"   Termo derivado: {formatar_expr(deriv_b)}·x^{int(exp_b_novo)}")
    print()

    # Derivada do termo constante
    print("   --- Derivando o termo constante ---")
    print(f"   A derivada de uma constante ({formatar_expr(c)}) é sempre 0.")

    # Passo 4: Resultado final da derivada
    deriv = sp.simplify(sp.diff(func, x))
    print("\n4️⃣ Resultado final da derivada:")
    print(f"   f'(x) = {formatar_expr(deriv)}")

    # Resultado final
    print("\n" + "=" * 70)
    print("✅ RESULTADO FINAL:")
    print("=" * 70)
    print("\nFunção original:")
    print(f"   f(x) = {formatar_expr(func)}")
    print("\nDerivada:")
    print(f"   f'(x) = {formatar_expr(deriv)}")
    print("\n💡 Interpretação: A derivada representa a taxa de variação instantânea")
    print("   da função em qualquer ponto x.")
    print("=" * 70 + "\n")


def calcular_derivada(a, exp_a, b, exp_b, c):
    """Função principal que será chamada pelo main.py"""
    # Converter para float se necessário
    a = float(a)
    exp_a = int(exp_a)
    b = float(b)
    exp_b = int(exp_b)
    c = float(c)

    derivada_polinomial(a, exp_a, b, exp_b, c)
