import threading
from time import sleep
    
# THREADS PARA DADOS EM MASSA.
def extrair_precos(site, produto, preco):
    print(f'Entrando no \033[33;1m{site}\033[m e pesquisando sobre \033[30;41;1;4m{produto}\033[m.')
    sleep(5)
    print(f'O PRECO DO ITEM: \033[30;46;1;4m{produto}\033[m FOI PROCESSADO COM SUCESSO!')
    print(f'O \033[30;46;1;4m{produto}\033[m CUSTA \033[32;43;1m{preco}\033[m.')

threads = []
produtos = ['CELULAR', 'MONITOR', 'FONE DE OUVIDO', 'ALTO-FALANTE', 'COMPUTADOR']
precos = ['£1350,00', '£325,00','£89,00','£175,00', '£3890,00']
for i in range(5):
    nova_thread = threading.Thread(
        target=extrair_precos, args=('https://best.aliexpress.com', produtos[i], precos[i]))
    threads.append(nova_thread)
    
for thread in threads:
    thread.start()
    #print(f'Iniciando {thread.name}')
    
for thread in threads:
    thread.join()
    #print(f'Finalizando {thread.name}') """ """
    