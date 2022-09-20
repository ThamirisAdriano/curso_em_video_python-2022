dias = int(input('Quantos dias alugados?: '))
km = float(input('Quantos Km rodados?: '))
preco_dias = dias * 60
preco_km = km * 0.15

print(f'O preço pelos dias foi de R${preco_dias} e pelos Kms rodados foi de R${preco_km}, sendo assim o total a pagar é de R${preco_dias + preco_km}')