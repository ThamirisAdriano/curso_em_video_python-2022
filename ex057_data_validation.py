sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while 'M' not in sexo:
    sexo = str(input('Dado inválido, digite corretamente: ')).strip().upper()[0]
print('Sexo M registrado com sucesso.')