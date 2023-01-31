print('\n**** Apresendendo sobre Classes. ****\n') #criando Classes
#criando uma classe:
class Computador:
    def __init__(self,marca,memoria_ram,placa_de_video): #abaixo, temos as propriedades das classes:
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
 
computador1 = Computador('Asus', '8gb' ,'NVIDIA_RTX3070Ti') #podemos replicar o código ao lado para obter 
print('*' *16)                                              #e imprimir as informações def. pela classe.
print(computador1.marca)
print(computador1.memoria_ram)
print(computador1.placa_de_video)

print('*' *16) 
computador2 = Computador('ACER_NITRO', '16gb' ,'AMD_RX6900')
print(computador2.marca)
print(computador2.memoria_ram)
print(computador2.placa_de_video)

print('*' *16) 
computador3 = Computador('LENOVO_LEGION', '32gb' ,'NVIDIA_RTX4090')
print(computador3.marca)
print(computador3.memoria_ram)
print(computador3.placa_de_video)
print('*' *16)
