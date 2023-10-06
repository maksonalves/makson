'''class Carro:
    motor = 0.0
    hibrido = False
    cor = ""
    portas = 0
    cambioalt = False'''

'''class Carro:
    def __init__(self, motor, hibrido, cor, portas, cambioalt):
        self.motor = motor
        self.hibrido = hibrido
        self.cor = cor
        self.portas = portas
        self.cambioalt = cambioalt

    def acelerar(self):
        print('acelerar...')
    def frear(self):
        print('frear...')
    def re(self):
        print('re...')

onix = Carro(1.0, False, "preto", 4, "manual")

print(onix.motor, onix.cor)
'''
'''class Carro:
#Atributos:
#    - nome (str): nome do carro
#    - motor (float): tamanho do motor em litros
#    - hibrido (bool): indica se o carro é híbrido ou não
#    - cor (str): cor do carro
#    - portas (int): número de portas do carro
#    - cambio (str): tipo de câmbio do carro (manual ou automático)
#    """    
    def __init__(self,nome="carro", motor=1.0, hibrido=False, cor="Preto", portas=2, cambio="Manual"):
        self.nome = nome
        self.motor = motor
        self.hibrido = hibrido
        self.cor = cor
        self.portas = portas
        self.cambio = cambio

    def acelerar(self):
        print(f"Acelerando o {self.nome}")

    def frear(self):
        print("Freando...")
    
    def re(self):
        print("Ré...")
    

onix = Carro(nome="onix", cambio="Automatico")

print(onix.nome)
print(onix.motor)
print(onix.hibrido)
print(onix.cor)
print(onix.portas)
print(onix.cambio)'''
'''
class Calculadora:
    def __init__(self):
        while True:
            escolha = int(input("Digite uma das opções:\n"
                                "1 - Soma\n"
                                "2 - Subtração\n"
                                "0 - Finalizar"))
            
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

calculadora = Calculadora()'''


#Crie uma classe chamada Fatura que possa ser utilizada por uma loja de
#suprimentos de informática para representar uma fatura de um item
#vendido na loja. Uma fatura deve incluir as seguintes informações como
#atributos:

#o nome do item;
#o preço unitário do item;
#quantidade de item a ser faturado;
#valor total da fatura;


#Sua classe deve ter um construtor que inicialize todos os atributos menos o
#valor total da fatura. Além disso, forneça um método chamado
#gerar_fatura que calcula o valor da fatura (isto é, multiplicar a quantidade
#pelo preço por item).

class fatura:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.total = quantidade * preco 
    
    def gerar_fatura(self):
        self.total = self.quantidade * self.preco
        return (f'fatura do item {self.nome}\n'
                f'preço: {self.preco}\n'
                f'quantidade: {self.quantidade}\n'
                f'valor total: {self.total}')
Fatura = fatura('TECLADO MECANICO', 250.00, 2)

print(Fatura.gerar_fatura())

