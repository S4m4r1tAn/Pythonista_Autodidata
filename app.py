from processamento_de_audio import aumentar_volume, diminuir_volume, volume_maximo, volume_minimo, Audio

def iniciar_gravacao():
    print(f'Iniciar gravacao.')
    
aumentar_volume()
print(volume_maximo)
diminuir_volume()
print(volume_minimo)
audio = Audio()
