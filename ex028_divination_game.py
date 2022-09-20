from random import randint

print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' *20)
num1 = randint(0,5)
num = int(input('Em que número eu pensei?: '))
print('PROCESSANDO...')
if num1 == num:
    print('Congratulations!')
else:
    print(f'YOU LOST!! O número que eu pensei foi: {num1}')