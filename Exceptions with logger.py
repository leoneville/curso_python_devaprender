# Exceptions
import logging

logging.basicConfig(
    filename="info.log",
    level=logging.DEBUG,
    format="%(levelname)s %(asctime)s: %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",

)
logger = logging.StreamHandler()
logging.getLogger('').addHandler(logger)

try:
    ano_atual = int(input('Qual é o ano atual? '))
except ValueError:
    logging.warning('Você deve digitar um número.')

try:
    print(5/0)
except ZeroDivisionError:
    logging.warning('Não é possivel dividir por 0.')

try:
    print(5/0)
except:
    logging.warning('Ocorreu um erro')



try:
    print(5/0)
except:
    logging.warning('ocorreu um erro')
finally:
    logging.info('usuario X realizou calculos no sistema.')

""" for pagina in range(10):
    try:
        print('Buscando informaçoes')
        print(5/0)
    except:
        pass """