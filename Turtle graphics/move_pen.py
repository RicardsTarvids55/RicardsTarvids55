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

def move_forward():
    player1.color("light green")
    player1.forward(10)

def move_backward():
    player1.color("light green")
    player1.backward(10)
window1.onkeypress(turn_left_1, "a")
window1.onkeypress(turn_right_1, "d")
window1.onkeypress(move_forward, "w")
window1.onkeypress(move_backward, "s")
window1.listen()

while True:
    player1.forward(0.005)
    window1.update() 
# function for movement of an object  
    def moving_object(move): 
        
        # to fill the color in ball 
        move.fillcolor('orange')  
        
        # start color filling 
        move.begin_fill()  
        
        # draw circle 
        move.circle(20)   
        
        # end color filling 
        move.end_fill()              

    # Driver Code 
    if __name__ == "__main__" : 
        
        # create a screen object 
        screen = turtle.Screen()  
    
        # set screen size 
        screen.setup(600,600)     
    
        # screen background color 
        screen.bgcolor('green')    
    
        # screen updaion  
        screen.tracer(0)            
    
        # create a turtle object object 
        move = turtle.Turtle()  
    
        # set a turtle object color 
        move.color('orange') 
    
        # set turtle object speed 
        move.speed(0)  
    
        # set turtle object width 
        move.width(2)      
    
        # hide turtle object 
        move.hideturtle()           
    
        # turtle object in air 
        move.penup()                
    
        # set initial position 
        move.goto(-250, 0)  
    
        # move turtle object to surface 
        move.pendown()              
    
        # infinite loop 
        while True : 
            
            # clear turtle work 
            move.clear()   
            
            # call function to draw ball 
            moving_object(move)    
            
            # update screen 
            screen.update()     
            
            # forward motion by turtle object 
            move.forward(0.05)

            