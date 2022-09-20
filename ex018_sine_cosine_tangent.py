import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O angulo de {angulo} tem o SENO de {seno:.2f}, o COSSENO de  {cosseno:.2f}, e a TANGENTE{tangente:.2f}')
