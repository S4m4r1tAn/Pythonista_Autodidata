import time
import threading
 
""" Gostaria de uma ajuda neste código. Estou treinando e pensei em criar como se fosse um jogo, onde a thread 
que esteja responsável pelo relógio pudesse controlar a thread do 'jogo', fazendo para a thread caso o tempo
finalize. Como disse, estou treinando e não sei se isto seria possível. Desde já, agradeço!"""
 
jogo = [i for i in range(15)]
stop_flag = False
def jogando(jogo):
    for i in jogo:
        print(f'Você está jogando {i}', end="\r")
        time.sleep(1)
    while not stop_flag.is_set():
        if stop_flag:
            stop_flag.set()
            break
 
def temporizador(tempo):
    if tempo == 'f' or 'F' or 'Facil' or 'facil':
        tempo = 60
    elif tempo == 'm' or 'M' or 'Medio' or 'medio':
        tempo = 30
    elif tempo == 'd' or 'D' or 'dificil' or 'Dificil':
        tempo = 10
    else:
        print('\033[0;30;41mOPCAO INVALIDA\033[m, digite uma opcao valida: ')
 
    while tempo >= 0:
        print('TEMPO...'   '{:02d}'.format(tempo).center(50), end="\r")
        time.sleep(1)
        tempo-=1
        if tempo == 0:
            print('VOCE PERDEU! '.center(50))
tempo = input('Selecione a dificuldade do jogo: Facil -> f | Medio -> m | Dificil -> d: ')
stop_flag = threading.Event()
t = threading.Thread(target=jogando, args=(jogo,))
t1 = threading.Thread(target=temporizador, args=tempo,)
t.start()
t.join()
t1.start()
t1.join()
stop_flag.set()
