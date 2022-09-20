from math import hypot

cateto1 = float(input('Digite o valor do cateto oposto: '))
cateto2 = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(cateto1, cateto2)
print(f'{hipotenusa:.2f}')


"""FORMA MATEMATICA"""
""" cateto1 = float(input('Digite o valor do cateto oposto: '))
cateto2 = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = (cateto1**2 + cateto2 ** 2) ** (1/2)
print(hipotenusa) """