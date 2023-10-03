num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

iguais = []
if num1 == num2:
    iguais.append(num1)
    iguais.append(num2)
if num1 == num3:
    iguais.append(num1)
    iguais.append(num3)
if num2 == num3:
    iguais.append(num2)
    iguais.append(num3)

print("O maior número é:", maior)
print("O menor número é:", menor)

if len(iguais) > 0:
    print("Existem números iguais:", iguais)
else:
    print("Não existem números iguais.")