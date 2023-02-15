import webbrowser
import threading
from time import sleep
import random

def extrair_dados_do_site(site):
    print(f'Estamos navegando ate o site {site}.')
    webbrowser.open_new(site)
    for i in range(1, 20):
        print(f'Processando dados - {i}/19.')
        sleep(1)
    print(f'Finalizando extracao de dados do site.')
    
def baixar_arquivos():
    for i in range(1, 10):
        print(f'Baixando arquivos - {i}/10.')
        sleep(1)    
    print('Arquivos baixados.')
        
nova_thread = threading.Thread(
    target=extrair_dados_do_site, args=('https:devaprender.com',), daemon=True)
nova_thread.start()
baixar_arquivos()
nova_thread.join()
        
# THREADS PARA DADOS EM MASSA.
def comentar(site, comentario):
    print(f'Entrando no site: {site}')
    print(f'Deixando um comentario {comentario}')
cometarios = ['oi', 'ola', 'gostei', 'curti', 'muito bom', 'show de bola']
threads = []
for site in range(6):
    nova_thread = threading.Thread(target=comentar, args=(site,random.choice(cometarios)))
    threads.append(nova_thread)
    
for thread in threads:
    thread.start()
    print(f'Iniciando {thread.name}')
    
for thread in threads:
    thread.join()
    print(f'Finalizando {thread.name}')
    