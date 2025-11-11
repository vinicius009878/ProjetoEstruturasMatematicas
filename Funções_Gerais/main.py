import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def menu():
    print("\n=== CALCULADORA DE FUNÇÕES ===")
    print("1 - Gerar gráfico de função de 1º grau")
    print("2 - Gerar gráfico de função de 2º grau")
    print("3 - Calcular função de 1º grau (ax + b)")
    print("4 - Calcular função de 2º grau (ax² + bx + c)")
    print("5 - Calcular derivada")
    print("6 - Calcular vértice (Xv e Yv)")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def grafico_1_grau():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    x = np.linspace(-10, 10, 200)
    y = a*x + b
    plt.plot(x, y, label=f"f(x)={a}x+{b}")
    plt.title("Função de 1º Grau")
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.legend()
    plt.grid(True)
    plt.show()

def grafico_2_grau():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    x = np.linspace(-10, 10, 200)
    y = a*x**2 + b*x + c
    plt.plot(x, y, label=f"f(x)={a}x²+{b}x+{c}")
    plt.title("Função de 2º Grau")
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.legend()
    plt.grid(True)
    plt.show()

def calcular_1_grau():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    x = float(input("Digite o valor de x: "))
    y = a*x + b
    print(f"f({x}) = {y}")

def calcular_2_grau():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    x = float(input("Digite o valor de x: "))
    y = a*x**2 + b*x + c
    print(f"f({x}) = {y}")

def calcular_derivada():
    x = sp.Symbol('x')
    expressao = sp.sympify(input("Digite a função (ex: 3*x**2 + 2*x + 1): "))
    derivada = sp.diff(expressao, x)
    print(f"A derivada de {expressao} é: {derivada}")

def calcular_vertice():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    xv = -b / (2*a)
    yv = a*xv**2 + b*xv + c
    print(f"Xv = {xv}")
    print(f"Yv = {yv}")

def main():
    while True:
        opcao = menu()
        if opcao == "1":
            grafico_1_grau()
        elif opcao == "2":
            grafico_2_grau()
        elif opcao == "3":
            calcular_1_grau()
        elif opcao == "4":
            calcular_2_grau()
        elif opcao == "5":
            calcular_derivada()
        elif opcao == "6":
            calcular_vertice()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()