import sympy as sp

x = sp.symbols('x')

print("Escolha o tipo de função:")
print("1 - Função de 1º grau (ax + b)")
print("2 - Função de 2º grau (ax² + bx + c)")
tipo = int(input("Opção: "))

if tipo == 1:
    a = float(input("a = "))
    b = float(input("b = "))
    f = a*x + b

elif tipo == 2:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    f = a*x**2 + b*x + c

derivada = sp.diff(f, x)
print("Derivada:", derivada)