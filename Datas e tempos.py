#Datas e tempos
from datetime import datetime

""" print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

print(datetime(2020,1,25))

data_postagem_foto = datetime.strptime(input('Quando devemos postar essa foto? '), '%d/%m/%Y')
print(type(data_postagem_foto))
 """
""" data_inicio = datetime.now()
data_entrega = datetime(2020,11,18)

prazo_entrega = data_entrega - data_inicio
print(prazo_entrega) """

#Desafio quanto tempo falta até o seu aniversario

tempo_atual = datetime.now()
proximo_niver = datetime(2021,1,21)

restante_dias = proximo_niver - tempo_atual
print(restante_dias)