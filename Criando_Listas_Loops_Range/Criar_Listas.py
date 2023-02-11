# Criar listas usando Loops e Range
nomes = []
for i in range(2):
    digitar = input('Nome do(a) aluno(a): ')
    frequencia = input('Voce frenquentou a aula? sim ou nao: ')
    if frequencia == 'sim':
        print(f' APROVADO(A)')
    elif frequencia == 'nao':
        print(f' REPROVADO(A)')
    else:
        print('FAVOR DIGITAR SIM OU NAO!')
        nomes.append(digitar)
 
# MAP
def aprovar_aluno(nome):
    frequentou_aula = True
    passou_nas_provas = True
    if frequentou_aula and passou_nas_provas:
        return nome + ' APROVADO'
    else:
        return nome + ' REPROVADO'
 
print(list(map(aprovar_aluno, nomes)))
