def calcular_derivada(a, exp_a, b, exp_b, c):
    print("\n=== DERIVADA ===")

    deriv_a = a * exp_a
    exp_a_novo = exp_a - 1

    deriv_b = b * exp_b
    exp_b_novo = exp_b - 1

    print(f"f(x) = {a}x^{exp_a} + {b}x^{exp_b} + {c}")
    print("\nA derivada é:")
    print(f"f'(x) = {deriv_a}x^{exp_a_novo} + {deriv_b}x^{exp_b_novo}")
