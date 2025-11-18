from sympy import symbols, Eq, solve, S, pretty_print, simplify, sqrt, latex
from sympy.printing import pretty

x = symbols("x")

def formatar_expr(expr):
    """Formata expressão de forma legível, substituindo ** por ^"""
    return str(expr).replace('**', '^').replace('*', '·')

def ler_numero(msg):
    while True:
        try:
            entrada = input(msg).strip()
            return S(entrada)
        except Exception:
            print("Entrada inválida! Digite um número válido (ex: 2, -3, 4/5).")

def calcular_raiz_1grau():
    print("\n" + "="*60)
    print("--- Cálculo de raiz de função de 1º grau (ax + b = 0) ---")
    print("="*60)
    
    a = ler_numero("Digite o valor de a: ")
    b = ler_numero("Digite o valor de b: ")
    
    if a == 0:
        print("Erro: para ser 1º grau, o coeficiente 'a' deve ser diferente de 0.")
        return
    
    print("\n📝 PASSO A PASSO DA RESOLUÇÃO:")
    print("-" * 60)
    
    # Passo 1: Mostrar a equação
    print("\n1️⃣ Equação formada:")
    equacao = a * x + b
    print(f"   {formatar_expr(equacao)} = 0")
    
    # Passo 2: Isolar o termo com x
    print("\n2️⃣ Isolar o termo com x (passar o termo independente para o outro lado):")
    print(f"   {formatar_expr(a*x)} = {formatar_expr(-b)}")
    
    # Passo 3: Dividir pelo coeficiente
    print(f"\n3️⃣ Dividir ambos os lados por {formatar_expr(a)}:")
    print(f"   x = {formatar_expr(-b)}/{formatar_expr(a)}")
    
    # Passo 4: Simplificar
    raiz = solve(Eq(equacao, 0), x)[0]
    raiz_simplificada = simplify(raiz)
    
    print(f"\n4️⃣ Simplificar:")
    print(f"   x = {formatar_expr(raiz_simplificada)}")
    
    # Resultado final
    print("\n" + "="*60)
    print("✅ RESULTADO FINAL:")
    print("="*60)
    print("\nFunção:")
    print(f"   f(x) = {formatar_expr(equacao)}")
    print("\nRaiz da equação:")
    print(f"   x = {formatar_expr(raiz_simplificada)}")
    print("\n" + "="*60 + "\n")

