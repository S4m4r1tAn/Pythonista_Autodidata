""" ​Desafio 🥇 """

""" Crie uma função chamado gerar_objeto_personalizado que irá receber 3 parâmetros, cor, altura, formato.
A sua função deve apenas imprimir na tela o que foi passado para ela, nada mais, nada menos.
Porém ela deve seguir as seguintes regras: """

#print('1 - O primeiro argumento deve ser posicional.')
#print('2 - Os argumentos altura e formato precisam OBRIGATORIAMENTE serem nomeados.')
cor = input('Digite sua cor favorita: ')
def gerar_objeto_persoalizado(cor, *, altura, formato):
    print(f'A cor do item eh {cor} e sua altura {altura}cm e o mesmo possui o maravilhoso formato de um {formato}.')

gerar_objeto_persoalizado(cor, altura=25, formato='hexagono')