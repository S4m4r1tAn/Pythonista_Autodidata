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
pprint([i for i in range(19+1) if i not in (1, 5, 15, 19)])