import logging
'''
debug: passar informacoes para os desenvolvedores.
info: informar algo que esta acontecendo na aplicacao, mas nao eh um erro.
warning: ALERTAR sobre algo que esta acontecendo na aplicacao, mas ainda nao eh um erro.
error: um erro aconteceu na aplicacao.
critical: erro com concequencias graves aconteceu na aplicacao.
'''
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a', format='%(levelname)s - %(message)s')
logging.debug('Logging no nivel debug.')
logging.info('Logging no nivel info.')
logging.warning('Logging no nivel warning.')
logging.error('Logging no nivel error.')
logging.critical('Logging no nivel critical.')
