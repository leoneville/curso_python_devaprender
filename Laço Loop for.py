# Laço/Loop for
'''
for nome_da_variavel_temporaria in quantas_vezes:
    fazer_algo_aqui_dentro
'''
# Quando o programa descobre a quantidade por você
""" lista = ['Manga', 'Arroz', 'Feijao', 'Carne', 'Verduras', 'Legumes']
for item in lista:
    print(item) """

# Você ja sabe a quantidade de vezes que deve rodar
# Função range roda até o penúltimo número
""" for volume in range(11):
    print(f'Aumentando o volume para {volume}')
 """
# Começa a contar a partir do número que você colocou
for volume in range (1,11):
    print(f'Aumentando o volume para {volume}')

# Desafio !!
# Desafio 1

""" Exiba na tela usando o loop todas as palavras que tiverem
dentro de uma lista. Voce pode colocar dentro dessa lista
o nome dos objetos que voce mais usa em sua casa,
a quantidade de nomes fica a seu criterio. Lembrando que
você nao deve especificar aqui a quantidade para o loop,
deixe que ele descubra. """

nomes = ["Neville", "lais", "Amanda", "Nichollas", "FELIPE", "Olaf", "Zilean", "TimeKiller"]

for nome in nomes:
    print(nome.upper())

#Desafio 2
""" Você precisa de 10 passos para finalizar uma tarefa.
Imprima na tela: "Executando passo 1" até "Executando passo 10"
usando laço for """

for i in range(1,11):
    print(f'Executando passo {i}')
