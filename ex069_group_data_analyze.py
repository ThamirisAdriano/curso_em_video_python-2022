print('-=' * 20)
print('Cadastre uma pessoa: ')
print('-=' * 20)

mais18 = homem = mulhernova = 0

while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        mais18 += 1
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        homem = homem + 1
    elif sexo == 'F' and idade < 20:
        mulhernova = mulhernova +1
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {homem} homem cadastrados.')
print(f'E temos {mulhernova} mulheres com menos de 20 anos.')