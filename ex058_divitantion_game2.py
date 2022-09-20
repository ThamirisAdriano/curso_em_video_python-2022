from random import randint
num = randint(0,11)
tentativa = 0
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10')
#MINHA SOLUÇÃO
"""palpite = int(input('Diga seu palpite: '))
while palpite < num:
    palpite = int(input('Mais, tente mais uma vez: '))
    tentativa = tentativa + 1
while palpite > num:
    palpite = int(input('Menos, tente mais uma vez: '))
    tentativa = tentativa + 1
if palpite == num:
    print(f'Acertou! O número era {num} e vc acertou com {tentativa} tentativas.')"""

#SOLUÇÃO DO VÍDEO
acertou = False
while not acertou:
    jogador = int(input('Diga seu palpite: '))
    tentativa +=1
    if jogador == num:
        acertou = True
    else:
        if jogador < num:
            print('Mais, tente mais uma vez: ')
        elif jogador > num:
            print('Menos, tente mais uma vez: ')


print(f'Acertou! O número era {num} e vc acertou com {tentativa} tentativas.')