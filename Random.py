# Random
""" 
1. Voce quer simular a opçao de jogar uma moeda em cara ou coroa
2. Voce quer fazer um sorteio entre 300 nomes em uma lista de nomes
3. Voce quer escolher aleatoriamente um numero de 10-100
4. Voce quer escolher uma carta aleatoriamente dentro de um baralho
5. Voce quer gerar nomes de usuario aleatoriamente
6. Voce quer gerar senhas seguras"""

import random

""" print(random.random())# Valor aleatorio de 0.0 ate 1.0
print(random.uniform(4,10))# Valor decimal do minimo ao maximo que voce passar pra ele
print(random.randint(12,55)) # valor inteiro do minimo ao maximo

cores = ["verde", "vermelho", "azul"]
print(random.choice(cores)) # Escolher uma opçao dentro de uma lista

cartas_de_um_baralho = ["cartas1", "cartas2", "cartas3", "cartas4", "cartas5"]
random.shuffle(cartas_de_um_baralho) #altera a ordem dos itens da lista aleatoriamente
print(cartas_de_um_baralho) """

# DESAFIO
# Desafios Random

"""
1.Você quer simular a opção de jogar uma moeda e resultar
em cara ou coroa
    Jogue as opçoes dentro de uma variavel e depois crie um
    programa que imprime 'cara' ou 'coroa' na tela 

2. Você quer fazer um sorteio entre 5 nomes em uma lista de nomes:
    Crie uma lista de 5 nomes e sorteie um nome de dentro dessa lista
    e exiba na tela.  

3. Você quer escolher aleatoriamente um número de 10-100
    Imprima na tela um valor aleatório entre 10 e 100
"""

#Desafio 1

escolha = ["cara", "coroa"]
print(random.choice(escolha))

#Desafio 2
lista_nomes = ["Neville", "Laís", "Nichollas", "Melissa", "Amanda"]
print(random.choice(lista_nomes))

#Desafio 3
print(random.randint(10,100))
