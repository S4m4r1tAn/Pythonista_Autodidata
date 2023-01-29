import os

frutas = ['apple, orange, banana, grape, watermelon']
cores = ['verde, amarelo, azul, branco, cinza']
linguagem = ['Python, C#, C++, Java, Rust']


with open('frutas.txt', 'w', newline='') as arquivo:              #('DESAFIO 1:')
    for fruta in frutas:
        arquivo.write(fruta + os.linesep)
              
with open('frutas.txt', 'r') as arquivo:                          #('DESAFIO 2:')  
        for fruta in frutas:
            print(fruta)

with open('frutas.txt', 'a', newline='') as arquivo:              #('DESAFIO 3:')
    for cor in cores:
        arquivo.write(os.linesep + cor)
    
with open('Top 5 Linguagens.txt', 'w', newline='') as arquivo:     #('DESAFIO 4:')
    for linguagem in linguagem:
        arquivo.write(linguagem + os.linesep)
        
itens = ['musica.mp4', 'pic.jgp', 'passcode.txt','report.pdf']
""" for i in range(1, 4+1):                                        #('B O N U S:')

    x = str(i)
    with open("desafio" + x + ".txt", "w") as arquivo:
        pass             """
        
for file in itens:
    with open(file, 'w') as arquivo:
        pass                                         