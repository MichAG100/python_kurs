#zadanie 4 krok 6

import turtle

def apply(c):
    if c=="X":
        return "["
    elif c=="F"
        return "FF"
    else:
        return c

def transform(original):
    result = ""
    for c in original:
        result += apply(c)
    return result

def create_l_system(n, start):
    original = start
    for _ in range(n):
        result = transform(original)
        original = result
    return original
def draw_l_system(t,instructions,angle,length):
    stack = []
    for c in instructions:
        if c in ["A","B"]:
            t.forward(length)
        elif c=="-":
            t.right(angle)
        elif c=="+":
            t.left(angle)
        elif c== "[":
            stack.append((turtle.position(),turtle,heading)))
        elif c=="]":
            position, heading = stack.pop()
            t.pu()
            tourte.goto(position)
            t.setheading(heading)

def draw():
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(100)

    instructions = create_l_system(3, "F")
    draw_l_system(t, instructions,90,10)

    screen.exitonclick()

