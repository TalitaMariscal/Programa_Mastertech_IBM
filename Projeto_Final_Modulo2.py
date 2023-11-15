from datetime import datetime
from tabulate import tabulate
import sys

def verificar_maioridade(data_nascimento):
    idade = (datetime.now() - data_nascimento).days // 365
    if idade < 18:
        print("Cálculo negado, empréstimos são autorizados somente para maiores de 18 anos.")
        print ()
        return False
    return 18 <= idade <= 69

# Verifica se o requisitante trabalha
def situacao_empregaticia():
    print("Vamos agora para informações sobre a sua fonte de renda.")
    print("""Lembre-se que a fonte de renda deve ser comprovada com holerite,
comprovante de imposto de renda e/ou documentos comprovatórios assinados pelo contador.""")
    print()
    trabalha = int(input("""Atualmente, você possui forma de renda comprovada?
1 - Sim
2 - Não
Opção escolhida: """))
    print()
    if trabalha == 1:
        escolha_trabalho = int(input("""Qual é a sua fonte de renda?
1 - Empregado com carteira assinada
2 - Autônomo
3 - Aposentado/Pensionista
4 - Nenhuma das opções anteriores
Opção escolhida: """))
        print()
        if escolha_trabalho == 1:
            print("""Para trabalhadores que possuem carteira assinada, será necessária 
a apresentação de holerite ou carteira de trabalho para a finalização do empréstimo.""")
            print()
        elif escolha_trabalho == 2:
            print("""Para trabalhadores autônomos, será necessária a apresentação de 
comprovante de renda, podendo ser o comprovante de declaração de IRRF ou declaração 
emitida e assinada pelo contador responsável juntamente com o extrato bancário.""")
            print()
        elif escolha_trabalho == 3:
            print("""Para aposentados/pensionistas, será necessária a apresentação do 
número de beneficiário emitido pelo INSS.""")
            print()
        elif escolha_trabalho == 4:
            print("""Infelizmente não conseguiremos lhe atender por aqui. Pedimos a 
gentileza de se dirigir a um de nossos pontos de atendimento ou entrar em contato com 
nossa central no número 0800-0800800.""")
            print()           
            sys.exit()
        else:
            print("Você digitou a opção errada. Reinicie a sua solicitação.")
    elif trabalha == 2:
        print("""Infelizmente não conseguiremos prosseguir com a sua solicitação, pois 
para concessão de empréstimo é necessária a comprovação de renda.""")
        sys.exit()
    else:
        print("Você digitou a opção errada. Reinicie a sua solicitação.")

# Verifica quanto é 30% do valor da parcela 
def verificar_renda(valor_emprestimo, renda_cliente):
    
    trinta_porcento_salario = renda_cliente * 0.30
    for prazo in range(2, 61):
        valor_parcela = valor_emprestimo / prazo
        if valor_parcela <= trinta_porcento_salario:
            print(f"""Para a sua renda é permitida uma parcela máxima de R$ {trinta_porcento_salario:.2f}, 
podendo a partir deste valor de parcela seu empréstimo ser liberado. Verifique na tabela 
o valor mais adequado a sua necessidade.""")
            return True
    print("Infelizmente, não foi possível encontrar uma quantidade de parcelas viáveis com o valor desejado.")
    return False

def calcular_emprestimo(valor_emprestimo, renda_cliente):
    options = []
    for prazo in range(2, 61):  # Loop de 2 a 60 parcelas
        if prazo <= 12:
            taxa_juros = 0.020
        elif 24 >= prazo >= 13:
            taxa_juros = 0.015
        elif 36 >= prazo >= 25:
            taxa_juros = 0.010
        else:
            taxa_juros = 0.005

        valor_total = 0
        valor_parcela = valor_emprestimo * (1 + taxa_juros) ** prazo / prazo
        valor_total = (valor_parcela * prazo)

        options.append([f'R$ {valor_emprestimo:.2f}', prazo, f'R$ {valor_parcela:.2f}', f'R$ {valor_total:.2f}'])

    headers = ["Valor do Empréstimo", "Quantidade Parcelas", "Valor Parcela", "Valor Total a Pagar"]
    table = tabulate(options, headers=headers, tablefmt="pretty")
    print("\nOpções de Empréstimo de 2 a 90 parcelas:")
    print(table)

def iniciar_atendimento():
    print()
    print("-------------------------")
    print("Financeira DINDIN na Mão")
    print("-------------------------")
    print()
    print("Temos o maior prazer em lhe atender. Para darmos continuidade ao seu atendimento, favor nos informar:")
    print()
    instituicao = "Financeira DINDIN na Mão"
    nome = input("Digite o nome completo? (Sem abreviações) ")
    cpf = input("Digite o número do CPF? (Digite os 11 números sem traços ou espaços) ")

    tentativas = 0
    max_tentativas = 3
    data_nascimento = None

    while tentativas < max_tentativas:
        dig_nascimento = input("Qual a data de nascimento? (Digite somente números no formato DDMMAAAA) ")
        if len(dig_nascimento) == 8:
            day = dig_nascimento[:2]
            month = dig_nascimento[2:4]
            year = dig_nascimento[4:]
            data_nascimento = datetime.strptime(f"{day}/{month}/{year}", '%d/%m/%Y')
            print(f'Data de nascimento: {data_nascimento}')
            print()
            break
        else:
            print("Você digitou a data de nascimento no formato errado. Digite novamente no formato solicitado.")
            tentativas += 1
    if data_nascimento is None:
        print("Número máximo de tentativas atingido. Por favor, inicie outra solicitação.")
    return nome, data_nascimento

def processo_emprestimo():
    print ()

def processo_emprestimo():
    print ()
    nome, data_nascimento = iniciar_atendimento()
    if data_nascimento and verificar_maioridade(data_nascimento):
        situacao_empregaticia()
        valor_emprestimo_cliente = float(input("Digite o valor do empréstimo desejado: R$ "))
        renda_cliente = float(input("Digite o valor de sua renda mensal: R$ "))
        print()
        if verificar_renda(valor_emprestimo_cliente, renda_cliente):
            calcular_emprestimo(valor_emprestimo_cliente, renda_cliente)
    print()
    print(f"""Prezado(a) {nome}, para podermos continuar a sua solicitação de análise,
pedimos que escolha um de nossos canais de atendimento e nos encaminhe
cópia do RG, CPF, comprovante de residência e comprovação de renda.
E-mail: analise@dindinnamao.com.br
Whatsapp: 11 99999-9999
Central de relacionamento: 0800-0800800""")
    print()
    print ("Agradecemos o seu contato!")
    print()
    
processo_emprestimo()


