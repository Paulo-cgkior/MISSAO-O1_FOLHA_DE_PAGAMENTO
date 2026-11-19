import os
os.system("cls")

def calcular_inss(valor_salario):
    if valor_salario <= 8475.55:
        inss = (valor_salario * 0.14)
        print(f"sua aliquota é 14%: {inss}")
    elif valor_salario <= 4354.27:
        inss = (valor_salario * 0.12)
        print(f"sua aliquota é 12%: {inss}")
    elif valor_salario <= 2902.84:
        inss = (valor_salario * 0.09)
        print(f"sua aliquota é 9%: {inss}")
    elif valor_salario <= 1621.84:
        inss = (valor_salario * 0.075)
        print(f"sua aliquota é 7,5%: {inss}")
    else:
        inss = valor_salario -  988.10
        print(f"sua aliquota é R$ 988.10: {inss}")
    return inss

valor_salario = float(input("Digite seu salario: "))


calcular_inss(valor_salario)