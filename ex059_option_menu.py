num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    print('[ 1 somar] ')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    opcao = int(input('>>>> Qual é sua opção?: '))
    if opcao ==1:
        print(f'{num1 + num2}')
    elif opcao ==2:
        print(f'{num1 * num2}')
    elif opcao ==3:
        if num1 > num2:
            print(f'O número maior é {num1}')
        else:
            print(f'O número maior é {num2}')       
    elif opcao ==4:
        print('Informe os números novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Fim do programa!')

