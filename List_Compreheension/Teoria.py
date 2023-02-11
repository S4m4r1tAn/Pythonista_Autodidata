from pprint import pprint
# Como usar uma list compreheension
# nova_lista = [2 * i for i in range(10)]
# [expressao for membro in iteravel]
# print(nova_lista)
def aprovar_pessoa(nome):
    return nome + ' APROVADO'
# nomes = ['Larissa', 'Rafael', 'Marcus', 'John']
# print([nome + ' APROVADO' for nome in nomes])
# print([aprovar_pessoa(nome) for nome in nomes])
""" 
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5 
"""
pprint([[i for i in range(1, 6)] for x in range(5)])

# Usar condicionais em List Compreheension
# [expressao for membro in iteravel (condicional if)]
nomes = ['Larissa', 'Rafael', 'Marcus', 'John']
print([aprovar_pessoa(nome) for nome in nomes if nome != 'Rafael'])

# Valores numericos
def eh_numero_par(numero):
    valor = numero % 2
    if valor == 0:
        return True
    else:
        return False
print([i for i in range(20) if i not in (1, 5, 15, 19)])
print([i for i in range(20) if eh_numero_par(i)])
# A condicionavel eh flexivel
# [expressao (condicional if) for membro in iteravel]
participantes = ['Larissa', 'Rafael', 'Marcus', 'John']
ganhadores = ['Marcus', 'John']
print([i + ' GANHADOR' if i in ganhadores else i + ' NAO SELECIONADOS' for i in participantes])
