num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[ 1 ] conevrter para BINÁRIO ')
print('[ 2 ] conevrter para OCTAL ')
print('[ 3 ] conevrter para HEXADECIMAL ')
opcao = int(input('Sua opção: '))

if num == 1 : 
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif num ==2 :
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
else:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}') 
