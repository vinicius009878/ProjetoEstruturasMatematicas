import sympy as sp

x = sp.symbols('x')

while True:
    print("=== Cálculo de Raízes ===")
    print("1 - Função de 1º grau (ax + b)")
    print("2 - Função de 2º grau (ax² + bx + c)")
    print("0 - Sair")
    tipo = int(input("Opção: "))

    if tipo == 0:
        print("Encerrando...")
        break

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
    raizes_formatadas = []

    for r in raizes:
        r = sp.nsimplify(r)
        if r.is_real:
            raizes_formatadas.append(sp.simplify(r))
        else:
            raizes_formatadas.append(sp.simplify(r))

    print("Raízes:")
    for raiz in raizes_formatadas:
        print("  →", raiz)

    input("Pressione ENTER para calcular outra raiz...")
