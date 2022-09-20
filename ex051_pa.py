
print(20*'=')
print('10 TERMOS DE UMA PA')
print(20*'=')
termo1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo1 + (10-1) * razao #enesimo termo de uma PA
for n in range(termo1, decimo + razao, razao):
    print(n, end=('-> '))
print('ACABOU')