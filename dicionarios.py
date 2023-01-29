import random
from datetime import datetime

""" PROJETO 1
Objetivo de projeto:
Estamos criando um módulo de login do nosso aplicativo, 
e você deve obter as seguintes informações do funcionário. """

""" -> Módulo 1 - Gerar registro do funcionário
Funcionalidades do módulo 1
1. Obtenha o nome do usuário x
2. Obtenha a idade do usuário x
3. Registre de forma automática a data do cadastro do usuário, usando a data do 
registro como data de registro x
4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, 
que é sorteado de forma aleatória:
cartoes = ['R$50,00','R$250,00','R$120,00']
5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa) """

dados = dict()
dados ['nome'] = input('Digite seu nome para registro: ')
nasc = datetime.strptime(input('Digite sua data de nascimento: '), '%d/%m/%Y')
dados ['idade'] = datetime.now() - nasc
cartoes = ['R$50,00','R$250,00','R$120,00']

""" -> Módulo 2 - Gerar apresentação do usuário
Funcionalidades do módulo 2 - Mensagem de boas vindas!
Usando os dados obtidos no módulo 1, exiba as seguintes informações:
1. Olá (nome do usuário), seu registro foi concluído com sucesso no dia(data de cadastro no 
formato dd/mm/aaaa).
Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de (valor sorteado). """

data_registro = datetime.today().strftime('%d/%m/%Y')

print(f'Ola {dados ["nome"]}, seu registro foi concluido com sucesso no dia {data_registro}.')

print(f'Parabens, houve um sorteio e voce ganhou um cartao de compras no valor de {random.choice(cartoes)}.')
