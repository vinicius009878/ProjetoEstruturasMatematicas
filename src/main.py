import os

# Imports de funções
from funcoes.funcao_primeiro_grau import funcao_primeiro_grau
from funcoes.funcao_segundo_grau import equacao_segundo_grau
from funcoes.grafico_primeiro_grau_didatico import gerar_grafico_primeiro_grau_didatico
from funcoes.grafico_primeiro_grau import gerar_grafico_primeiro_grau
from funcoes.grafico_segundo_grau import gerar_grafico_segundo_grau
from funcoes.grafico_segundo_grau_didatico import gerar_grafico_segundo_grau_didatico
from funcoes.vertice import calcular_xv_yv
from funcoes.menu_derivada import menu_derivadas
from funcoes.banco_questoes.menu_banco_questoes import menu_banco_questoes


# Funções para limpeza do terminal


def limpar_terminal():
    """Limpa o terminal"""
    os.system("cls" if os.name == "nt" else "clear")


def pausa_limpeza():
    """Pergunta se o usuário deseja limpar o terminal após uma operação."""
    escolha = (
        input("\n🔄 Deseja limpar o terminal antes de voltar ao menu? (s/n): ")
        .strip()
        .lower()
    )
    if escolha == "s":
        limpar_terminal()


# Menu principal
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
        print("7️⃣  - Calcular Derivadas")
        print("8️⃣  - Calcular Vértice (Xv e Yv)")
        print("9️⃣  - Banco de Questões")
        print("\n0️⃣  - Sair")
        print("=======================================\n")

        opc = input("👉 Escolha uma opção: ").strip()

        # 1 - Função de 1º grau
        if opc == "1":
            print("\n=======================================")
            print("   📏  Função de 1º grau: ax + b  📏    ")
            print("=======================================\n")
            a = float(input("✍️  Digite o valor de a: "))
            b = float(input("✍️  Digite o valor de b: "))
            funcao_primeiro_grau(a, b)
            pausa_limpeza()

        # 2 - Função de 2º grau
        elif opc == "2":
            print("\n=======================================")
            print("📐  Função de 2º grau: ax² + bx + c  📐")
            print("=======================================\n")
            a = float(input("✍️  Digite o valor de a: "))
            b = float(input("✍️  Digite o valor de b: "))
            c = float(input("✍️  Digite o valor de c: "))
            equacao_segundo_grau(a, b, c)
            pausa_limpeza()

        # 3 - Gráfico didático de 1º grau
        elif opc == "3":
            print("\n=======================================")
            print("📊 Gráfico Didático da Função 1º Grau📊")
            print("=======================================\n")
            a = float(input("✍️  Digite o valor de a: "))
            b = float(input("✍️  Digite o valor de b: "))
            gerar_grafico_primeiro_grau_didatico(a, b)
            pausa_limpeza()

        # 4 - Gráfico didático de 2º grau
        elif opc == "4":
            print("\n=======================================")
            print("📊 Gráfico Didático da Função 2º Grau📊")
            print("=======================================\n")
            a = float(input("✍️  Digite o valor de a: "))
            b = float(input("✍️  Digite o valor de b: "))
            c = float(input("✍️  Digite o valor de c: "))
            gerar_grafico_segundo_grau_didatico(a, b, c)
            pausa_limpeza()

        # 5 - Gráfico simples de 1º grau
        elif opc == "5":
            print("\n=======================================")
            print("📊 Gráfico Simples da Função 1º Grau 📊")
            print("=======================================\n")
            a = float(input("✍️  Digite o valor de a: "))
            b = float(input("✍️  Digite o valor de b: "))
            gerar_grafico_primeiro_grau(a, b)
            pausa_limpeza()

        # 6 - Gráfico simples de 2º grau
        elif opc == "6":
            print("\n=======================================")
            print("📊 Gráfico Simples da Função 2º Grau 📊")
            print("=======================================\n")
            a = float(input("✍️  Digite o valor de a: "))
            b = float(input("✍️  Digite o valor de b: "))
            c = float(input("✍️  Digite o valor de c: "))
            gerar_grafico_segundo_grau(a, b, c)
            pausa_limpeza()

        # 7 - Menu de Derivadas
        elif opc == "7":
            menu_derivadas()
            pausa_limpeza()

        # 8 - Cálculo do Vértice
        elif opc == "8":
            print("\n=======================================")
            print("📐 Vértices da Parábola: ax² + bx + c 📐")
            print("=======================================\n")
            a = float(input("✍️  Digite o valor de a: "))
            b = float(input("✍️  Digite o valor de b: "))
            c = float(input("✍️  Digite o valor de c: "))
            calcular_xv_yv(a, b, c)
            pausa_limpeza()

        # 9 - Banco de Questões
        elif opc == "9":
            menu_banco_questoes()
            pausa_limpeza()

        # 0 - Sair do programa
        elif opc == "0":
            print("👋 Encerrando o programa...")
            break

        else:
            print("\n❌ Opção inválida! Tente novamente.")
            pausa_limpeza()


# Execução do menu principal

menu()
