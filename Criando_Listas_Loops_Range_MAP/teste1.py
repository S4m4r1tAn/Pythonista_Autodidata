# Criar listas usando Loops e Range
nomes = []
frequencias = []
for i in range(2):
    digitar = input('Nome do(a) aluno(a): ')
    frequencia = input('Voce frenquentou as aulas? sim ou nao: ')

    nomes.append(digitar)
    frequencias.append(frequencia)
 
# MAP

def aprovar_aluno(nome, frequencia):
    if frequencia == 'sim':
        return nome + ' APROVADO(a)'
    if frequencia == 'nao':
        return nome + ' REPROVADO(a)'
        
print(list(map(aprovar_aluno, nomes, frequencias)))
