from calculadora import *
from funcoes import *

escolha = int(input("Digite uma das opções: \n"
                    "1 - calculadora\n"
                    "2 - carro\n"))

match escolha:
    case 1:
        calculadora = Calculadora()
    
    case 2:
        escolha = input("Quer montar o carro do zero?(s/n) ")
        if escolha == "s":
            nome = input("Digite o nome do carro: ")
            motor = float("Digite a quantidade de cilindrada: ")
            hibrido = input("O carro será hibrido: ")
            cor = input("Digite a cor do carro: ")
            portas = int(input("Digite a quantidade de portas: "))
            cambio = input("O carro será Manual ou Automatico? ")

            if hibrido == "sim":
                hibrido = True
            else:
                hibrido = False

            carro = Carro(nome, motor, hibrido, cor, portas, cambio)
        else:

            carro = Carro()