num = int(input('Digite um número para calcular o fatorial: '))
f = 1
c = num
for c in range(num, 0, -1):  #solução com FOR
    print(f'{c} ', end=' ')
    print('x ' if c > 1 else '=', end=' ')
    f = f * c
    c = c -1
print(f)
   

#solução com while
"""num = int(input('Digite um número para calcular o fatorial: '))
f = 1
c = num
while c > 0: 
    print(f'{c} ', end=' ')
    print('x ' if c > 1 else '=', end=' ')
    f = f * c
    c = c -1
print(f)"""