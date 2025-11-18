# main.py

# === IMPORTAÇÕES DAS FUNÇÕES ===
from funcoes.calculofuncao1 import funcao_primeiro_grau
from funcoes.calculofuncao2 import equacao_segundo_grau
from funcoes.calculoderivada import calcular_derivada
from funcoes.calculovertice import calcular_xv_yv
from funcoes.graficoisolado1 import gerar_grafico_primeiro_grau
from funcoes.graficoisolado2 import gerar_grafico_segundo_grau


# ============================================
# ===============     MENU     ===============
# ============================================


def menu():
    while True:
        print("\n=======================================")
        print("          SISTEMA DE CÁLCULOS          ")
        print("=======================================")
        print("1 - Função de 1º grau (explicada)")
        print("2 - Função de 2º grau (explicada)")
        print("3 - Gerar Gráfico - 1º Grau")
        print("4 - Gerar Gráfico - 2º Grau")
        print("5 - Calcular Derivada")
        print("6 - Calcular Vértice (Xv e Yv)")
        print("0 - Sair")
        print("=======================================")

        opc = input("Escolha uma opção: ")

        # ----------------------------------------
        # 1 - Função de 1º grau
        # ----------------------------------------
        if opc == "1":
            print("\n--- Função de 1º grau: ax + b ---")
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            funcao_primeiro_grau(a, b)

        # ----------------------------------------
        # 2 - Função de 2º grau
        # ----------------------------------------
        elif opc == "2":
            print("\n--- Função de 2º grau: ax² + bx + c ---")
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))
            equacao_segundo_grau(a, b, c)

        # ----------------------------------------
        # 3 - Gráfico 1º Grau
        # ----------------------------------------
        elif opc == "3":
            print("\n--- Gráfico da Função de 1º Grau ---")
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            gerar_grafico_primeiro_grau(a, b)

        # ----------------------------------------
        # 4 - Gráfico 2º Grau
        # ----------------------------------------
        elif opc == "4":
            print("\n--- Gráfico da Função de 2º Grau ---")
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))
            gerar_grafico_segundo_grau(a, b, c)

        # ----------------------------------------
        # 5 - Derivada
        # ----------------------------------------
        elif opc == "5":
            print("\n--- Derivada de ax^n + bx^m + c ---")
            a = float(input("Digite o valor de a: "))
            exp_a = float(input("Digite o expoente do termo a: "))
            b = float(input("Digite o valor de b: "))
            exp_b = float(input("Digite o expoente do termo b: "))
            c = float(input("Digite o valor de c: "))
            calcular_derivada(a, exp_a, b, exp_b, c)

        # ----------------------------------------
        # 6 - Vértice
        # ----------------------------------------
        elif opc == "6":
            print("\n--- Vértice da parábola ax² + bx + c ---")
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))
            calcular_xv_yv(a, b, c)

        # ----------------------------------------
        # 0 - SAIR
        # ----------------------------------------
        elif opc == "0":
            print("Encerrando o programa...")
            break

        else:
            print("\nOpção inválida! Tente novamente.")


# ============================================
# ===============   EXECUÇÃO   ===============
# ============================================

if __name__ == "__main__":
    menu()
