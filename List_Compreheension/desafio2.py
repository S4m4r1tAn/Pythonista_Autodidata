from pprint import pprint
cores = ['vermelho', 'azul', 'verde', 'amarelo', 'rosa', 'preto']
ordem_cor = [1, 2, 3, 4, 5, 6]

pprint([str(cores.index(i)+1) + ' - ' + i for i in cores])
