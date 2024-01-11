import turtle
#n = 10
#turtle.showturtle()
#turtle.shape("turtle")
#turtle.pencolor("blue")
#for i in range (n*4):
#    turtle.forward (i * 10)
#    turtle.right(90)
#turtle.done()


def spiral(veids, krasa):
    n = 10
    turtle.showturtle()
    turtle.shape(veids)
    turtle.pencolor(krasa)
    for i in range (n*4):
        turtle.forward (i * 10)
        turtle.right(90)
    turtle.done()
spiral("arrow", "red")