# Criar listas usando Loops e Range
nomes = []
for i in range(2):
    digitar = input('Nome do(a) aluno(a): ')
    frequencia = input('Voce frenquentou as aulas? sim ou nao: ')

    nomes.append(digitar)
 
# MAP

def aprovar_aluno(nome):
    frequencia = 'sim' or 'nao' #or False and 'nao'
    #frequencia = False or 'nao'
    if frequencia == 'sim':
        return nome + ' APROVADO(a)'
    if frequencia == 'nao':
        return nome + ' REPROVADO(a)'
        
print(list(map(aprovar_aluno, nomes)))
