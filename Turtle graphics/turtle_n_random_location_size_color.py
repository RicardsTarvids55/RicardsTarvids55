import random, turtle
n = int(input("Cik figūrās zīmēsiet?"))
mylist = ["Blue", "red", "black", "brown", "green", "purple", "yellow", "pink", "orange", "cyan" ]
turtle.shape("turtle")
for _ in range (n):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()

    lenght = random.randint(1, 15) * 10
    turtle.showturtle()
    turtle.color(random.choice(mylist))

    for _ in range (15):
        turtle.forward(lenght)
        turtle.right(90)
        lenght += 5
turtle.done()