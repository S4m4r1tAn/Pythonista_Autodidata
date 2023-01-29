def processamento_de_audio(aumentando_volume=None, diminuindo_volume=None):
    if aumentando_volume != None:
        print(f'Aumentando o volume.')
    elif diminuindo_volume != None:
        print(f'Dminuindo o volume.')
    else:
        print(f'DESLIGANDO!')
        
volume_maximo = 10
volume_minimo = 0

class Audio:
    pass
