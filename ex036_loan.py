casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Quantos anos de financiamento?: '))

prestacao = casa / (anos * 12)

if prestacao < (salario *30/100):
    print(f'Ok, a prestação da casa ficou em  R${prestacao:.2f} e é menor do que o seu salário de R${salario:.2f}')
else:
    print('Negado! O valor da prestação excede os 30% do seu salário')
