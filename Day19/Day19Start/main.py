import turtle as t

tim = t.Turtle()
screen = t.Screen()

# Listen to interaction from user:
def move_forward():
    print ("Forward")
    tim.forward(10)

def move_backward():
    print ("Backwards")
    tim.back(10)

def turn_right():
    print ("Turning right")
    tim.right(10)

def turn_left():
    print ("Turning left")
    tim.left(10)

def clear_drawing():
    tim.reset()

screen.listen()
screen.onkeypress(fun = move_forward, key="w")
screen.onkeypress(fun = move_backward, key="s")
screen.onkeypress(fun = turn_left, key="a")
screen.onkeypress(fun = turn_right, key="d")
screen.onkeypress(fun = clear_drawing, key="c")











screen.exitonclick()