import turtle, math

pegasus = turtle.Turtle()

turtle.getscreen().bgcolor("Cyan")
pegasus.speed(10)

def star(turtle, size):   
    if size <= 10:
        return
    else: 
        for i in range (5):
            turtle.forward(size)
            star(turtle, size/2)
            turtle.left(216)

star(pegasus, 200)

turtle.done()