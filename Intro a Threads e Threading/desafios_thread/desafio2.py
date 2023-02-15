import threading
from time import sleep
    
# THREADS PARA DADOS EM MASSA.
def extrair_precos(site, produto):
    print(f'Entrando no \033[33;1m{site}\033[m e pesquisando sobre \033[30;41;1;4m{produto}\033[m.')
    sleep(5)
    print(f'O ITEM: \033[30;46;1;4m{produto}\033[m FOI PROCESSADO COM SUCESSO!')

threads = []
produtos = ['CELULAR', 'MONITOR', 'FONE DE OUVIDO', 'ALTO-FALANTE', 'COMPUTADOR']
for i in range(5):
    nova_thread = threading.Thread(
        target=extrair_precos, args=('https://best.aliexpress.com', produtos[i]))
    threads.append(nova_thread)
    
for thread in threads:
    thread.start()
    #print(f'Iniciando {thread.name}')
    
for thread in threads:
    thread.join()
    #print(f'Finalizando {thread.name}') """ """
    