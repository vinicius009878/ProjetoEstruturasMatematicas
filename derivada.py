import sympy as sp

x = sp.symbols('x')

while True:
    print("=== Derivada de Funções Polinomiais ===")
    print("Você pode escolher o número de termos da função, e os coeficientes e expoentes de cada termo.")
    print("0 - Sair")
    op = input("Digite qualquer tecla para continuar ou 0 para sair: ")

    if op == "0":
        print("Encerrando...")
        break

    termos = int(input("Quantos termos sua função terá? "))

    f = 0
    for i in range(1, termos+1):
        print(f"\nTermo {i}:")
        a = float(input("Coeficiente (a): "))
        e = int(input("Expoente de x (ex: 1, 2, 3...): "))
        f += a * x**e

    print("\nFunção montada:")
    print(f"f(x) = {f}")

    derivada = sp.diff(f, x)
    print("\nDerivada:")
    print("f'(x) =", derivada)

    input("\nPressione ENTER para fazer outra derivada...")
