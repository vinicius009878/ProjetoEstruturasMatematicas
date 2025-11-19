from .questoes_primeiro_grau import questoes_primeiro_grau
from .questoes_segundo_grau import questoes_segundo_grau
from .questoes_vertice import questoes_vertice
from .questoes_derivada import questoes_derivada


def menu_banco_questoes():
    categorias = {
        "1": ("Funções de 1º Grau", questoes_primeiro_grau),
        "2": ("Funções de 2º Grau", questoes_segundo_grau),
        "3": ("Cálculo de Vértice", questoes_vertice),
        "4": ("Derivadas", questoes_derivada),
    }

    while True:
        print("\n=======================================")
        print("           BANCO DE QUESTÕES           ")
        print("=======================================")
        print("1 - Funções de 1º Grau")
        print("2 - Funções de 2º Grau")
        print("3 - Vértice")
        print("4 - Derivadas")
        print("0 - Voltar")
        print("=======================================")

        opc = input("Escolha uma categoria: ")

        if opc == "0":
            break

        if opc not in categorias:
            print("\n❌ Opção inválida!")
            continue

        titulo, lista = categorias[opc]

        print(f"\n=== {titulo.upper()} ===")

        for i, q in enumerate(lista):
            print(f"{i+1} - {q['titulo']}")
        print("0 - Voltar")

        esc_q = input("\nEscolha a questão: ")

        if esc_q == "0":
            continue

        try:
            questao = lista[int(esc_q) - 1]
        except:
            print("\n❌ Questão inválida!")
            continue

        exibir_questao(questao)


def exibir_questao(questao):
    print("\n=======================================")
    print("📘 ENUNCIADO DA QUESTÃO")
    print("=======================================\n")
    print(questao["enunciado"])

    input("\nPressione ENTER para ver a resposta...")

    print("\n📌 RESPOSTA:")
    print(questao["resposta"])

    while True:
        print("\nDeseja ver o passo a passo?")
        print("1 - Sim")
        print("0 - Voltar")
        escolha = input("Escolha: ")

        if escolha == "1":
            print("\n🧠 PASSO A PASSO:\n")
            print(questao["passo_a_passo"])
            input("\nPressione ENTER para voltar...")
            return

        elif escolha == "0":
            return

        else:
            print("❌ Opção inválida!")
