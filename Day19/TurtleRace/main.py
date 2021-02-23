import turtle as t
import random

screen = t.Screen()
screen_dimensions = (500, 400)
screen.setup(width = screen_dimensions[0], height = screen_dimensions[1])

race_on = False
winner = None
user_bet = screen.textinput(title = "Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
turtles_distance = 30
lowest_y = -((len(colors)-1) * turtles_distance)/2
goal_x = screen_dimensions[0]/2 - 30
for i in range(len(colors)):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.up()
    new_turtle.color(colors[i])
    turtles.append(new_turtle)
    new_turtle.goto(x=-screen_dimensions[0]/2 + 20, y = lowest_y + turtles_distance * i)

if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        move = random.randint(0 , 10)
        turtle.forward(move)
        if turtle.xcor() >= goal_x:
            winner = turtle.pencolor()
            race_on = False
            break

print (f"The winner is: {winner}")
if winner == user_bet:
    print ("Woohoo!! You won!!")
else:
    print ("You lost... Better luck next time!")


screen.exitonclick()