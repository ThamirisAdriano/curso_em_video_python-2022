print('-' * 30)
print('Lojinha! =)')
print('-' * 30)

contmaismil = soma = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    cont += 1
    if preco > 1000:
        contmaismil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
        #o bloco abaixo pode ser eliminado pois o comando se repete
    '''else:
        if preco < menor:
            menor = preco  
            barato = produto'''
    soma = soma + preco
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    
    if continuar == 'N':
        break
print(f'Fim do programa!')
print(f'O total da compra foi de R${soma}.')
print(f'Temos {contmaismil} produtos custando mais de R$1000,00.')
print(f'O produto mais barato é o {barato} que custa R$ {menor}.')
