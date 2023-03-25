#zadanie 4 krok 1

import turtle

def draw_rect():
    print("XXX")
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(1)

    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)

    screen.exitonclick()

#zadanie 4 krok 3

def draw_star():
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(1)

    for _ in range(5):
        t.forward(100)
        t.right(144)
    screen.exitonclick()

#zadanie 4 krok 2

def draw_reg_poly(n):
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(1)

    for _ in range (n):
        t.forward(100)
        t.left(360 / n)

    screen.exitonclick()



