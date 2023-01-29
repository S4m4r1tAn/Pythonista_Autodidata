from abc import ABC, abstractmethod

class Monitor(ABC):
    @abstractmethod
    def aumentar_claridade(self, quantidade):
        pass
    @abstractmethod
    def diminuir_claridade(self, quantidade):
        pass

class MonitorFullHD(Monitor):
    def aumentar_claridade(self, quantidade):
        print('**' *17)
        print(f'Aumentando a claridade em {quantidade} pontos.')
    def diminuir_claridade(self, quantidade):
        print(f'Diminuindo a claridade em {quantidade} pontos.')
        print('**' *17)
    
monitor = MonitorFullHD()
monitor.aumentar_claridade(5)
monitor.diminuir_claridade(5)
