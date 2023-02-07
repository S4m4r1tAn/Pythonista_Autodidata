while True:
    valor = input('Digite um numero: ')
    
    try:
        valor = float(valor)
    except ValueError:
        if not valor:
            print('Digitar um valor.')
            continue
        print('Favor digitar apenas numeros.')
        continue
    
    resultado = valor * 5.07
    print(f'O resultado do calculo eh {resultado}!')
    break
