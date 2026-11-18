import os

# Variaveis
usuario = "Briar"
senha = "069"
tentativas = 0

# Funções das regras
def login(usuario, senha, tentativas):
    while True:
        os.system("cls")
        usuario_digitado = input("Digite o nome do usuario: ")
        senha_digitada = input("Digite a senha do usuario: ")
        if usuario_digitado == usuario and senha_digitada == senha:
            resultado = "Acesso liberado"
            break
        else:
            tentativas += 1
            print("Bad ending")
            if tentativas == 3:
                resultado = "Acesso bloqueado"
                exit()
            else:
                print(f"Tentativas restantes: {3 - tentativas}")
                input("Aperte enter para continuar...")
    return resultado
def salario():
    while True:
        os.system("cls")
        print("=== Salário ===")
        valor_salario = float(input("\nDigite o salário base: "))
        if valor_salario <= 0:
            print("Valor do salário incorreto")
            print("Valor do salário precisa ser maior que R$ 0")
            input("Aperte enter para continuar... ")
        else:
            print ("Valor do salário correto")
            break
    return valor_salario
def vale_transporte():
    while True:
        os.system("cls")
        print("=== Vale-transporte ===")
        opcao_transporte_yn = str(input("\nDigite S se deseja vale-transporte e N caso contrário: ")).lower()
        if opcao_transporte_yn == "s":
            print("O usuário aceita o vale-transporte")
            break
        elif opcao_transporte_yn == "n":
            print ("O usuário não aceita o vale transporte")
            break
        else:
            print("Alternativa invalida, digite apenas Y ou N")
            input("Aperte Enter para continuar...")
def vale_refeicao():
    while True:
        os.system("cls")
        print("=== Vale-refeicao ===")
        opcao_refeicao_yn = str(input("\nDigite S se deseja vale-refeição e N caso contrário: ")).lower()
        if opcao_refeicao_yn == "s":
            valor_refeicao = float(input("Digite o valor do vale-refeição: "))
            print(f"O valor do vale-refeição é: {valor_refeicao}")
            print("O usuário aceita o vale-refeição")
            break
        elif opcao_refeicao_yn == "n":
            print ("O usuário não aceita o vale-refeição")
            break
        else:
            print("Alternativa invalida, digite apenas Y ou N")
            input("Aperte Enter para continuar...")
    return valor_refeicao
def dependentes():
    while True:
        os.system("cls")
        print("=== Dependentes ===")
        escolha_dependentes_yn = str(input("\nDigite S se você tem dependentes e N caso contrário: ")).lower()
        if escolha_dependentes_yn == "s":
            opcao_dependentes = int(input("Se sim quantos?: "))
            if opcao_dependentes <= 0:
                print("Número menor que 1")
                input("Aperte enter para continuar...")
            else:
                print(f"Você tem: {opcao_dependentes} dependentes")
                break
        elif escolha_dependentes_yn == "n":
            print("")
            break
        else:
            print("Escolha inválida")
            input("Digite enter para continuar...")

#Funções dos cálculos
def calcular_inss(valor_salario):
    if valor_salario <= 8475.55:
        inss = valor_salario * 0.14
        print(f"sua aliquota é 14%: {inss}")
    elif valor_salario <= 4354.27:
        inss = valor_salario * 0.12
        print(f"sua aliquota é 12%: {inss}")
    elif valor_salario <= 2902.84:
        inss = valor_salario * 0.09
        print(f"sua aliquota é 9%: {inss}")
    elif valor_salario <= 2902.84:
        inss = valor_salario * 0.075
        print(f"sua aliquota é 7,5%: {inss}")
    else:
        inss = valor_salario -  988.10
        print(f"sua aliquota é R$ 988.10: {inss}")
# Login
resultado = login(usuario, senha, tentativas)
print(f"Seu login teve o {resultado}")

# Quatro perguntas
salario()
vale_transporte()
vale_refeicao()
dependentes()


#falta somar a faixa salarial 