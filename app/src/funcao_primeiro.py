# funcionando
def funcao_primeiro_grau(a, b):
    print("\n\n=== Analisador de Função de Primeiro Grau ===")
    print("Forma geral: f(x) = ax + b\n")

    if a == 0:
        print("\nIsso não é uma função de primeiro grau (a deve ser diferente de 0).")
        return

    print("\n=== Resultados ===")

    raiz = -b / a
    print(f"Raiz da função (f(x)=0): x = {raiz:.2f}")

    if a > 0:
        print("A função é crescente (a > 0).")
    else:
        print("A função é decrescente (a < 0).")

    print(f"\nEquação: f(x) = {a}x + {b}")

    x = float(input("\nDigite um valor para x: "))
    fx = a * x + b
    print(f"f({x}) = {fx:.2f}")

    xv = -b / (2*a)
    print(f"O valor de x do vértice é: {xv:.2f}")