#Simulador de Dado
""" 
Objetivo:
Seu programa deve: Gerar um número aleatorio entre 1 e 6
(ou qualquer outro valor minimo ou maximo) e exibir na tela.
Depois disso você deve perguntar o usuário se ele quer
rodar o dado novamente. Casoele diga que sim, gere e exiba
um valor novo. Caso o usuário não responda com as respostas
validas, mostre na tela quais sao as respostas validas e
pergunte novamente se ele gostaria de rodar o dado novamente.
 """

import random

class Simulador_De_Dados:
    def __init__(self):
        self.menor_valor = 1
        self.maior_valor = 6

    def Iniciar(self):
        self.Jogar_Dado()
        self.Jogar_Novamente()

    def Jogar_Dado(self):
        print(random.randint(self.menor_valor, self.maior_valor))

    def Jogar_Novamente(self):
        resposta = input("Deseja rolar o dado novamente: ").lower()
        if resposta == "sim" or resposta == "s":
            self.Iniciar()
        elif resposta == "não" or resposta == "nao" or resposta == "n":
            print("Obrigado por ter usado este aplicativo ^^,")
        else:
            print("Resposta Invalida... Responda apenas com Sim ou Não")
            self.Jogar_Novamente()

Rolar_Dados = Simulador_De_Dados()
Rolar_Dados.Iniciar()