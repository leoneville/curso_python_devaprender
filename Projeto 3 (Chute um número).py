#Chute um número
"""
Objetivo: Chutar corretamente qual foi o número aleatório
que foi gerado dentro de um limite.
 Ex: Limite: entre 1 a 100, valor aleatorio gerado -> 73
 Seu programa deve:
 1. Definir qual é o valor mínimo e máximo que deve ser gerado
 2. Gerar um valor aleatorio que nao será exibido para o
 usuario, dentro do limite anterior(Recomendo criar uma função
 para isso)
 3. O usuario deve tentar chutar o valor que foi gerado (Recomendo
 criar uma funçao, onde você pede informaçao para o usuario e tambem valida
 se é realmente o número)
 4. Se o usuario acertar, voce deve mostrar alguma mensagem
 positiva para o usuario
 5. Se errar, mostrar para o usuario se ele chutou um valor menor
 ou maior que o valor aleatorio
 6. Continuar executando o programa ate que o usuario acerte
 """

import random

class Adivinhe_O_Numero:
    def __init__(self):
         self.valor_aleatorio = 0
         self.menor_valor = 0
         self.maior_valor = 100
         self.valor_chute = 0
    
    def Iniciar(self):
        self.valor_aleatorio = self.Gerar_Numero_Aleatorio()
        self.Chutar_O_Numero()
        while self.valor_chute != self.valor_aleatorio:
            if self.valor_chute < self.valor_aleatorio:
                print("Chute um valor maior...")
                self.Chutar_O_Numero()
            elif self.valor_chute > self.valor_aleatorio:
                print("Chute um valor menor...")
                self.Chutar_O_Numero()
        print("Parabéns, você acertou!!")


    def Gerar_Numero_Aleatorio(self):
        return random.randint(self.menor_valor, self.maior_valor)

    def Chutar_O_Numero(self):
        try:
            self.valor_chute = int(input("Chute um número de 0 a 100: "))
        except:
            print("Somente números inteiros são aceitos...")
            self.Chutar_O_Numero()

Chute_Um_Numero = Adivinhe_O_Numero()
Chute_Um_Numero.Iniciar() 


""" import random

numero = random.randint(1,100)
def Chutar_Numero():
    try:
        chute = int(input("Chute um número: "))
        while chute != numero:
            if chute < numero:
                print("Chute um numero maior...")
                chute = int(input("Chute um número: "))
            elif chute > numero:
                print("Chute um número menor...")
                chute = int(input("Chute um número: "))
    except:
        print("Somente números inteiros são aceitos...")
        Chutar_Numero()

def Acertou():
    print("Parabéns, você acertou !!")

        

Chutar_Numero()
Acertou() """
           