menu = '''
Menu:
d) depositar
s) sacar
e) extrato
q) sair
Enter option: '''

saldo = 0
limite = 500
extrato = ''
numero_de_saques = 0
LIMITES_DE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == 'd':
        print('Depósito')
        deposito = float(input('Qual a quantia: '))
        if deposito < 0:
            print('Valor inválido')
            continue
        saldo += deposito
        print(f'Saldo é de R$ {saldo:.2f}')
        extrato += f'Deposito de: R$ {deposito} '

    elif opcao == 's':
        print('Saque')
        numero_de_saques += 1
        valor_saque = float(input('Valor a sacar: '))

        if valor_saque > 500:
            print('Valor excede o limite de saque')
            continue

        if numero_de_saques > LIMITES_DE_SAQUES:
            print('Limite de saques excedido')
            continue

        if valor_saque >= saldo + limite:
            print('Saldo insuficiente')
            continue

        if valor_saque <= saldo + limite:
            saldo -= valor_saque
            print(f'Seu saldo é de R$ {saldo:.2f}')
            extrato += f' Saque de : R$ {valor_saque}'
        print(f'Seu número de saques foi {numero_de_saques} o máximo são 3')

    elif opcao == 'e':
        print('Extrato')
        print('\n===========Extrato Bancário============')
        print('Não foram realizadas transações' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('=========================================')


    elif opcao == 'q':
        break

    else:
        print('Operação invalida')
