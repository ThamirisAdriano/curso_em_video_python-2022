velocidade = int(input('Qual a velocidade do carro?:'))
multa = (velocidade - 80) * 7
if velocidade <80:
    print('Tudo certo! Tenha um bom dia e dirija com segurança!')
else:
    print(f'Você está acima da velocidade permitida, e foi multado em R${multa:.2f}')

print('Tenha um bom dia! Dirija com segurança!')