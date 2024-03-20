nome = input('Qual o seu nome?')
print(f'Seu nome é: {nome}')

nome2 = input('Qual o seu nome2?')
print(f'Seu nome2 é: {nome2=}')


numero_1 = input('Digite um numero: ')
numero_2 = input('Digite outro numero: ')

if numero_1.isnumeric() and numero_2.isnumeric():
    print(int(numero_1) + int(numero_2))
else:
    print('O valor digitado não é um número')
