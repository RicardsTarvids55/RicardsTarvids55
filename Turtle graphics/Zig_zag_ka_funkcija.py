import turtle
#turtle.showturtle()
#turtle.shape("turtle")
#turtle.pencolor("red")
#for x in range (10):
#    if x%2 == 0:
#        turtle.forward(25)
#        turtle.right(45)
#    else:
#        turtle.forward(25)
#        turtle.right(45)

def turtle_zigzag(veids, krasa):
    turtle.showturtle()
    turtle.shape(veids)
    turtle.pencolor(krasa)
    for x in range (10):
        if x%2 == 0:
            turtle.forward(25)
            turtle.right(45)
        else:
            turtle.forward(25)
            turtle.right(45)
turtle_zigzag("turtle", "red")