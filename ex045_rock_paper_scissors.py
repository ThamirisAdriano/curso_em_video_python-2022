from random import randint
from time import sleep

i = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
print('Suas opções: ')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
jogador = int(input('Qual é a sua jogada?: '))
print('JO')
sleep(.5)
print('KEN')
sleep(.5)
print('PO!')
print('-=' * 11)
print('Você escolheu {}.'.format(i[jogador]))
print('PC escolheu {}.'.format(i[pc]))
print('-=' * 11)

if pc ==0:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Você venceu!')
    elif jogador ==2:
        print('PC venceu!')
elif pc ==1:
    if jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Você venceu!')
    elif jogador ==0:
        print('PC venceu!')
elif pc ==2:
    if jogador == 2:
        print('Empate!')
    elif jogador == 0:
        print('Você venceu!')
    elif jogador ==1:
        print('PC venceu!')