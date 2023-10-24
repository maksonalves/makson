#Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números
#de matrícula usando um dicionário.
#O programa deve fornecer as seguintes funcionalidades:
#Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.
#Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.
#Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário,
#exibindo seus respectivos números de matrícula.
#O programa deve ser executado em um loop contínuo até que o usuário escolha sair.

dicionario = {}

while True:
    print("Selecione uma opção:")
    print("1 - Adicionar aluno")
    print("2 - Remover aluno")
    print("3 - Visualizar todos os alunos")
    print("4 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite o número de matrícula do aluno: ")
        dicionario[matricula] = nome
        print("Aluno adicionado com sucesso!")

    elif opcao == "2":
        matricula = input("Digite o número de matrícula do aluno a ser removido: ")
        if matricula in dicionario:
            del dicionario[matricula]
            print("Aluno removido com sucesso!")
        else:
            print("Aluno não encontrado!")

    elif opcao == "3":
        if len(dicionario) == 0:
            print("Não há alunos registrados.")
        else:
            print("Lista de alunos:")
            for matricula, nome in dicionario.items():
                print(f"Nome: {nome} - Matrícula: {matricula}")

    elif opcao == "4":
        print(f'programa encerrado')
        break

    else:
        print("Opção inválida!")