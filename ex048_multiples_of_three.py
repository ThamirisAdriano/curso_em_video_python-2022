soma = 0
c = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        c = c + 1
        print(soma)