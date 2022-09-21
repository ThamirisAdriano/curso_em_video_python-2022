num = cont = soma = 0
while True:
    num = int(input('Digite um valor, [999 para parar]: '))
    if num == 999:
        break
    cont = cont + 1
    soma = soma + num
print(f'Você digitou {cont} números e a soma foi de {soma}.')

