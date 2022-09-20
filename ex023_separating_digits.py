nome = str(input('Digite seu nome completo: ')).strip()
mai = nome.upper()
min = nome.lower()
tam = len(nome)
contagem = nome.count(' ')
separa = nome.split()

print('Analisando seu nome...')
print(f'Seu nome em LETRAS MAIÚSCULAS é {mai}')
print(f'Seu nome em letras minúsculas é {min}')
#print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) #conta quantas letras tem até o primeiro espaço.
print(f'Seu nome tem ao todo {tam - contagem} ')
print(f'Seu primeiro nome é {separa[0]}')