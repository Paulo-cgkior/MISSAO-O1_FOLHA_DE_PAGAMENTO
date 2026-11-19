import os

# Variaveis
usuario = "Paulo"
senha = "609"
tentativas = 0
vale_refeicao = 500.00

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
            resposta_vale_transporte = "O usuário aceita o vale-transporte"
            break
        elif opcao_transporte_yn == "n":
            resposta_vale_transporte = "O usuário não aceita o vale transporte"
            break
        else:
            print("Alternativa invalida, digite apenas Y ou N")
            input("Aperte Enter para continuar...")
    return resposta_vale_transporte
def vale_refeicao():
    while True:
        os.system("cls")
        print("=== Vale-refeicao ===")
        opcao_refeicao_yn = str(input("\nDigite S se deseja vale-refeição e N caso contrário: ")).lower()
        if opcao_refeicao_yn == "s":
            resposta_vale_refeicao = "O usuário aceita o vale-refeição"
            break
        elif opcao_refeicao_yn == "n":
            resposta_vale_refeicao = "O usuário não aceita o vale-refeição"
            break
        else:
            print("Alternativa invalida, digite apenas Y ou N")
            input("Aperte Enter para continuar...")
    return resposta_vale_refeicao
def dependentes():
    while True:
        os.system("cls")
        print("=== Dependentes ===")
        escolha_dependentes_yn = str(input("\nDigite S se você tem dependentes e N caso contrário: ")).lower()
        if escolha_dependentes_yn == "s":
            resposta_dependentes = "s"
            quantidade_dependentes = int(input("Quantos?: "))
            if quantidade_dependentes <= 0:
                print("Número menor que 1")
                input("Aperte enter para continuar...")
            else:
                break
        elif escolha_dependentes_yn == "n":
            quantidade_dependentes = 0
            resposta_dependentes = "n"
            break
        else:
            print("Escolha inválida")
            input("Digite enter para continuar...")
    return resposta_dependentes, quantidade_dependentes
#Funções dos cálculos
def calcular_inss(valor_salario):
    if valor_salario <= 1621.84:
        inss = (valor_salario * 0.075)
        print(f"sua aliquota é 7,5%: {inss}")
    elif valor_salario <= 2902.84:
        inss = (valor_salario * 0.09) - 1621.84
        print(f"sua aliquota é 9%: {inss}")
    elif valor_salario <= 4354.27:
        inss = (valor_salario * 0.12) - 2902.84
        print(f"sua aliquota é 12%: {inss}")
    elif valor_salario <= 8475.55:
        inss = (valor_salario * 0.14) - 4354.27
        print(f"sua aliquota é 14%: {inss}")
    else:
        inss = valor_salario - 988.10
        print(f"sua aliquota é R$ 988.10: {inss}")
    return inss
def calcular_irrf(valor_salario, inss, quantidade_dependentes):
    base = valor_salario - inss - (189.59 * quantidade_dependentes)
    if base <= 2428.80:
        imposto = base
    elif base <= 2826.65:
        imposto = (base * 0.075) - 182.16
    elif base <= 3751.05:
        imposto = (base * 0.15) - 394.16
    elif base <= 4664.68:
        imposto = (base * 0.225) - 675.49
    else:
        imposto = (base * 0.275) - 908.73
    
    if valor_salario <= 5000.00:
        irrf = 0
    elif valor_salario <= 7350.00:
        irrf = (imposto - 978.62) - (0,133145 * valor_salario)
    else:
        irrf = imposto
    return irrf
def calcular_vale_transporte(valor_salario, resposta_vale_transporte):
    if resposta_vale_transporte == "s":
        valor_vale_transporte = valor_salario * 0.06
    elif resposta_vale_transporte == "n":
        valor_vale_transporte = 0
    return valor_vale_transporte
def calcular_vale_refeicao(vale_refeicao, resposta_vale_refeicao):
    if resposta_vale_refeicao == "s":
        valor__vale_refeicao = vale_refeicao * 0.20
    elif resposta_vale_refeicao == "n":
        valor__vale_refeicao = 0
    return valor__vale_refeicao
def calcular_plano_saude(resposta_dependentes, quantidade_dependentes):
    if resposta_dependentes == "s":
        valor_plano_saude = 150.00 * quantidade_dependentes
    elif resposta_dependentes == "n":
        valor_plano_saude = 150
    return valor_plano_saude
def salario_liquido(valor_salario, inss, irrs, valor_vale_transporte, valor_vale_refeicao, valor_plano_saude):
    total_desconto = inss + irrs + valor_vale_transporte + valor_vale_refeicao + valor_plano_saude
    salario_liquido = valor_salario - total_desconto
    return salario_liquido
# Login
resultado = login(usuario, senha, tentativas)
print(f"Seu login teve o {resultado}")

# Quatro perguntas
salario()
vale_transporte()
vale_refeicao() 
dependentes()

#Atribuindo as perguntas
inss = calcular_inss(valor_salario)


print("\n" + "=" * 45)
print(f"CONTRACHEQUE • MATRÍCULA {usuario}")
print("=" * 45)
print(f"Salário base              R$ {inss}")
print("-" * 45)
print(f"(-) INSS                  R$ ")
print(f"(-) IRRF                  R$ ")
print(f"(-) Vale-transporte       R$ ")
print(f"(-) Escolha: {...}")
print(f"(-) Vale-refeição         R$ ")
print(f"(-) Escolha: {...}")
print(f"(-) Plano de saúde        R$ ")
print("-" * 45)
print(f"Total de descontos        R$ ")
print(f"SALÁRIO LÍQUIDO           R$ ")
print("=" * 45 + "\n")
#falta somar a faixa salarial do irrf eu acho
