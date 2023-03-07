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
    
    resultado = valor * 3.141592643

#Veja mais sobre "Número pi (π)" em: https://brasilescola.uol.com.br/matematica/numero-pi.htm
    print(f'O resultado do calculo eh {resultado:.4f}!')
    break
