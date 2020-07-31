# Class
#Syntaxe

# Marca, Memoria Ram, Placa de video
class computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    

    def ligar(self):
        print('estou ligando')


    def desligar(self):
        print('estou desligando')

    
    def ExibirInformacoesDesteComputador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)


computador1 = computador('Asus', '16Gb', 'Nvidia')
computador1.ligar()
computador1.desligar()
computador1.ExibirInformacoesDesteComputador()

    



# Ligar, Desligar, Exibir Configuraçoes



""" computador1 = computador('Asus', '8Gb', 'Nvidia')
computador2 = computador('Dell', '16Gb', 'Intel Graphics')
computador3 = computador('HP', '32Gb', 'Radeon')
print(computador1.marca, computador1.memoria_ram, computador1.placa_de_video)
print(computador2.marca, computador2.memoria_ram, computador2.placa_de_video)
print(computador3.marca, computador3.memoria_ram, computador3.placa_de_video) """

# DESAFIO !!!
# DESAFIO 1
""" Você irá criar a class carro e eu quero no minimo
3 propriedades para a classe carro e no minimo 3 metodos
para ela. """

# Propriedades: Marca, Modelo, Ano, Porte(Grande, medio, pequeno)
 
class carro:
    def __init__(self, marca, modelo, ano, porte):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.porte = porte

    
    def ligar(self):
        print('Ligando o carro')


    def acelerar(self):
        print('Acelerando o carro')


    def freiar(self):
        print('Freiando o carro')

    
    def desligar(self):
        print('Desligando o carro')


    def DetalhesDoCarro(self):
        print(self.marca, self.modelo, self.ano, self.porte)


carros = carro('Hyundai', 'HB20', '2014', 'Médio')
carros.ligar()
carros.acelerar()
carros.freiar()
carros.desligar()
carros.DetalhesDoCarro()
