from datetime import date

nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.')
if idade < 18:
    print(f'Faltam {18 - idade} anos para seu alistamento.')
elif idade == 18:
    print('Esse é o ano do seu alistamento!')
else: 
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
