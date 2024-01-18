import turtle
import time
stage = turtle.Screen()
stage.bgcolor("black")
stage.title("Welcome to my game!")

pen = turtle.Turtle()
pen.color("White")
pen.penup()
pen.hideturtle()

border = turtle.Turtle()
border.color("yellow")
border.penup
border.setposition(-250, -250)
border.pendown()
border.pensize(3)
for i in range(4):
    border.forward(500)
    border.left(90)
border.hideturtle()

fred = turtle.Turtle()
fred.color("White")
fred.shape("turtle")

positions = []

startTime = time.time()

def go_up():
    fred.setheading(90)

def go_down():
    fred.setheading(270)

def go_left():
    fred.setheading(180)

def go_right():
    fred.setheading(0)

def end_game():
    pen.setposition(-330, -240)
    pen.write("Game over", True, align="left", font=("Arial", 14, "bold"))

def show_time():    
    pen.setposition(-330,260)
    pen.write(str(round(t, 2)) + " secs", True, align="left", font=("Arial", 14, "bold"))


stage.listen()
stage.onkey(go_right, "Right")
stage.onkey(go_up, "Up")
stage.onkey(go_down, "Down")
stage.onkey(go_left, "Left")

while True: 
    fred.forward(1)

    t = time.time()-startTime 

    if fred.xcor() > 240 or fred.xcor() < -240:
        end_game()
        show_time()
        break
    if fred.xcor() > 240 or fred.ycor() < -240:
        end_game()
        show_time()
        break

    position = (fred.xcor(), fred.ycor())
    if position in positions:
        end_game()
        show_time()
        break;
    else:
        positions.append(position)

turtle.done()