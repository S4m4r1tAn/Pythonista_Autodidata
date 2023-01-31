#Criando os Métodos de uma classe --> Ligar, desligar, exibir dados do computador
class Computador:
    def __init__(self,marca,memoria_ram,placa_de_video): #abaixo, temos as propriedades das classes:
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    #criando a função ligar o computador
    def ligar(self):
        print('Estou ligando o Computador.')
    #criando a função desligar o computador
    def deligar(self):
        print('Estou desligando o Computador.')
    #criando uma função exibindo dados do computador
    def exibir_dados_computador(self):
        print(f'Computador da marca {self.marca}, com {self.memoria_ram} de memória ram e que usa a placa de vídeo {self.placa_de_video}.')

#após ter a classe "computador" e as "funções", podemos utilizar quantas vezes forem necessárias:
computador1 = Computador('ACER_NITRO', '16gb' ,'AMD_RX6900')
computador1.ligar()
computador1.deligar()
computador1.exibir_dados_computador()
 
computador2 = Computador('LENOVO_LEGION', '32gb' ,'NVIDIA_RTX4090')
computador2.ligar()
computador2.deligar()
computador2.exibir_dados_computador()
 