# Imports de funções
from funcoes.funcao_primeiro_grau import funcao_primeiro_grau
from funcoes.funcao_segundo_grau import equacao_segundo_grau
from funcoes.grafico_primeiro_grau_didatico import gerar_grafico_primeiro_grau_didatico
from funcoes.grafico_primeiro_grau import gerar_grafico_primeiro_grau
from funcoes.grafico_segundo_grau import gerar_grafico_segundo_grau
from funcoes.grafico_segundo_grau_didatico import gerar_grafico_segundo_grau_didatico
from funcoes.derivada import calcular_derivada
from funcoes.vertice import calcular_xv_yv

# Import do banco de questões
from funcoes.banco_questoes.menu_banco_questoes import menu_banco_questoes


# Def da função do menu interativo
def menu():
    while True:
        print("\n=======================================")
        print("      🧮  SISTEMA DE CÁLCULOS  🧮       ")
        print("=======================================")
        print("1️⃣  - Função de 1º grau (Didático)")
        print("2️⃣  - Função de 2º grau (Didático)")
        print("3️⃣  - Gerar Gráfico - 1º Grau (Didático)")
        print("4️⃣  - Gerar Gráfico - 2º Grau (Didático)")
        print("5️⃣  - Gerar Gráfico - 1º Grau (Simples)")
        print("6️⃣  - Gerar Gráfico - 2º Grau (Simples)")
        print("7️⃣  - Calcular Derivada")
        print("8️⃣  - Calcular Vértice (Xv e Yv)")
        print("9️⃣  - Banco de Questões")
        print("\n0️⃣  - Sair")
        print("=======================================\n")

        opc = input("👉 Escolha uma opção: ")

        # 1 - Função de 1º grau
        if opc == "1":
            print("\n=======================================")
            print("   📏  Função de 1º grau: ax + b  📏    ")
            print("=======================================\n")
            a = float(input("✍️  Digite o valor de a: "))
            b = float(input("✍️  Digite o valor de b: "))
            funcao_primeiro_grau(a, b)

        # 2 - Função de 2º grau
        elif opc == "2":
            print("\n=======================================")
            print("📐  Função de 2º grau: ax² + bx + c  📐")
            print("=======================================\n")
            a = float(input("✍️  Digite o valor de a: "))
            b = float(input("✍️  Digite o valor de b: "))
            c = float(input("✍️  Digite o valor de c: "))
            equacao_segundo_grau(a, b, c)

        # 3 - Gráfico didático 1º grau
        elif opc == "3":
            print("\n=======================================")
            print("📊 Gráfico Didático da Função 1º Grau📊")
            print("=======================================\n")
            a = float(input("✍️  Digite o valor de a: "))
            b = float(input("✍️  Digite o valor de b: "))
            gerar_grafico_primeiro_grau_didatico(a, b)

        # 4 - Gráfico didático 2º grau
        elif opc == "4":
            print("\n=======================================")
            print("📊 Gráfico Didático da Função 2º Grau📊")
            print("=======================================\n")
            a = float(input("✍️  Digite o valor de a: "))
            b = float(input("✍️  Digite o valor de b: "))
            c = float(input("✍️  Digite o valor de c: "))
            gerar_grafico_segundo_grau_didatico(a, b, c)

        # 5 - Gráfico simples de 1º grau
        elif opc == "5":
            print("\n=======================================")
            print("📊 Gráfico Simples da Função 1º Grau 📊")
            print("=======================================\n")
            a = float(input("✍️  Digite o valor de a: "))
            b = float(input("✍️  Digite o valor de b: "))
            gerar_grafico_primeiro_grau(a, b)

        # 6 - Gráfico simples de 2º grau
        elif opc == "6":
            print("\n=======================================")
            print("📊 Gráfico Simples da Função 2º Grau 📊")
            print("=======================================\n")
            a = float(input("✍️  Digite o valor de a: "))
            b = float(input("✍️  Digite o valor de b: "))
            c = float(input("✍️  Digite o valor de c: "))
            gerar_grafico_segundo_grau(a, b, c)

        # 7 - Cálculo da Derivada
        elif opc == "7":
            print("\n=======================================")
            print(" 📐  Derivada de Função Polinomial  📐 ")
            print("=======================================\n")
            a = float(input("✍️  Digite o valor de a: "))
            exp_a = float(input("✍️  Digite o expoente do termo a: "))
            b = float(input("✍️  Digite o valor de b: "))
            exp_b = float(input("✍️  Digite o expoente do termo b: "))
            c = float(input("✍️  Digite o valor de c: "))
            calcular_derivada(a, exp_a, b, exp_b, c)

        # 8 - Cálculo do Vértice
        elif opc == "8":
            print("\n=======================================")
            print("📐 Vértices da Parábola: ax² + bx + c 📐")
            print("=======================================\n")
            a = float(input("✍️  Digite o valor de a: "))
            b = float(input("✍️  Digite o valor de b: "))
            c = float(input("✍️  Digite o valor de c: "))
            calcular_xv_yv(a, b, c)

        # 9 - Banco de Questões
        elif opc == "9":
            menu_banco_questoes()

        # 0 - Sair
        elif opc == "0":
            print("👋 Encerrando o programa...")
            break

        else:
            print("\n❌ Opção inválida! Tente novamente.")


menu()
