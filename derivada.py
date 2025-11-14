import sympy as sp
from sympy import symbols, diff, simplify

x = symbols('x')

# Aqui o usuário pode escolher o tipo de função para calcular a derivada
while True:
    print("=== CÁLCULO DE DERIVADA ===")
    print("1 - Função de 1º grau (ax + b)")
    print("2 - Função de 2º grau (ax² + bx + c)")
    print("0 - Sair")

    opc = input("Escolha: ")

    if opc == "0":
        print("Encerrando...")
        break

    # Cálculo da derivada de acordo com a escolha do usuário (Função de 1º)
    if opc == "1":
        print("--- Função de 1º grau ---")

        a = float(input("Digite o valor de a: "))

        b = float(input("Digite o valor de b (constante, sem expoente): "))

        func = a * x + b
        derivada = simplify(diff(func, x))

        print(f"Função: {func}")
        print(f"Derivada: {derivada}")
        
    # Cálculo da derivada de acordo com a escolha do usuário (Função de 2º)
    elif opc == "2":
        print("--- Função de 2º grau ---")

        a = float(input("Digite o valor de a: "))
        exp_a = float(input("Digite o expoente do termo 'a': "))

        b = float(input("Digite o valor de b: "))
        exp_b = float(input("Digite o expoente do termo 'b': "))

        c = float(input("Digite o valor de c (constante, sem expoente): "))
        
        # Monta a string da função na ordem digitada
        func_str = f"{a}*x**{exp_a} + {b}*x**{exp_b} + {c}"

        # Define a função e calcula a derivada
        func = a * x**exp_a + b * x**exp_b + c
        derivada = simplify(diff(func, x))

        # Exibe a função que o usuário definiu e sua derivada
        print(f"Função Montada: {func_str}")
        print(f"Derivada: {derivada}")
        
        input("Pressione Enter para continuar...")
        
    # Caso o usuário digite uma opção inválida        
    else:
        print("Opção inválida!")