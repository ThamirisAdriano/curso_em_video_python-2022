print(20*'=')
print('10 TERMOS DE UMA PA 2.0')
print(20*'=')
termo1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = termo1
cont = 1
while cont < 11:
    print(f'-> {termo}', end='')
    termo = termo + razao
    cont+=1
    
print(' ACABOU!')

"""for n in range(termo1, decimo + razao, razao):
    print(n, end=('-> '))"""