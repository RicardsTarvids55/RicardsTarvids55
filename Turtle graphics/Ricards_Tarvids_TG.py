#1. uzd
#importēju turtle
import turtle
#definēju kvadrāta leņķi un garumu
def square (angle, lenght):
    turtle.showturtle()
    turtle.shape("turtle")
    turtle.pencolor("blue")
#Ievadu kodu, kas izveidos kvadrātu
    for i in range (4): 
        turtle.forward(lenght)
        turtle.right(angle)
#Pārvietoju turtle lai 2. kvadrāts būtu ārpus pirmā
square(90, 100)
turtle.penup()
turtle.left(180)
turtle.forward(30)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.pendown()
square(90, 160)
turtle.done()

#2. uzd par apli onscreen click
#Importēju turtle un random
#import turtle, random 
#pārdēvēju turtle par sun lai saīsinātu pierakstu
#sun = turtle.Turtle()
#Ievadu krāsu opcijas no kurām random izvēlēties
#mylist = ["Blue", "red", "black", "green", "purple", "yellow", "pink", "orange", "cyan" ]
#definēju apļa funkciju
#def aplis(x ,y):
#    sun.penup()
#    sun.goto(x ,y)
#    sun.pendown()
#    sun.begin_fill()
#    sun.color(random.choice(mylist))
#    sun.circle(70)
#    sun.end_fill()
#Pievienoju cirlce funkciju 1. peles pogai
#turtle.onscreenclick(aplis, 1)
#turtle.listen()
#turtle.done()