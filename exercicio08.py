import turtle
import tkinter as TK

#Desenhe um quadrado.
# Configurações iniciais
'''screen = turtle.Screen()
screen.title("Desenho de um Quadrado")
t = turtle.Turtle()

# Desenha um quadrado com lado de 100 unidades
lado = 100

t.forward(lado)  # Move para a frente
t.right(90)      # Vira à direita 90 graus

t.forward(lado)  # Move para a frente
t.right(90)      # Vira à direita 90 graus

t.forward(lado)  # Move para a frente
t.right(90)      # Vira à direita 90 graus

t.forward(lado)  # Move para a frente
t.right(90)      # Vira à direita 90 graus

# Finaliza a execução
turtle.done()


#Desenhar um triangulo

import turtle

# Configurações iniciais
screen = turtle.Screen()
screen.title("Desenho de um Triângulo")
t = turtle.Turtle()

# Desenha um triângulo com lado de 100 unidades
lado = 100

t.forward(lado)  # Move para a frente
t.left(120)      # Vira à esquerda 120 graus

t.forward(lado)  # Move para a frente
t.left(120)      # Vira à esquerda 120 graus

t.forward(lado)  # Move para a frente
t.left(120)      # Vira à esquerda 120 graus

# Finaliza a execução
turtle.done()


#desenhar um circulo

import turtle

# Configurações iniciais
screen = turtle.Screen()
screen.title("Desenho de um Círculo")
t = turtle.Turtle()

# Desenha um círculo com raio de 100 unidades
t.circle(100)

# Finaliza a execução
turtle.done()


#Desenhe três quadrados
em uma fila com um espaço
entre cada um. Preencha-os
usando três cores diferentes.

import turtle

# Configurações iniciais
screen = turtle.Screen()
screen.title("Desenho de Três Quadrados")
t = turtle.Turtle()

# Lista de cores
cores = ['red', 'green', 'blue']

# Função para desenhar e preencher um quadrado
def desenhar_quadrado(t, lado, cor):
    t.fillcolor(cor)
    t.begin_fill()
    for _ in range(4):
        t.forward(lado)
        t.right(90)
    t.end_fill()

# Desenhar três quadrados com um espaço entre eles
lado = 50
espaco = 20

for cor in cores:
    desenhar_quadrado(t, lado, cor)
    t.penup()
    t.forward(lado + espaco)
    t.pendown()

# Finaliza a execução
turtle.done()'''


#Desenhar uma estrela de cinco pontas

import turtle

# Configurações iniciais
screen = turtle.Screen()
screen.title("Desenho de uma Estrela de Cinco Pontas")
t = turtle.Turtle()
t.pencolor("blue")
t.fillcolor("yellow")

# Função para desenhar uma estrela de cinco pontas
def desenhar_estrela(t, tamanho):
    for _ in range(5):
        t.forward(tamanho)
        t.right(144)  # Ângulo para formar a estrela de cinco pontas

# Desenha uma estrela com tamanho de 100 unidades
desenhar_estrela(t, 300)

# Finaliza a execução
turtle.done()
