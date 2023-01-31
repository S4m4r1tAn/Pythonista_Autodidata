from abc import ABC, abstractmethod

class Carro(ABC):
    @abstractmethod
    def numero_de_rodas(self, quantidade):
        pass
    @abstractmethod
    def quantidade_de_portas(self, quantidade):
        pass
    
class Carrosseria(Carro):
    def numero_de_rodas(self, quantidade):
        print('**' *26)
        print(f'A quantidade de rodas  solicitada pelo cliente eh {quantidade}.')
    def quantidade_de_portas(self, quantidade):
        print(f'A quantidade de portas solicitada pelo cliente eh {quantidade}.')
        print('**' *26)
        
detalhe = Carrosseria()
detalhe.numero_de_rodas(4)
detalhe.quantidade_de_portas(2)
