from funcao_primeiro import funcao_primeiro_grau
from funcao_segundo_grau import equacao_segundo_grau

escolha = int(input("""
- Escolha o tipo de calculo que deseja fazer - 
- 1 - Função de primeiro grau - 
- 2 - Função de segundo grau - 
- 3 - sair -
\nDigite sua escolha (1 ou 2): """))

match escolha:
    case 1:
        print("- 1 Função de primeiro grau:")
        a = int(input("Digite o valor de a: "))
        b = int(input("Digite o valor de b: "))
        funcao_primeiro_grau(a, b)
    case 2:
        print("- 2 Função de segundo grau:")
        a = int(input("Digite o valor de a: "))
        b = int(input("Digite o valor de b: "))
        c = int(input("Digite o valor de c: "))
        equacao_segundo_grau(a, b, c)
    case 3:
        print("Finalizando programa...")
    case _:
        print("Opção inválida")