class computador:
    def componentes_computador(self, marca=None, gpu=None, ram=None):
        if marca and gpu and ram != None:
            print(f'{marca}, {gpu}, {ram}')
        elif gpu != None:
            print(f'{marca}, {gpu}')
        elif ram != None:
            print(f'{marca}, {ram}')
        else:
            print(f'{marca}')
            
pc = computador()
print('$$' *12)
pc.componentes_computador(marca='Alienware', gpu='RTX4080', ram='16gb')
pc.componentes_computador(marca='Lenovo_LEGION', ram='32gb')
pc.componentes_computador(marca='Acer_NITRO', gpu='RTX3090')
pc.componentes_computador(marca='HP_OMEN')
print('$$' *12)
