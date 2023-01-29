import logging
 
#logging.basicConfig(level=logging.DEBUG, filename='app.log',filemode='a', format='%(levelnames)s - %(message)s')
while True:
    try:
        email = '<devaprender@python.com>'
        senha = int(input('Senha: '))
        if senha == 1234:
            print(f'Login feito com sucesso no e-mail {email}.')
            break
        elif senha != 1234:
            print('Senha incorreta, tente novamente!')
        
    
    except ValueError as erro:
    
        print('Digite apenas numeros.')
 