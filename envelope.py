import turtle
import random
m = turtle.Turtle()

def colour_random():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r,g,b)


for count in range(0,4):
    m.forward(100)
    m.right(90)


m.right(60)
m.forward(100)
m.left(120)
m.forward(100)
