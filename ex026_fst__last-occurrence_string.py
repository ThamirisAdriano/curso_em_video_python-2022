frase = str(input('Digite uma frase:')).strip().upper()
contagem = frase.count('A')
procure = frase.find('A')
procure2 = frase.rfind('A')

print(f'A letra A aparece {contagem} vezes na frase.')
print(f'A primeira letra A apareceu na posição {procure+1}')
print(f'A última letra A apareceu na posição {procure2+1}')
