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


# Derivada de função de 1º grau
def derivada_1grau(a, b):
    func = a * x + b

    print("\n" + "=" * 50)
    print("📝 PASSO A PASSO DA DERIVAÇÃO — FUNÇÃO DE 1º GRAU")
    print("=" * 50)

    # Função formada
    print("\n💠 Função original:")
    print(f"💠 f(x) = {formatar_expr(func)}")
    esperar()

    # Passo 1
    print("\n=== Passo 1️⃣ : Identificar os termos ===")
    print(f"💠 Termo linear: {formatar_expr(a*x)}")
    print(f"💠 Termo constante: {formatar_expr(b)}")
    esperar()

    # Passo 2
    print("\n=== Passo 2️⃣ : Aplicar a regra do expoente ===")
    print("📖 Se f(x) = k·x^n, então f'(x) = k·n·x^(n-1)\n")
    print(f"💠 d/dx({formatar_expr(a*x)}) = {formatar_expr(a)}")
    print(f"💠 d/dx({formatar_expr(b)}) = 0")
    esperar()

    # Passo 3
    deriv = sp.diff(func, x)
    print("\n=== Passo 3️⃣ : Derivada total ===")
    print(f"   f'(x) = {formatar_expr(deriv)}")
    esperar()

    # Final
    print("\n" + "=" * 40)
    print("✅ RESULTADO FINAL:")
    print("=" * 40)
    print(f"\n❇️  Derivada: f'(x) = {formatar_expr(deriv)}")
    print("\n💡 A derivada de uma função de 1º grau é sempre o coeficiente 'a'.")
    print("=" * 70 + "\n")


# Derivada de polinômio
def derivada_polinomial(a, exp_a, b, exp_b, c):
    func = a * x**exp_a + b * x**exp_b + c

    print("\n" + "=" * 50)
    print("📝 PASSO A PASSO DA DERIVAÇÃO — FUNÇÃO POLINOMIAL")
    print("=" * 50)

    # Função formada
    print("\n💠 Função original:")
    print(f"💠 f(x) = {formatar_expr(func)}")
    esperar()

    # Passo 1
    print("\n=== Passo 1️⃣ : Identificar os termos ===")
    print(f"💠 Primeiro termo: {formatar_expr(a * x**exp_a)}")
    print(f"💠 Segundo termo:  {formatar_expr(b * x**exp_b)}")
    print(f"💠 Termo constante: {formatar_expr(c)}")
    esperar()

    # Passo 2
    print("\n=== Passo 2️⃣ : Aplicar a regra do expoente ===")
    print("📖 Se f(x) = k·x^n, então f'(x) = k·n·x^(n-1)")

    # Passo 3 - Derivando primeiro termo
    print("\n=== Passo 3️⃣ : Derivando o primeiro termo ===")
    deriv_a = a * exp_a
    exp_a_novo = exp_a - 1
    print(f"💠 {formatar_expr(a)} × {exp_a} = {formatar_expr(deriv_a)}")
    print(f"🔹 Novo expoente: {exp_a} - 1 = {exp_a_novo}")
    esperar()

    # Passo 4 - Derivando segundo termo
    print("\n=== Passo 4️⃣ : Derivando o segundo termo ===")
    deriv_b = b * exp_b
    exp_b_novo = exp_b - 1
    print(f"💠 {formatar_expr(b)} × {exp_b} = {formatar_expr(deriv_b)}")
    print(f"🔹 Novo expoente: {exp_b} - 1 = {exp_b_novo}")
    esperar()

    # Passo 5 - Derivada do termo constante
    print("\n=== Passo 5️⃣ : Derivando o termo constante ===")
    print(f"💠 Derivada de {formatar_expr(c)} = 0")
    esperar()

    # Passo 6 — Resultado
    deriv = sp.simplify(sp.diff(func, x))
    print("\n=== Passo 6️⃣ : Exibindo o Resultado final ===")
    print(f"❇️  f'(x) = {formatar_expr(deriv)}")
    esperar()

    # Final
    print("\n" + "=" * 50)
    print("✅ RESULTADO FINAL:")
    print("=" * 50)
    print(f"💠 Função original: f(x) = {formatar_expr(func)}")
    print(f"❇️  Derivada final: f'(x) = {formatar_expr(deriv)}")
    print("=" * 50 + "\n")


# Função principal usada no main


def calcular_derivada(a, exp_a, b, exp_b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    exp_a = int(exp_a)
    exp_b = int(exp_b)

    derivada_polinomial(a, exp_a, b, exp_b, c)
