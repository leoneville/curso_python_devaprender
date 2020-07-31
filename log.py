# logging
import logging

logging.basicConfig(
    filename='information.log',
    level=logging.DEBUG,
    format='%(levelname)s %(asctime)s: %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'

)
logger = logging.StreamHandler()
logging.getLogger('').addHandler(logger)

logging.debug('Isso é uma mensagem de nível debug')
logging.info('Isso é uma mensagem de nível info')
logging.warning('Isso é uma mensagem de nível warning')
logging.error('Isso é uma mensagem de nível error')
logging.critical('Isso é uma mensagem de nível critical')