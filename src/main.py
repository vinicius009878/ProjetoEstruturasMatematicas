from funcoes.funcaografico1 import funcao_primeiro_grau
from funcoes.funcaografico2 import equacao_segundo_grau
from funcoes.x_y_vertice import calcular_vertice

from time import sleep
import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    while True:
        limpar_tela()
        print(
            """
    === MENU PRINCIPAL ===

    1 - Função de 1º Grau (com gráfico)
    2 - Função de 2º Grau (com gráfico)
    3 - Calcular Xv e Yv
    0 - Sair
        """
        )

        try:
            escolha = int(input("Digite sua escolha: "))
        except ValueError:
            print("⚠ Entrada inválida. Digite apenas números.")
            sleep(1.5)
            continue

        match escolha:
            case 1:
                limpar_tela()
                print("--- Função de 1º Grau ---\n")
                a = float(input("Digite o valor de a: "))
                b = float(input("Digite o valor de b: "))
                funcao_primeiro_grau(a, b)
                input("\nPressione Enter para voltar ao menu...")

            case 2:
                limpar_tela()
                print("--- Função de 2º Grau ---\n")
                a = float(input("Digite o valor de a: "))
                b = float(input("Digite o valor de b: "))
                c = float(input("Digite o valor de c: "))
                equacao_segundo_grau(a, b, c)
                input("\nPressione Enter para voltar ao menu...")

            case 3:
                limpar_tela()
                print("--- Calcular Xv e Yv ---\n")
                calcular_vertice()
                input("\nPressione Enter para voltar ao menu...")

            case 0:
                print("Finalizando programa...")
                sleep(1)
                break

            case _:
                print("⚠ Opção inválida! Tente novamente.")
                sleep(1.5)


if __name__ == "__main__":
    menu()
