# Tomando Decisoes (if else)
#if
#elif
#else

#se ela chegar antes das 8: 'Loja Fechada'
#se ela chegar depois das 18: 'Loja Fechada'
#qualquer outro horario: 'Volte outro horario'

#horario_chegada = int(input("Digite o horario da sua chegada: "))

""" if horario_chegada < 8:
    print('loja ainda não abriu')
elif horario_chegada > 18:
    print('Loja ja fechou')
else:
    print("Volte outro horario") """

#Cenario realista

""" if horario_chegada >= 8 and horario_chegada <= 12:
    print("Loja está aberta")
elif horario_chegada >= 14 and horario_chegada <= 18:
    print("Loja está aberta")
else:
    print("Loja está fechada") """

#Desafio !!
#Desafio 1
#Você tem uma lista de pessoas aprovadas para entrar no evento
#Essas pessoas são josé, marcos, camilla



""" nome = str(input("Digite o seu nome para entrar na festa: "))
if nome == "José" or nome == "josé" or nome == "Marcos" or nome == "marcos" or nome == "Camille" or nome == "camille":
    print("Seu nome está na lista... Pode entrar !!")
else:
    print("Seu nome não está na lista... Vá embora !!") """

#nomes = ["José", "josé", "Marcos", "marcos", "Camille", "camille"]

""" for nome in nomes:
    print(nome) """

#def pertence(nome, nomes):
'''(objeto, list) -> bool

Recebe uma lista de itens e um item e
retorna True se o item eh um elemento da lista e
False em caso contrario.
'''
#    print("Vixe! Ainda nao fiz a funcao!")


#teste
nomes = ["José", "josé", "Marcos", "marcos", "Camille", "camille"]
print("Verifique se seu nome está na lista para entrar na festa")
nome = str(input("Diga qual o seu nome: "))

if nome in nomes:
    print('Seu nome está na lista... Se diverta na festa !!')
else:
    print('Seu nome não está na lista... Vá embora !!')


