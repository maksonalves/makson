#Faça um programa para determinar o número de dígitos de
#um número inteiro positivo informado.
while True:
    numero = int(input('Digite um número inteiro positivo: '))
    numero_digitos = len(str(numero))
    print(f'o numero {numero}, tem {numero_digitos - 1} digitos')
    if numero > 0:
        continue
    if numero <= 0:
        print('O número deve ser positivo!')
        continue
    if numero == 0:
        print('o numero é zero')

#Faça um programa para determinar o número de dígitos de'''