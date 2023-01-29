import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log',filemode='a', 
                    format='%(levelnames)s - %(message)s - %(acstime)s')
try:
    email = input('Digite seu e-mail: ')
    senha = int(input('Digite sua senha bancaria: '))
    if senha == '1234':
        #print('Welcome to your account!')
        logging.info(f'{email} entrou em sua conta bancaria.')
except ValueError as erro:
    print('Favor digitar apenas numeros.')
    logging.warning(erro)
        