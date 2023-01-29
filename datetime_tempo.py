from datetime import datetime

aniversario = datetime(2023, 12, 1)

#dia_do_aniversario = datetime.strptime(input('Digite a data do seu aniversario: '),'%d/%m/%Y')
data_atual = datetime.now()
dias = aniversario - data_atual
print(f'Faltam {dias} para o seu ANIVERSARIO!')