from turtle import Turtle

#DESAFIO 1
t = Turtle()
t.speed(1)
while True:
    direcao = input('Para qual direcao devemos ir? "f: frente" ou "t: tras": ')
    if direcao == 'f':
        distancia = int(
            input('Quantos pixels devemos movimentar para a frente? '))
        movimentar_para_lado = input(
            'Rotacionar para d: direita, e: esquerda n: nao rotacionar ')
        if movimentar_para_lado == 'd':
            angulo = int(input('Quantos graus a direita devemos rotacionar? '))
            t.right(angulo)
        elif movimentar_para_lado == 'e':
            angulo = int(input('Quantos graus para a esquerda devemos rotacionar? '))
            t.left(angulo)
        t.forward(distancia)
    if direcao == 't':
        distancia = int(
            input('Quantos pixels devemos movimentar para tras? '))
        movimentar_para_lado = input(
            'Rotacionar para d: direita, e: esquerda n: nao rotacionar ')
        if movimentar_para_lado == 'd':
            angulo = int(input('Quantos graus para a direita devemos rotacionar? '))
            t.right(angulo)
        elif movimentar_para_lado == 'e':
            angulo = int(input('Quantos graus para a esquerda devemos rotacionar? '))
            t.left(angulo)
        t.backward(distancia)
    resposta = input('Continuar andando? ')
    if resposta not in ('sim', 's'):
        break
    
#DESAFIO 2
