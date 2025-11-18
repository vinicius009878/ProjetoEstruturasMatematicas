import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


def calcular_vertice():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    xv = -b / (2 * a)
    yv = a * xv**2 + b * xv + c
    print(f"Xv = {xv}")
    print(f"Yv = {yv}")


if __name__ == "__main__":
    calcular_vertice()
