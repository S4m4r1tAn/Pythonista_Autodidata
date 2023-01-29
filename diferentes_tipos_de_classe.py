# Métodos comuns
# Metodos de Classes (class Methods)
# Métodos estáticos (Static Methods)
class Computador:
    sistema_operacional = 'Windows 11'
    
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
 
    def exibir_dados_do_computador(self):
        print(self.marca, self.memoria_ram,
        self.placa_de_video, self.sistema_operacional)
 
    @classmethod
    def computador_escritorio(cls,memoria_ram):
        return cls('HP', memoria_ram,'Placa de Video - Baixo Custo')
 
    @classmethod
    def computador_configuracao_pesado(cls,memoria_ram):
        return cls('Lenovo_LEGION', memoria_ram,'Placa de Video - Alto Nível')
    @staticmethod 
    def roda_programas_pesados(memoria_ram):
        if memoria_ram >= 8:
            return True
        else:
            return False
print(Computador.roda_programas_pesados(12))
    
""" # Configuração para cliente de escritorio
computador1 = Computador.computador_escritorio('8Gb')
# Configuracao para clientes de trabalho pesado(jogos,edicao de videos,3d,4K)
computador2 = Computador.computador_configuracao_pesado('16')
computador1.exibir_dados_do_computador()
print('##########')
computador2.exibir_dados_do_computador() """



