from datetime import date

hoje = date.today().year
maior = 0
menor = 0
for p in range(1,7):
    ano = int(input(f'Em que ano a {p}ª pessoa nasceu?: '))
    if hoje - ano >= 18:
        maior = maior +1
    else:
        menor = menor +1

print(f'Ao todo tivemos {maior} pessoas maiores de idade e {menor} menores de idade.')