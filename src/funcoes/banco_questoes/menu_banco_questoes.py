import sys
import time


from .questoes_primeiro_grau import questoes_primeiro_grau
from .questoes_segundo_grau import questoes_segundo_grau
from .questoes_vertice import questoes_vertice
from .questoes_derivada import questoes_derivada


# Função de texto animado (digitando)
def escrever_animado(texto, delay=0.01):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def menu_banco_questoes():
    categorias = {
        "1": ("Funções de 1º Grau", questoes_primeiro_grau),
        "2": ("Funções de 2º Grau", questoes_segundo_grau),
        "3": ("Cálculo de Vértice", questoes_vertice),
        "4": ("Derivadas", questoes_derivada),
    }

    while True:
        escrever_animado("\n=======================================")
        escrever_animado("       📚  BANCO DE QUESTÕES  📚      ")
        escrever_animado("=======================================")
        escrever_animado("1️⃣  - Funções de 1º Grau")
        escrever_animado("2️⃣  - Funções de 2º Grau")
        escrever_animado("3️⃣  - Vértice")
        escrever_animado("4️⃣  - Derivadas")
        escrever_animado("0️⃣  - Voltar")
        escrever_animado("=======================================")

        opc = input("💭 Escolha uma categoria: ")

        if opc == "0":
            break

        if opc not in categorias:
            escrever_animado("\n❌ Opção inválida!")
            continue

        titulo, lista = categorias[opc]

        escrever_animado(f"\n=== {titulo.upper()} ===")

        for i, q in enumerate(lista):
            escrever_animado(f"{i+1} - {q['titulo']}")
        escrever_animado("0 - Voltar")

        esc_q = input("\n💭 Escolha a questão: ")

        if esc_q == "0":
            continue

        try:
            questao = lista[int(esc_q) - 1]
        except:
            escrever_animado("\n❌ Questão inválida!")
            continue

        exibir_questao(questao)


def exibir_questao(questao):
    escrever_animado("\n=======================================")
    escrever_animado("      📘 ENUNCIADO DA QUESTÃO 📘      ")
    escrever_animado("=======================================\n")
    escrever_animado(questao["enunciado"])

    input("\nPressione ENTER para ver a resposta...")

    escrever_animado("\n📌 RESPOSTA:")
    escrever_animado(questao["resposta"])

    while True:
        escrever_animado("\n👀 Deseja ver o passo a passo?")
        escrever_animado("1️⃣  - Sim")
        escrever_animado("0️⃣  - Voltar")
        escolha = input("Escolha: ")

        if escolha == "1":
            escrever_animado("\n🧠 PASSO A PASSO:\n")
            escrever_animado(questao["passo_a_passo"])
            input("\nPressione ENTER para voltar...")
            return

        elif escolha == "0":
            return

        else:
            escrever_animado("❌ Opção inválida!")
