cores = ['vermelho', 'azul', 'verde', 'amarelo', 'rosa', 'preto']
ordem_cor = [1, 2, 3, 4, 5, 6]
print([i for i in cores])

#print('**RESULTADO 2**')
def lista_de_cores(ordem_cor):
    return ordem_cor + cores

print([lista_de_cores(ordem_cor) for cor in cores])
