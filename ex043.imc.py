peso = float(input('Qual é o seu peso? (Kg): '))
altura = float(input('Qual é a sua altura? (m): '))

imc = peso / (altura ** 2 )

if imc < 18.5:
    print(f'IMC {imc:.1f} Abaixo do peso!')
elif imc >= 18.5 and imc <=24.9:
    print(f'IMC {imc:.1f} Normal!')
elif imc >= 25 and imc <= 29.9:
    print(f'IMC {imc:.1f} Sobrepeso!')
elif imc >= 30:
    print('Obesidade!')