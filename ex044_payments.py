valor = float(input('Valor das compras: '))
print('Forma de pagamento: ')
print('[1] à vista dinheiro ou cheque')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
opcao = int(input('Qual é a opção?: '))
if opcao == 1:
    saldo = valor *10 / 100 
    print(f'Valor da compra ficou em {valor - saldo:.2f}')
if opcao == 2:
    saldo = valor *5 / 100 
    print(f'Valor da compra ficou em {valor - saldo:.2f}')
elif opcao == 3:
    print(f'Valor da compra ficou em 2x de {valor / 2:.2f}')
elif opcao == 4:
    saldo = valor *20 /100 + valor
    print(f'Valor da compra ficou em {saldo:.2f} em 3x de {saldo / 3:.2f}')
