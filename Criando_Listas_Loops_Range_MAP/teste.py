# Criar listas usando Loops e Range
nomes = []
for i in range(2):
    digitar = input('Nome do(a) aluno(a): ')
    frequencia = input('Voce frenquentou as aulas? sim ou nao: ')

    nomes.append(digitar)
 
# MAP

def aprovar_aluno(nome):
    frequencia = 'sim' or 'nao' #or False and 'nao' 
    if frequencia == True or 'sim': #frequencia = False or 'nao'
        return nome + ' APROVADO(a)'
    if frequencia == False or 'nao':
        return nome + ' REPROVADO(a)'
        
print(list(map(aprovar_aluno, nomes)))
