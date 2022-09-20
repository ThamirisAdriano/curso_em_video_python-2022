
from re import A

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulhernova = 0

for p in range(1,5):
    print(f'------{p}ª PESSOA------')
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    somaidade = somaidade + idade
    mediaidade = somaidade / 2

    if p ==1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo =='M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo == 'F' and idade < 20:
        mulhernova = mulhernova + 1

print(f'A média de idade do grupo é de {mediaidade}')
print(f'O homem mais velho é o {nomevelho} com {maioridadehomem} anos.')
print(f'No grupo temos {mulhernova} mulheres com menos de 20 anos')