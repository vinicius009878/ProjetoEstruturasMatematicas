from funcoes.derivada import derivada_1grau, derivada_polinomial, le_numero


def menu_derivadas():
    while True:
        print("\n=======================================")
        print("        📐 MENU DE DERIVADAS 📐        ")
        print("=======================================\n")
        print("1️⃣  - Derivada de função de 1º grau (ax + b)")
        print("2️⃣  - Derivada de polinômio (ax^n + bx^m + c)")
        print("0️⃣  - Voltar")
        print("=======================================\n")

        opc = input("💭 Escolha: ").strip()

        if opc == "1":
            a = le_numero("\n✍️  Digite o coeficiente a: ")
            b = le_numero("✍️  Digite o coeficiente b: ")
            derivada_1grau(a, b)

        elif opc == "2":
            a = le_numero("\n✍️  Digite o coeficiente a: ")
            exp_a = le_numero("✍️  Expoente do termo a·x^n: ", int)
            b = le_numero("✍️  Digite o coeficiente b: ")
            exp_b = le_numero("✍️  Expoente do termo b·x^m: ", int)
            c = le_numero("✍️  Digite a constante c: ")
            derivada_polinomial(a, exp_a, b, exp_b, c)

        elif opc == "0":
            break

        else:
            print("❌ Opção inválida. Tente novamente.")
