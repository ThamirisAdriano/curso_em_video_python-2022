salario = float(input('Qual o salário do funcionário?'))
if salario <= 1250:
    aumento = (salario * 15/ 100) 
    salario1 = aumento + salario
if salario >1250:
    aumento = (salario * 10/100)
    salario1 = aumento + salario
print(f'O funcionário que recebia R${salario} passará a receber R${salario1}')