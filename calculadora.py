class Calculadora:
    def __init__(self):
        while True:
            escolha = int(input("Digite uma das opções:\n"
                                "1 - Soma\n"
                                "2 - Subtração\n"
                                "0 - Finalizar\n"))
            
            match escolha:
                case 1:
                    self.soma()

                case 2:
                    self.subtracao()
                
                case 0:
                    break

                case _:
                    print("Opção inexistente")

    def soma(self):
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))

        print(f"O valor da soma é {n1 + n2}")

    
    def subtracao(self):
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))

        print(f"O valor da subtração é {n1 - n2}")
