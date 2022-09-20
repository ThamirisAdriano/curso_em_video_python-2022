#MINHA SOLUÇÃO

viagem = float(input('Qual a distância da sua viagem?'))
valor1 = viagem * 0.50
valor2 = viagem * 0.45

print(f'Você está prestes a iniciar uma viagem de {viagem} km')

if viagem <= 200:
    print(f'Sua viagem custará {valor1}')
else:
    print(f'Sua viagem custará {valor2}')

#SOLUÇÃO AULA

viagem = float(input('Qual a distância da sua viagem?'))
print(f'Você está prestes a iniciar uma viagem de {viagem} km')
if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45

print(f'O preço da sua passagem será de R${preco}.')

