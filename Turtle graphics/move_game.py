import turtle

window1 = turtle.Screen()
window1.bgcolor('dark salmon')
window1.tracer(0)

player1 = turtle.Turtle()
player1.shape('turtle')
player1.color('turquoise')
player1.penup()

def turn_left_1():
  player1.color('light green')
  player1.left(10)
  
def turn_right_1():
  player1.color('light blue')
  player1.right(10)

def move_forward_1():
    player1.color("light green")
    player1.forward(10)

def move_backward_1():
    player1.color("light green")
    player1.backward(10)

window1.onkeypress(turn_left_1, "h")
window1.onkeypress(turn_right_1, "k")
window1.onkeypress(move_forward_1, "u")
window1.onkeypress(move_backward_1, "j")
window1.listen()

window2 = turtle.Screen()
window2.bgcolor('light salmon')
window2.tracer(0)

player2 = turtle.Turtle()
player2.shape('turtle')
player2.color('dark blue')
player2.penup()

def turn_left_2():
  player2.color('light green')
  player2.left(10)
  
def turn_right_2():
  player2.color('light blue')
  player2.right(10)

def move_forward_2():
    player2.color("light green")
    player2.forward(10)

def move_backward_2():
    player2.color("light green")
    player2.backward(10)
  
window2.onkeypress(turn_left_2, "a")
window2.onkeypress(turn_right_2, "d")
window1.onkeypress(move_forward_2, "w")
window1.onkeypress(move_backward_2, "s")
window2.listen()

while True:
  player1.forward(0.005)
  player2.forward(0.005)
  window2.update()
  window1.update()

  
turtle.done()