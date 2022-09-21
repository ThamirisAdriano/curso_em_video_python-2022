cont = media = soma = maior = menor = 0
sequencia = 'S'

while sequencia == 'S':
    num = int(input('Digite um número: '))
    soma += num
    cont = cont + 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    sequencia = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

media = soma / cont
print(f'Você digitou {cont} numeros e a média foi de {media}, o maior número foi {maior} e o menor número foi {menor}.')
