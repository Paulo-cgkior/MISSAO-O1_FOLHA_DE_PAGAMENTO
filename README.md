# MISSAO-O1_FOLHA_DE_PAGAMENTO

#3 vale-transporte
while True:
    vale_transporte = str(input("\nDigite Y caso aceite vale transporte ou N caso contrarío"))
    if salario_base <= 0:
        print("Valor do salário incorreto")
        print("Valor do salário precisa ser maior que 0")
        input("Aperte enter para continuar... ")
    else:
        print("Valor do salário correto")
        break

#3 Vale-refeição
while True:
    vale_refeicao = float(input("\nDigite o salário base: "))
    eif salario_base <= 0:
        print("Valor do salário incorreto")
        print("Valor do salário precisa ser maior que 0")
        input("Aperte enter para continuar... ")
    else:
        print("Valor do salário correto")
        break

#3 Dependentes
while True:
    Dependentes = int(input("\nDigite o salário base: "))
    if salario_base <= 0:
        print("Valor do salário incorreto")
        print("Valor do salário precisa ser maior que 0")
        input("Aperte enter para continuar... ")
    else:
        print("Valor do salário correto")
        break