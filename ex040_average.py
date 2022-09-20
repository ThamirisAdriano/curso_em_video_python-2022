nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))

media = (nota1 + nota2) / 2 

if media <=5:
    print(f'Média {media:.1f} aluno reprovado!')
elif media >5 and media < 6.9:
    print(f'Média {media:.1f} aluno de recuperação!')
else:
    print(f'Média {media:.1f} aluno aprovado!')
