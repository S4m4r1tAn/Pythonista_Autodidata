while True:
    try:    
        idade = int(input('Qual a sua idade: '))
        if idade < 18:
            print(f'Eu sou menor de idade, tenho apenas {idade} anos.')
        elif idade >= 18:
            print(f'Tenho {idade} anos e sou maior de idade.')
            break
    except ValueError as error:
        print('Digite apenas numeros.')
    except TypeError as error:
        print('Digite apenas numeros.')
        