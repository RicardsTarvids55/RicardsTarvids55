import turtle, random
sun = turtle.Turtle()
mylist = ["Blue", "red", "black", "green", "purple", "yellow", "pink", "orange", "cyan" ]
def taisnsturis (x, y):
    sun.penup()
    sun.goto(x, y)
    sun.pendown()
    sun.begin_fill()
    sun.color("brown")
    for i in range(2):
        sun.forward(40)
        sun.right(90)
        sun.forward(100)
        sun.right(90)
        sun.speed(10)
    sun.end_fill()
turtle.onscreenclick(taisnsturis, 1)
turtle.listen()
def aplis(x ,y):
    sun.penup()
    sun.goto(x ,y)
    sun.pendown()
    sun.begin_fill()
    sun.color(random.choice(mylist))
    sun.circle(70)
    sun.speed(10)
    sun.end_fill()
turtle.onscreenclick(aplis, 3)
turtle.listen()
turtle.done()