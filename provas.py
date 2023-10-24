#Faça um programa em python que determine em duas variáveis (senha e email) e que
#contenha uma senha e um email cadastrados antecipadamente, em seguida solicite ao
#usuário uma senha e um email e utilize o laço de repetição juntamente com a estrutura
#de condição para verificar se o email e a senha digitado pelo usuário é igual ao email
#e senha cadastrados antecipadamente. E enquanto a senha e o email que o usuário digitou 
#não for igual ao email esenha cadastrados ele continue em um loop.

email_cadastrado = "exemplo@gmail.com"

senha_cadastrada = "123456"

while True:
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    if email == email_cadastrado and senha == senha_cadastrada:
        print("Login efetuado com sucesso!")
        break

    else:
        print("Email ou senha incorreto! tente novamente")
        continue
