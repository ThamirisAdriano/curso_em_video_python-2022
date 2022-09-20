preco = float(input('QUal o preço do produto? R$ '))
desconto = float(input('Insira o desconto: '))
desconto_calc = preco * desconto / 100
preco_final = preco - desconto_calc
print(f'O produto que custava R${preco:.2f}, na promoção com o desconto de {desconto:.0f} % , custará R${preco_final:.2f}.')