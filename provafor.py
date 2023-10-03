pessoas = []

for i in range(5):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M/F): ")
    
    pessoa = {"nome": nome, "idade": idade, "sexo": sexo}
    pessoas.append(pessoa)

idades = [pessoa["idade"] for pessoa in pessoas]
media_idade = sum(idades) / len(idades)

pessoa_mais_velha = max(pessoas, key=lambda x: x["idade"])
nome_pessoa_mais_velha = pessoa_mais_velha["nome"]

menores_de_20 = len([pessoa for pessoa in pessoas if pessoa["idade"] < 20])
maiores_de_40 = len([pessoa for pessoa in pessoas if pessoa["idade"] > 40])

sexos = [pessoa["sexo"] for pessoa in pessoas]
sexo_mais_frequente = max(set(sexos), key=sexos.count)

print(f"Média de idade do grupo: {media_idade}")
print(f"Nome da pessoa mais velha: {nome_pessoa_mais_velha}")
print(f"Número de pessoas com menos de 20 anos: {menores_de_20}")
print(f"Número de pessoas com mais de 40 anos: {maiores_de_40}")
print(f"Sexo mais frequente: {sexo_mais_frequente}")
