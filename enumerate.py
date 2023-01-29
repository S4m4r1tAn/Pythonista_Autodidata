frutas = ['Apple', 'Orange', 'Strowberry', 'Lime']

for indice, fruta in enumerate(frutas, 1):
    if indice == 3:
        print(f'A fruta {fruta} na posicao {indice} esta EM PROMOCAO, aproveite!')
    else:
        print(indice, fruta)
        