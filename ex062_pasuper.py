print('Gerador de PA')
print('=-' * 10)

termo1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = termo1
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while  cont <= total:
        print(f'-> {termo}', end='')
        termo = termo + razao
        cont+=1
    
    print(' Pausa!')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print(f'FIM!Foram mostrados {total} termos nessa PA!')
