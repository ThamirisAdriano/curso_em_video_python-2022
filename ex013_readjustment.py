salario = float(input('Qual é o salário do funcionário? R$'))
aumento = int(input('Qual o aumento? %'))
aumento1 = salario * aumento / 100
salariofinal = salario + aumento1
print(f'Um funcionário que recebia R${salario:.2f}, com o aumento de {aumento}% passou a receber R${salariofinal:.2f}')