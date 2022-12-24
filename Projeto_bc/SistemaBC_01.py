menu = """"
===============
1 - DEPOSITAR
2 - SACAR
3 - EXTRATO
4 - SAIR
================

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

    opção = input(menu)

    if opção == '1':
        valor=float(input("Digite o valor que deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito:R$ {valor:.2f}\n"
        else:
            print(" Operação falhou, valor inválido")

    elif opção == '2':

        valor=float(input("Digite o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print('Operação falhou você não tem saldo suficiente')

        elif excedeu_limite:
             print('Operação falhou valor acima do limite') 

        elif  excedeu_saques:
                print('Operação falhou você excedeu o número de daques diários') 

        elif valor > 0:
            saldo -= valor
            extrato += ('Saque: R$ {:.2f}'.format(valor))
            numero_saques +=1

        else:
            print(' Operação falhou, o valor informado é inválido!!')

    elif opção == "3":
         print("\n =================== EXTRATO ===================")
         print('Não foram realizadas operações.' if not extrato else extrato)
         print(f'\nSaldo:  R$ {saldo:.2f}')
         print('==================================================')
    
    elif opção == "4":
        break

    else:
        print('Opção inválida, selecione novamente uma opção válida')
