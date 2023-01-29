from datetime import datetime

def decorator(funcao):
    def tempo():
        print(datetime.now())
        funcao()
        print(datetime.now())
    return tempo

@decorator   
def shazam():
    print('O tempo eh relativo!')
    
shazam()