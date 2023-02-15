import webbrowser
import threading
from time import sleep

def extrair_fotos_do_site(site):
    print(f'\033[0;30;41mEstamos navegando ate o site:\033[m \033[0;33;1m{site}\033[m \033[0;30;41mpara baixar algumas fotos.\033[m')
    webbrowser.open_new(site)
        #print(f'Processando dados - {i}/19.')
    sleep(0.5)
    #print(f'Finalizando extracao de dados do site.')
    
def baixar_fotos(site):
    print(f'ESTAMOS PROCESSANDO AS FOTOS NO SITE \033[0;33;1m{site}\033[m.')
    webbrowser.open_new(site)
    sleep(0.5)
    print(f'PREPARANDO AS FOTOS...')
    sleep(1)
    print(f'LOADING AS FOTOS...')
    sleep(3)    
    print(f'BAIXANDO AS FOTOS...')
    sleep(3)    
    print(f'\033[1;33mFOTOS BAIXADAS COM SUCESSO!\033[m')                                                                                                                  
        
nova_thread = threading.Thread(
    target=extrair_fotos_do_site, args=('https://github.com/S4m4r1tAn/S4m4r1t4n',), daemon=True)
nova_thread.start()
baixar_fotos('https://github.com/S4m4r1tAn/S4m4r1t4n')
nova_thread.join()
