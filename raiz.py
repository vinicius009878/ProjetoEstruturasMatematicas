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

raizes = sp.solve(f, x)

# Converte cada raiz para fração exata (Rational)
raizes_formatadas = [sp.nsimplify(r) for r in raizes]

print("Raízes (formato simbólico):", raizes_formatadas)
