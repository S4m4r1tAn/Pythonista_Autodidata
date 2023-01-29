class Computador:
    sistema_operacinal = 'Windows 11'
    def __init__(self,marca,memoria_ram,placa_de_video): #abaixo, temos as propriedades das classes:
        self.marca = marca #são variáveis de uma instância
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    #criando a função ligar o computador
    def ligar(self):
        print('Estou ligando o Computador.')

Computador.sistema_operacinal = 'Windows 11'

computador1 = Computador('ACER_NITRO', '16gb' ,'AMD_RX6900')
computador1.marca = 'Asus'
print(computador1.marca)
print(computador1.sistema_operacinal)

Computador.sistema_operacinal = 'Mac_OS'
computador2 = Computador('LENOVO_LEGION', '32gb' ,'NVIDIA_RTX4090')
print(computador2.sistema_operacinal)
print(computador2.memoria_ram)
