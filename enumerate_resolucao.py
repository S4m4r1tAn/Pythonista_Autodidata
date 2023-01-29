frutas = ['Apple', 'Orange', 'Strowberry', 'Lime']

for indice, fruta in enumerate(frutas, 1):
    if indice == 3:
        print(f'{indice} {fruta} -> EM PROMOCAO!')
    else:
        print(indice, fruta)
        