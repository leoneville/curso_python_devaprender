# Break
#estilos_musicas = ['rock', 'pop', 'hip-hop', 'rap']
# Rodar até que ele encontre o estilo musical "Hip-Hop"
""" for estilo in estilos_musicas:
    if estilo == 'hip-hop':
        break
    print(estilo) """


""" estilos_musicas = ['rock', 'pop', 'hip-hop', 'rap']
for estilo in estilos_musicas:
    if estilo == 'pop':
        continue
    print(estilo) """

# DESAFIO !!!
# Desafio 1
""" Crie uma lista precos. depois crie um laço que exibe 
os valores na tela até que ele chegue no valor que você
está buscando. Quando ele encontrar o valor que você está
buscando ele deve sair do laço e imprimir 'encontramos o valor
desejado' """

# Desafio 2
""" Crie uma lista de sites. O seu laço deve passar sobre todos
os sites porem quando encontrar um determinado site 
(voce ira determinar qual site é esse) ele deve simplismente
pular este site e imprimir na tela: 'Site "nome do site" foi pulado """

precos = [22.50, 35.60, 44.72, 25.50, 10.40, 200.50, 36.90, 45.70]

for preco in precos:
    if preco == 200.50:
        break
    print(preco)


print(f'Encontramos o valor desejado: {preco}')

sites = ['www.facebook.com', 'www.instagram.com', 'www.roadsec.com', 'web.whatsapp.com', 'www.youtube.com']

for site in sites:
    if site == 'web.whatsapp.com':
        print(f'O site {site} foi pulado' )
        continue
    print(site)