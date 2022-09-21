from random import randint
vitoria = 0
print('=-' * 20)
print('Vamos jogar Par ou Ímpar:')
print('=-' * 20)

while True:
    num = int(input('Digite um valor: '))
    pc = randint(0,9)
    total = num + pc
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('[P/I]?: ')).upper().strip()[0]
    print(f'Você jogou {num} e o pc {pc}. Total de {total}.')
    print('Deu par' if total % 2 ==0 else 'Deu Ímpar!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            vitoria +=1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você Venceu!')   
        else:
            print('Você Perdeu!') 
            break
    print('Vamos jogar novamente!...')
print(f'Game Over! Você venceu {vitoria} vezes!')

    
