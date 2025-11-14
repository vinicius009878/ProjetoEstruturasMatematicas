from sympy import symbols, Eq, solve, S

def menu():
    while True:
        print("=== CÁLCULO DE RAÍZES ===")
        print("1 - Função de 1º grau (ax + b)")
        print("2 - Função de 2º grau (ax² + bx + c)")
        print("0 - Sair")

        opc = input("Escolha: ")

        if opc == "0":
            print("Encerrando...")
            break

        elif opc == "1":
            print("--- Cálculo de raíz de Função de 1º grau ---")
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))

            if a == 0:
                print("O valor de 'a' não pode ser zero em uma função de 1º grau.")
                continue

            x = symbols("x")
            equacao = Eq(a * x + b, 0)
            raiz = solve(equacao, x)

            print(f"A raíz da função {a}x + {b} é: {raiz[0]}")

        elif opc == "2":
            print("--- Cálculo de raíz de Função de 2º grau ---")
            a = int(input("Digite o valor de a: "))
            b = int(input("Digite o valor de b: "))
            c = int(input("Digite o valor de c: "))

            if a == 0:
                print("O valor de 'a' não pode ser zero em uma função de 2º grau.")
                continue

            x = symbols("x")
            equacao = Eq(a * x**2 + b * x + c, 0)
            raizes = solve(equacao, x)

            reais = [S(r) for r in raizes if r.is_real]

            if not reais:
                print("A função não possui raízes reais.")
                continue

            print(f"Raízes reais da função {a}x² + {b}x + {c}:")
            for r in reais:
                print(r)


menu()