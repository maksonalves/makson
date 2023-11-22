class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        self.quantidade_combustivel -= litros_abastecidos
        return litros_abastecidos

    def abastecer_por_litro(self, litros):
        valor_pagar = litros * self.valor_litro
        self.quantidade_combustivel -= litros
        return valor_pagar

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor

    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade

bomba1 = BombaCombustivel("Gasolina", 4.5, 1000)
bomba2 = BombaCombustivel("Etanol", 3.8, 800)

litros_abastecidos = bomba1.abastecer_por_valor(50)
print(f"Foram abastecidos {litros_abastecidos} litros de {bomba1.tipo_combustivel}")

valor_pagar = bomba2.abastecer_por_litro(30)
print(f"O valor a ser pago pelo cliente é de R${valor_pagar}")

bomba1.alterar_valor(4.8)
bomba2.alterar_combustivel("Gasolina Aditivada")
bomba1.alterar_quantidade_combustivel(900)