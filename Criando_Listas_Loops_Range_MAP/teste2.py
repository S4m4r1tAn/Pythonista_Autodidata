nomes = ['keila','hideki','cida','maria','andre','fabiana']
notas = [10, 5, 8, 5, 6, 6]
def aprovar_pessoas(nome, notas):
    if nome and notas <= 6:
        return nome + ' REPROVADO'
    else:
        return nome + ' APROVADO'
 
print(list(map(aprovar_pessoas, nomes, notas)))
