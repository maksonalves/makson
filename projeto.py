# SISTEMA FIFA DE CADASTRO
class Times :
    def __init__(self,nometime,cidadetime,mascotetime):
        self.nometime = nometime
        self.cidadetime = cidadetime
        self.mascotetime = mascotetime

class Jogadores:
    def __init__(self,nomejogador,numero,nometimejoga):
        self.nomejogador = nomejogador
        self.numerocamisa = numero
        self.nometimejoga = nometimejoga

class Comissao:
    def __init__(self,nome,time):
        self.nome = nome
        self.time = time

class Tecnico(Comissao):
    def __init__(self, nome, time, esquemat):
        super().__init__(nome, time)
        self.esquemat = esquemat

    def dar_coletiva(self):
        return f'O técnico está dando uma coletiva de imprensa'
        
class Auxiliar(Comissao):
    def __init__(self, nome, time, esquematx):
        super().__init__(nome, time)
        self.esquematx = esquematx
    

    def dar_coletiva(self):
        return ' O auxiliar está dando uma coletiva de imprensa'
    

class Preparador(Comissao):
    def __init__(self, nome, time,parte):
        super().__init__(nome, time)
        self.parte = parte

    def dar_coletiva(self):
        return 'O preparador está dando uma coletiva de imprensa '

while True:
    escolha = int(input('Bem vindo ao menu fifa ! \n'
                    '1 - Cadastrar novo time .\n'
                    '2 - Cadastrar novo jogador .\n'
                    '3 - Cadastrar comissão técnica\n'
                    '0 - Finalizar menu '))
    if escolha == 1:
        nometime = input("Digite o nome do time :")
        cidadetime = input("O time é de qual cidade ?")
        mascotetime = input("Qual o mascote do time ? ")
        times = Times(f"{nometime}",f'{cidadetime}',f'{mascotetime}')

    elif escolha == 2:
        nomejogador = input('Qual nome do jogador ? ')
        nometimejoga = input('Qual o time que o jogador atua ? ')
        numerocamisa = input('Qual numero do jogador ?')
        nomejogador1 = Jogadores(f"{nomejogador}",{numerocamisa},f'{nometimejoga}')
        
    elif escolha == 3:
        
        while True:
            escolha2 = int(input('1 - Cadastrar técnico ?\n'
                                '2 - Cadastrar auxiliar ?\n'
                                '3 - Cadastrar preparador ?\n'
                                '0 - Finalizar Cadastro da comissão.'))

            if escolha2 == 1:
                nometecnico = input('Qual o nome do técnico ?')
                timetreinador = input('Qual o time ele treina ?')
                esquemapreferidotec = input('Qual esquema tatico preferido ?')
                tec = Tecnico (f"{nometecnico}",f"{timetreinador}",f'{esquemapreferidotec}')
                coletiva = input("Deseja dar coletiva ? s/n")
                if coletiva == 's' :
                    print(tec.dar_coletiva())

            if escolha2 == 2:
                nomeauxiliar = input('Qual o nome do Auxiliar ?')
                timeaux = input('Qual time o auxiliar treina ?')
                esquemapreferidoaux = (input('Qual esquema tatico preferido ?'))
                aux = Auxiliar (f"{nomeauxiliar}",f"{timeaux}",f'{esquemapreferidoaux}')
                coletiva2 = input("Deseja dar coletiva ? s/n")
                if coletiva2 == 's' :
                    print(aux.dar_coletiva())

            if escolha2 == 3 :
                nomepreparador = input('Qual o nome do preparador ?')
                timepreparador = input('Qual time o preparador trabalha')
                partepreparo = input('Qual parte do time é preparado ? \n'
                                    'Jogadores de linha ?\n'
                                    'Goleiros ')
                prep = Preparador(f'{nomepreparador}',f'{timepreparador}',f'{partepreparo}')
                coletiva3 = input("Deseja dar coletiva ? s/n")
                if coletiva3== 's' :
                    print(prep.dar_coletiva())

            

            if escolha2 == 0:
                break
            
            
    elif escolha == 0:
        break
