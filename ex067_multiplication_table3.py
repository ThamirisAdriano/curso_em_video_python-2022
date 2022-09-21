table = 0

while True:
    table = int(input('Quer ver a tabuada de qual valor? '))
    if table < 0:
        break
    for n in range(1,11):
        print(f'{table} X {n} = {table* n}')
print('Programa encerrado!') 
