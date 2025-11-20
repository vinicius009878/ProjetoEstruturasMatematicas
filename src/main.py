import os
import sys
import time


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


# Função de texto animado
def escrever_animado(texto, delay=0.01):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


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
        escrever_animado("\n=======================================")
        escrever_animado("      🧮  SISTEMA DE CÁLCULOS  🧮       ")
        escrever_animado("=======================================")
        escrever_animado("1️⃣  - Função de 1º grau (Didático)")
        escrever_animado("2️⃣  - Função de 2º grau (Didático)")
        escrever_animado("3️⃣  - Gerar Gráfico - 1º Grau (Didático)")
        escrever_animado("4️⃣  - Gerar Gráfico - 2º Grau (Didático)")
        escrever_animado("5️⃣  - Gerar Gráfico - 1º Grau (Simples)")
        escrever_animado("6️⃣  - Gerar Gráfico - 2º Grau (Simples)")
        escrever_animado("7️⃣  - Calcular Derivadas")
        escrever_animado("8️⃣  - Calcular Vértice (Xv e Yv)")
        escrever_animado("9️⃣  - Banco de Questões")
        escrever_animado("\n0️⃣  - Sair")
        escrever_animado("=======================================\n")

        opc = input("👉 Escolha uma opção: ").strip()

        # 1 - Função de 1º grau
        if opc == "1":
            escrever_animado("\n=======================================")
            escrever_animado("   📏  Função de 1º grau: ax + b  📏    ")
            escrever_animado("=======================================\n")
            a = float(input("✍️  Digite o valor de a: "))
            b = float(input("✍️  Digite o valor de b: "))
            funcao_primeiro_grau(a, b)
            pausa_limpeza()

        # 2 - Função de 2º grau
        elif opc == "2":
            escrever_animado("\n=======================================")
            escrever_animado("📐  Função de 2º grau: ax² + bx + c  📐")
            escrever_animado("=======================================\n")
            a = float(input("✍️  Digite o valor de a: "))
            b = float(input("✍️  Digite o valor de b: "))
            c = float(input("✍️  Digite o valor de c: "))
            equacao_segundo_grau(a, b, c)
            pausa_limpeza()

        # 3 - Gráfico didático de 1º grau
        elif opc == "3":
            escrever_animado("\n=======================================")
            escrever_animado("📊 Gráfico Didático da Função 1º Grau📊")
            escrever_animado("=======================================\n")
            a = float(input("✍️  Digite o valor de a: "))
            b = float(input("✍️  Digite o valor de b: "))
            gerar_grafico_primeiro_grau_didatico(a, b)
            pausa_limpeza()

        # 4 - Gráfico didático de 2º grau
        elif opc == "4":
            escrever_animado("\n=======================================")
            escrever_animado("📊 Gráfico Didático da Função 2º Grau📊")
            escrever_animado("=======================================\n")
            a = float(input("✍️  Digite o valor de a: "))
            b = float(input("✍️  Digite o valor de b: "))
            c = float(input("✍️  Digite o valor de c: "))
            gerar_grafico_segundo_grau_didatico(a, b, c)
            pausa_limpeza()

        # 5 - Gráfico simples de 1º grau
        elif opc == "5":
            escrever_animado("\n=======================================")
            escrever_animado("📊 Gráfico Simples da Função 1º Grau 📊")
            escrever_animado("=======================================\n")
            a = float(input("✍️  Digite o valor de a: "))
            b = float(input("✍️  Digite o valor de b: "))
            gerar_grafico_primeiro_grau(a, b)
            pausa_limpeza()

        # 6 - Gráfico simples de 2º grau
        elif opc == "6":
            escrever_animado("\n=======================================")
            escrever_animado("📊 Gráfico Simples da Função 2º Grau 📊")
            escrever_animado("=======================================\n")
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
            escrever_animado("\n=======================================")
            escrever_animado("📐 Vértices da Parábola: ax² + bx + c 📐")
            escrever_animado("=======================================\n")
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
            escrever_animado("👋 Encerrando o programa...")
            break

        else:
            escrever_animado("\n❌ Opção inválida! Tente novamente.")
            pausa_limpeza()


# Execução do menu principal
menu()
