from turtle import Turtle

#DESAFIO 1
t = Turtle()
t.speed(1)
while True:
    distancia = int(input('Distancia a percorrer: '))
    t.forward(distancia)
    distancia = int(input('Distancia a percorrer: '))
    t.backward(distancia)
    continue
    
#DESAFIO 2   
size = int(input("Enter the size of the square: "))
t = Turtle()
t.speed(2)
for i in range(4):
    t.forward(size)
    t.right(90)
input()
