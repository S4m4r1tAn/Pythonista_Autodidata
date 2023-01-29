def processamento_de_audio(aumentar_volume=None, diminuir_volume=None):
    """ print(f'Aumentar volume.')
    print(f'Diminuir volume.') """
    
    if aumentar_volume != None:
        print(f'Aumentando o volume.')
    elif diminuir_volume != None:
        print(f'Dminuindo o volume.')
    else:
        print(f'DESLIGANDO!')
        
        
volume_maximo = 10
volume_minimo = 0

class Audio:
    pass
