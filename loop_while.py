from time import sleep
'''DESAFIOS🥇'''



"""def contador (i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' *15)
    print(f'Contagem de {i} ate {f}.')
    sleep(1.5)
    if i < f:
        cont = i
        while cont  <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont -= p
        print('FIM!')
        #Programa principal:
contador(1, 120, 1)"""

# DESAFIO 1 - Crie um loop while que irá contar e imprimir no console de 1 até 120

contar = 1
while contar <= 120:
    print(f'{contar} ', end='')
    contar += 1

# DESAFIO 2 - Crie um loop while que irá continuamente pedir ao usuário a senha para entrada, 
# e só irá permitir o programa continuar caso ele digite a senha 'secreto'

senha = ''
while senha != 'secreto':
    senha = input('Digite sua senha: ')
print('BEM VINDO!') 

# DESAFIO 3 - Crie um loop que conte e imprima na tela o valor em ordem descrescente de 100 para 1

valor = 0
while valor <= 100:
    print(f'{valor} ', end='')
    valor += 1
    