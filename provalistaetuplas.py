#Faça um programa que solicite ao usuário que digite 10 valores para
#preencher uma lista. Em seguida, o programa deve separar os números
#pares e ímpares em listas diferentes. Por fim, exiba na tela os números pares,
#os números ímpares em uma tupla, a quantidade de números pares e ímpares presentes
#na lista, e a soma de todos os números pares e ímpares, respectivamente.

lista = []

for i in range(10):
    lista.append(int(input("Digite um número: ")))

pares = []

impares = []

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(pares)

print(impares)

print(len(pares))

print(len(impares))

print(sum(pares))

print(sum(impares))