def calcular_derivada(a, exp_a, b, exp_b, c):
    print("\n=== DERIVADA ===")

    # Cálculo dos termos derivados
    deriv_a = a * exp_a
    exp_a_novo = exp_a - 1

    deriv_b = b * exp_b
    exp_b_novo = exp_b - 1

    print("\nFunção informada:")
    print(f"f(x) = {a}x^{exp_a} + {b}x^{exp_b} + {c}")

    print("\nPasso a passo da derivação:")

    print("\n1) Aplicando a regra do expoente (ou regra do poder):")
    print("   Se f(x) = k·xⁿ, então f’(x) = k·n·xⁿ⁻¹")

    print("\n--- Derivando o primeiro termo ---")
    print(f"   Termo original: {a}x^{exp_a}")
    print(f"   Multiplica o coeficiente pelo expoente: {a} × {exp_a} = {deriv_a}")
    print(f"   Diminui 1 do expoente: {exp_a} - 1 = {exp_a_novo}")
    print(f"   Termo derivado: {deriv_a}x^{exp_a_novo}")

    print("\n--- Derivando o segundo termo ---")
    print(f"   Termo original: {b}x^{exp_b}")
    print(f"   Multiplica o coeficiente pelo expoente: {b} × {exp_b} = {deriv_b}")
    print(f"   Diminui 1 do expoente: {exp_b} - 1 = {exp_b_novo}")
    print(f"   Termo derivado: {deriv_b}x^{exp_b_novo}")

    print("\n--- Derivando o termo constante ---")
    print(f"   A derivada de uma constante ({c}) é sempre 0.")

    print("\nResultado final da derivada:")
    print(f"f'(x) = {deriv_a}x^{exp_a_novo} + {deriv_b}x^{exp_b_novo}")
