import sympy as sp

# Símbolo simbólico
x = sp.symbols('x')

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
                if '/' in s:
                    num, den = s.split('/')
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

def formatar_expr(expr):
    """Formata expressão de forma legível, substituindo ** por ^"""
    return str(expr).replace('**', '^').replace('*', '·')

def derivada_1grau(a, b):
    """Calcula e mostra passo a passo a derivada de ax + b."""
    func = a * x + b
    
    print("\n" + "="*70)
    print("📝 PASSO A PASSO DA DERIVAÇÃO")
    print("="*70)
    
    # Passo 1: Mostrar a função
    print("\n1️⃣ Função original:")
    print(f"   f(x) = {formatar_expr(func)}")
    
    # Passo 2: Identificar os termos
    print("\n2️⃣ Identificar os termos:")
    print(f"   • Termo linear: {formatar_expr(a*x)}")
    print(f"   • Termo constante: {formatar_expr(b)}")
    
    # Passo 3: Aplicar regras de derivação
    print("\n3️⃣ Aplicar as regras de derivação:")
    print("   📖 Regra da potência: d/dx(x^n) = n·x^(n-1)")
    print("   📖 Regra da constante: d/dx(c) = 0")
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
    print("\n" + "="*70)
    print("✅ RESULTADO FINAL:")
    print("="*70)
    print("\nFunção original:")
    print(f"   f(x) = {formatar_expr(func)}")
    print("\nDerivada:")
    print(f"   f'(x) = {formatar_expr(deriv)}")
    print("\n💡 Interpretação: A derivada de uma função de 1º grau é sempre")
    print("   o coeficiente angular (a), que representa a taxa de variação constante.")
    print("="*70 + "\n")

def derivada_polinomial(a, exp_a, b, exp_b, c):
    """Calcula e mostra passo a passo a derivada de ax^n + bx^m + c."""
    func = a * x**exp_a + b * x**exp_b + c
    
    print("\n" + "="*70)
    print("📝 PASSO A PASSO DA DERIVAÇÃO")
    print("="*70)
    
    # Passo 1: Mostrar a função
    print("\n1️⃣ Função original:")
    print(f"   f(x) = {formatar_expr(func)}")
    
    # Passo 2: Identificar os termos
    print("\n2️⃣ Identificar os termos:")
    print(f"   • Primeiro termo: {formatar_expr(a * x**exp_a)}")
    print(f"   • Segundo termo: {formatar_expr(b * x**exp_b)}")
    print(f"   • Termo constante: {formatar_expr(c)}")
    
    # Passo 3: Aplicar regras de derivação
    print("\n3️⃣ Aplicar as regras de derivação:")
    print("   📖 Regra da potência: d/dx(x^n) = n·x^(n-1)")
    print("   📖 Regra da constante multiplicativa: d/dx(c·f(x)) = c·f'(x)")
    print("   📖 Regra da constante: d/dx(c) = 0")
    print()
    
    # Derivada do primeiro termo
    deriv_termo1 = sp.diff(a * x**exp_a, x)
    print(f"   • Derivada de {formatar_expr(a * x**exp_a)}:")
    print(f"     d/dx({formatar_expr(a)}·x^{exp_a}) = {formatar_expr(a)}·{exp_a}·x^({exp_a}-1)")
    if exp_a - 1 == 0:
        print(f"                           = {formatar_expr(sp.simplify(deriv_termo1))}")
    elif exp_a - 1 == 1:
        print(f"                           = {formatar_expr(a * exp_a)}·x")
    else:
        print(f"                           = {formatar_expr(a * exp_a)}·x^{exp_a - 1}")
    print()
    
    # Derivada do segundo termo
    deriv_termo2 = sp.diff(b * x**exp_b, x)
    print(f"   • Derivada de {formatar_expr(b * x**exp_b)}:")
    print(f"     d/dx({formatar_expr(b)}·x^{exp_b}) = {formatar_expr(b)}·{exp_b}·x^({exp_b}-1)")
    if exp_b - 1 == 0:
        print(f"                           = {formatar_expr(sp.simplify(deriv_termo2))}")
    elif exp_b - 1 == 1:
        print(f"                           = {formatar_expr(b * exp_b)}·x")
    else:
        print(f"                           = {formatar_expr(b * exp_b)}·x^{exp_b - 1}")
    print()
    
    # Derivada do termo constante
    print(f"   • Derivada de {formatar_expr(c)}:")
    print(f"     d/dx({formatar_expr(c)}) = 0  (constante)")
    
    # Passo 4: Somar as derivadas
    deriv = sp.simplify(sp.diff(func, x))
    print("\n4️⃣ Derivada total (soma das derivadas parciais):")
    print(f"   f'(x) = {formatar_expr(sp.simplify(deriv_termo1))} + {formatar_expr(sp.simplify(deriv_termo2))} + 0")
    print(f"   f'(x) = {formatar_expr(deriv)}")
    
    # Resultado final
    print("\n" + "="*70)
    print("✅ RESULTADO FINAL:")
    print("="*70)
    print("\nFunção original:")
    print(f"   f(x) = {formatar_expr(func)}")
    print("\nDerivada:")
    print(f"   f'(x) = {formatar_expr(deriv)}")
    print("\n💡 Interpretação: A derivada representa a taxa de variação instantânea")
    print("   da função em qualquer ponto x.")
    print("="*70 + "\n")

def main():
    while True:
        print("\n" + "="*70)
        print("         📐 CALCULADORA DE DERIVADAS COM PASSO A PASSO 📐")
        print("="*70)
        print("1 - Função de 1º grau (ax + b)")
        print("2 - Função polinomial (ax^n + bx^m + c)")
        print("0 - Sair")
        print("="*70)
        opc = input("Escolha uma opção: ").strip()
        
        if opc == "0":
            print("\n👋 Encerrando... Até logo!")
            break
        
        elif opc == "1":
            print("\n" + "="*70)
            print("--- Derivada de Função de 1º Grau (ax + b) ---")
            print("="*70)
            a = le_numero("Digite o coeficiente 'a' (ex: 2 ou 3/4): ", tipo=sp.Rational)
            b = le_numero("Digite o coeficiente 'b' (constante, ex: 1 ou -2/3): ", tipo=sp.Rational)
            derivada_1grau(a, b)
        
        elif opc == "2":
            print("\n" + "="*70)
            print("--- Derivada de Função Polinomial (ax^n + bx^m + c) ---")
            print("="*70)
            a = le_numero("Digite o coeficiente 'a' (ex: 2 ou 3/4): ", tipo=sp.Rational)
            exp_a = le_numero("Digite o expoente 'n' do primeiro termo (inteiro): ", tipo=int, permitir_neg=False)
            
            b = le_numero("Digite o coeficiente 'b' (ex: 1 ou -5/2): ", tipo=sp.Rational)
            exp_b = le_numero("Digite o expoente 'm' do segundo termo (inteiro): ", tipo=int, permitir_neg=False)
            
            c = le_numero("Digite o coeficiente 'c' (constante): ", tipo=sp.Rational)
            
            derivada_polinomial(a, exp_a, b, exp_b, c)
        
        else:
            print("\n❌ Opção inválida! Escolha 0, 1 ou 2.\n")

if __name__ == "__main__":
    main()