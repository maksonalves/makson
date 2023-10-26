def adicionar_produto(lista, total_produtos):
    produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    valor_unitario = float(input("Digite o valor unitário do produto: "))

    total_produto = quantidade * valor_unitario

    novo_produto = {
        "produto": produto,
        "valor": valor_unitario,
        "quantidade": quantidade,
        "total": total_produto
    }

    lista.append(novo_produto)
    total_produtos += total_produto

    print("Produto adicionado com sucesso!")

    return total_produtos


def exibir_lista(lista, total_produtos):
    print("\nLista de Produtos:")
    for produto in lista:
        print(f"Produto: {produto['produto']}")
        print(f"Valor Unitário: R${produto['valor']:.2f}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Total: R${produto['total']:.2f}\n")

    print(f"Valor Total de todos os produtos: R${total_produtos:.2f}")


def atualizar_produto(lista, total_produtos):
    nome_produto = input("Digite o nome do produto que deseja atualizar: ")

    for produto in lista:
        if produto["produto"] == nome_produto:
            novo_nome = input("Digite o novo nome do produto: ")
            nova_quantidade = int(input("Digite a nova quantidade do produto: "))
            novo_valor = float(input("Digite o novo valor unitário do produto: "))

            produto["produto"] = novo_nome
            produto["quantidade"] = nova_quantidade
            produto["valor"] = novo_valor

            produto["total"] = nova_quantidade * novo_valor

            total_produtos = calcular_total(lista)

            print("Produto atualizado com sucesso!")
            return total_produtos

    print("Produto não encontrado na lista.")
    return total_produtos


def remover_produto(lista, total_produtos):
    nome_produto = input("Digite o nome do produto que deseja remover: ")

    for produto in lista:
        if produto["produto"] == nome_produto:
            total_produtos -= produto["total"]
            lista.remove(produto)

            print("Produto removido com sucesso!")
            return total_produtos

    print("Produto não encontrado na lista.")
    return total_produtos


def calcular_total(lista):
    total = 0
    for produto in lista:
        total += produto["total"]
    return total


def main():
    lista_produtos = []
    totalProdutos = 0

    while True:
        print("\nOpções:")
        print("1 - Adicionar produtos")
        print("2 - Ver a lista de produtos")
        print("3 - Atualizar produtos")
        print("4 - Remover produto")
        print("5 - Encerrar programa")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            totalProdutos = adicionar_produto(lista_produtos, totalProdutos)

        elif opcao == 2:
            exibir_lista(lista_produtos, totalProdutos)

        elif opcao == 3:
            totalProdutos = atualizar_produto(lista_produtos, totalProdutos)

        elif opcao == 4:
            totalProdutos = remover_produto(lista_produtos, totalProdutos)

        elif opcao == 5:
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Digite novamente.")


if __name__ == "__main__":
    main()
