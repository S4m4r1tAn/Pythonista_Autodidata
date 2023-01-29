""" ​Desafio 1  🥇
Usando um loop, exiba na tela: Estamos em X
onde x é um valor iniciando em 18 e finalizando em 110 """

x = int(input('Digite um numero: '))
for x in range(18, 110 + 1):
    print(x)

""" Desafio 2
Você precisa de 10 passos para finalizar uma tarefa, 
exiba na tela, usando loop for a seguinte frase
"Realizando passo X" """

for numero in range(1, 11):
    print('Realizando passo X', numero)