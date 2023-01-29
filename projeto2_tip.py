
from turtle import Turtle
 
turtle = Turtle()
turtle.speed(1)
 
while True:
    to_rotate = input('Deseja rotacionar? s/n ')
    if to_rotate == 's':
        rotate = input('Para qual lado rotacionar? e/d')
        if rotate == 'e':
            rotate_left = int(input('Quantos graus para a esquerda deseja rotacionar? '))
            turtle.left(rotate_left)
        elif rotate == 'd':
            rotate_right = int(input('Quantos graus para a direita deseja rotacionar? '))
            turtle.right(rotate_right)
    else:
        direction = input('Para qual direção deseja se mover? f/t')
        if direction == 'f':
            to_direction = int(input('Quantos pixels para a frente deseja se mover? '))
            turtle.forward(to_direction)
        elif direction == 't':
             to_direction = int(input('Quantos pixels para a frente deseja se mover? '))
             turtle.backward(to_direction)
  