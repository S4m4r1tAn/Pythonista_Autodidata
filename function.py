'''
FUNCTIONS:
def -> nome da funcao (parametros)
    comandos
'''
print('DESAFIO 1')
def gerar_nome_completo(nome_completo):
    print(f'Bem vindo {nome_completo}!')

gerar_nome_completo('Emerson Guimaraes')

print('DESAFIO 2')
 
preco = float(input('Digite o preço unitário do produto: R$ '))
quantidade = int(input('Qual a quantidade que voce ira comprar: '))
 
def calcular_valores(preco, quantidade = 1):
    print(f'O preco do produto é R${preco:.2f} reais. Você comprou {quantidade}, irá pagar R${preco*quantidade:.2f}')      
calcular_valores(preco, quantidade)