def calcular_raiz_2grau():
    print("\n" + "="*60)
    print("--- Cálculo de raízes de função de 2º grau (ax² + bx + c = 0) ---")
    print("="*60)
    
    a = ler_numero("Digite o valor de a: ")
    b = ler_numero("Digite o valor de b: ")
    c = ler_numero("Digite o valor de c: ")
    
    if a == 0:
        print("Erro: em uma função de 2º grau, o coeficiente 'a' deve ser diferente de 0.")
        return
    
    print("\n📝 PASSO A PASSO DA RESOLUÇÃO (Fórmula de Bhaskara):")
    print("-" * 60)
    
    # Passo 1: Mostrar a equação
    print("\n1️⃣ Equação formada:")
    equacao_expr = a * x**2 + b * x + c
    print(f"   {formatar_expr(equacao_expr)} = 0")
    
    # Passo 2: Identificar coeficientes
    print("\n2️⃣ Identificar os coeficientes:")
    print(f"   a = {formatar_expr(a)}")
    print(f"   b = {formatar_expr(b)}")
    print(f"   c = {formatar_expr(c)}")
    
    # Passo 3: Calcular Delta
    delta = b**2 - 4*a*c
    delta_simplificado = simplify(delta)
    
    print("\n3️⃣ Calcular o discriminante (Δ = b² - 4ac):")
    print(f"   Δ = ({formatar_expr(b)})² - 4·({formatar_expr(a)})·({formatar_expr(c)})")
    print(f"   Δ = {formatar_expr(b**2)} - {formatar_expr(4*a*c)}")
    print(f"   Δ = {formatar_expr(delta_simplificado)}")
    
    # Passo 4: Analisar Delta
    print("\n4️⃣ Análise do discriminante:")
    if delta_simplificado > 0:
        print(f"   Δ > 0 → A equação possui DUAS raízes reais distintas")
    elif delta_simplificado == 0:
        print(f"   Δ = 0 → A equação possui UMA raiz real (raiz dupla)")
    else:
        print(f"   Δ < 0 → A equação possui DUAS raízes complexas conjugadas")
    
    # Passo 5: Aplicar Bhaskara
    print("\n5️⃣ Aplicar a fórmula de Bhaskara:")
    print(f"   x = (-b ± √Δ) / (2a)")
    print(f"   x = (-({formatar_expr(b)}) ± √({formatar_expr(delta_simplificado)})) / (2·{formatar_expr(a)})")
    
    if delta_simplificado >= 0:
        sqrt_delta = sqrt(delta_simplificado)
        print(f"   x = ({formatar_expr(-b)} ± {formatar_expr(sqrt_delta)}) / {formatar_expr(2*a)}")
    else:
        sqrt_delta = sqrt(-delta_simplificado)
        print(f"   x = ({formatar_expr(-b)} ± {formatar_expr(sqrt_delta)}i) / {formatar_expr(2*a)}")
    
    # Resolver
    raizes = solve(Eq(equacao_expr, 0), x)
    
    # Separar raízes reais e complexas
    reais = []
    complexas = []
    for r in raizes:
        r_s = simplify(r)
        if r_s.is_real:
            reais.append(r_s)
        else:
            complexas.append(r_s)
    
    # Passo 6: Calcular cada raiz
    print("\n6️⃣ Calcular as raízes:")
    
    if len(raizes) == 2:
        valor_sqrt = sqrt(abs(delta_simplificado)) if delta_simplificado >= 0 else f"{formatar_expr(sqrt(-delta_simplificado))}i"
        print(f"   x₁ = ({formatar_expr(-b)} + {valor_sqrt}) / {formatar_expr(2*a)}")
        print(f"   x₁ = {formatar_expr(simplify(raizes[0]))}")
        print()
        print(f"   x₂ = ({formatar_expr(-b)} - {valor_sqrt}) / {formatar_expr(2*a)}")
        print(f"   x₂ = {formatar_expr(simplify(raizes[1]))}")
    elif len(raizes) == 1:
        print(f"   x = {formatar_expr(-b)} / {formatar_expr(2*a)}")
        print(f"   x = {formatar_expr(simplify(raizes[0]))}")
    
    # Resultado final
    print("\n" + "="*60)
    print("✅ RESULTADO FINAL:")
    print("="*60)
    print("\nFunção:")
    print(f"   f(x) = {formatar_expr(equacao_expr)}")
    
    print("\nRaízes encontradas:")
    if reais:
        print("\n→ Raízes reais:")
        for i, r in enumerate(reais, 1):
            print(f"   x{i} = {formatar_expr(r)}")
    
    if complexas:
        print("\n→ Raízes complexas:")
        for i, r in enumerate(complexas, 1):
            print(f"   x{i} = {formatar_expr(r)}")
    
    print("\n" + "="*60 + "\n")

def menu():
    while True:
        print("\n" + "="*60)
        print("         🧮 CALCULADORA DE RAÍZES COM PASSO A PASSO 🧮")
        print("="*60)
        print("1 - Função de 1º grau (ax + b = 0)")
        print("2 - Função de 2º grau (ax² + bx + c = 0)")
        print("0 - Sair")
        print("="*60)
        opc = input("Escolha uma opção: ").strip()
        
        if opc == "0":
            print("\n👋 Encerrando... Até logo!")
            break
        elif opc == "1":
            calcular_raiz_1grau()
        elif opc == "2":
            calcular_raiz_2grau()
        else:
            print("\n❌ Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    menu()