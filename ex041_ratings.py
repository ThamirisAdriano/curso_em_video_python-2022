from datetime import date

ano = int(input('Ano de Nascimento: '))
hoje = date.today().year
idade = hoje - ano

if idade <= 9:
    print(f'Atleta tem {idade} anos. Classificação: Mirim')
elif idade > 9 and idade <= 14:
    print(f'Atleta tem {idade} anos. Classificação: Infantil')
elif idade >14 and idade <=19:
     print(f'Atleta tem {idade} anos. Classificação: Junior')
elif idade > 19 and idade <=25:
    print(f'Atleta tem {idade} anos. Classificação: Sênior')
else:
    print(f'Atleta tem {idade} anos. Classificação: Master')