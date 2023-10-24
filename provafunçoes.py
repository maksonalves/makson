#Desenvolva um programa em Python que permita ao usuário digitar várias notas.
#Em seguida, crie uma função chamada "calcular_media" que irá receber as notas 
#digitadas e calcular a média do aluno. Também crie uma função chamada "verificar
#situacao" que, com base na média calculada, irá exibir a situação do aluno: 
#"Reprovado" se a média for menor que 7, "Aprovado" se a média for maior ou igual a 7,
#e "Parabéns, sua média é 10" se a média for igual a 10.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

def calcular_media(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    return media

def situacao(media):
    if media < 7:
        return "Reprovado"
    elif media >= 7:
        return "Aprovado"
    else:
        return "Parabéns, sua média é 10"

media = calcular_media(nota1, nota2, nota3, nota4)

situacao = situacao(media)

print(f"Sua média é {media:.1f} e sua situação é {situacao}")   

