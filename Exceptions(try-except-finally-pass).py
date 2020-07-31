# Exceptions
""" try:
    ano_atual = int(input('Qual é o ano atual? '))
except ValueError:
    print('Você deve digitar um número.') """

""" try:
    print(5/0)
except ZeroDivisionError:
    print('Não é possivel dividir por 0.') """

""" try:
    print(5/0)
except:
    print('Ocorreu um erro') """



""" try:
    print(5/0)
except:
    print('ocorreu um erro')
finally:
    print('usuario X realizou calculos no sistema.') """

for pagina in range(10):
    try:
        print('Buscando informaçoes')
        print(5/0)
    except:
        pass