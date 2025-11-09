import math as mt
def equacao_segundo_grau(a, b, c):
    print("=== Analisador de Equação do Segundo Grau ===")
    print("Forma geral: f(x) = ax² + bx + c\n")

    if a == 0:
        print("\nIsso não é uma equação de segundo grau (a deve ser diferente de 0).")
        return

    print("\n=== Resultados ===")

    delta = b**2 - 4*a*c
    print(f"Δ (Delta) = {delta:.2f}")

    if delta < 0:
        print("A equação não possui raízes reais.")
        x1 = x2 = None
    elif delta == 0:
        x1 = x2 = -b / (2*a)
        print(f"Raiz única: x₁ = x₂ = {x1:.2f}")
    else:
        x1 = (-b + mt.sqrt(delta)) / (2*a)
        x2 = (-b - mt.sqrt(delta)) / (2*a)
        print(f"x₁ = {x1:.2f}")
        print(f"x₂ = {x2:.2f}")

    x = float(input("\nDigite um valor para x: "))
    fx = (a * (x**2)) + (x * b) + c
    print(f"f({x}) = {fx:.2f}")

    xv = -b / (2*a)
    if xv is not None:  
        print(f"O valor de x do vértice é: {xv:.2f}")

    yv = -delta / (4*a)
    if yv is not None:
        print(f"O valor de y do vértice é: {yv:.2f}")