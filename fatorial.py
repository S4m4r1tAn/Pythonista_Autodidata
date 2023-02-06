n = int(input('Digite um numero INTEIRO E POSITIVO: '))
while n > 0:
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    print = (f'O fatorial de {n} eh igual a {fatorial}.')
    n = int(input('Digite um numero INTEIRO E POSITIVO: '))