#Decida por mim
"""Objetivo: Seu programa deve permitir que o usuario
faça uma pergunta pra o programa, seu programa
deve exibir na tela que está pensando(isso
deve tomar alguns segundos) e depois o programa
deve responder o usuario, dentro de 10 possibilidades
que voce criou para ele. Depois de exibir a resposta,
você deve perguntar ao usuario se ele quer fazer
outra pergunta. Caso ele responda positivamente
rode o programa novamente e continue rodando desde
que o usuario responda positivamente. Caso ele
responda um não ou negativamente, finalize o
programa e deixe uma mensagem agradecendo o usuario 
por usar seu programa """

# Conceitos que podem ser usados:
#   Random
#   Listas
#   Classes
#   Funçoes
#   Print

import random
import time

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
        "Você tem certeza que quer fazer isso?", 
        "Acho que sim ...", 
        "Acho que não ...", 
        "Talvez sim...", 
        "Talvez não...", 
        "Sim!", "Não!", 
        "Não faço a mínima ideia!!", 
        "Acho que deveria perguntar isso pra outro!", 
        "Não sei, nem quero saber e tenho raiva de quem sabe!!"
        ]

    def Iniciar(self):
        self.FazerPergunta()
        self.Escolha()

    def FazerPergunta(self):
        pergunta = input("Qual é sua dúvida? ")
        print("pensando...")
        time.sleep(5)
        print(random.choice(self.respostas))
    

    def Escolha(self):
        fazer_outra_pergunta = input("Gostaria de fazer outra pergunta? ").lower()
        if fazer_outra_pergunta == "sim" or fazer_outra_pergunta == "s":
            self.Iniciar()
        elif fazer_outra_pergunta == "não" or fazer_outra_pergunta == "nao" or fazer_outra_pergunta == "n":
            print("Obrigado por usar este programa! ^^,")
        else:
            print("Favor digitar apenas 'sim' ou 'nao'")
            self.Escolha()

start = DecidaPorMim()
start.Iniciar()


