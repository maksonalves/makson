class Carro:
    """
    Classe que representa um carro.

    Atributos:
    - nome (str): nome do carro
    - motor (float): tamanho do motor em litros
    - hibrido (bool): indica se o carro é híbrido ou não
    - cor (str): cor do carro
    - portas (int): número de portas do carro
    - cambio (str): tipo de câmbio do carro (manual ou automático)
    """

    def __init__(self,nome="carro", motor=1.0, hibrido=False, cor="Preto", portas=2, cambio="Manual"):
        self.nome = nome
        self.motor = motor
        self.hibrido = hibrido
        self.cor = cor
        self.portas = portas
        self.cambio = cambio

    def acelerar(self):
        """
        Método que acelera o carro.
        """
        print(f"Acelerando o {self.nome}")

    def frear(self):
        """
        Método que freia o carro.
        """
        print("Freando...")
    
    def re(self):
        """
        Método que coloca o carro em marcha ré.
        """
        print("Ré...")
    



