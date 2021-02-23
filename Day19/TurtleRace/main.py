import turtle as t

screen = t.Screen()
screen_dimensions = (500, 400)
screen.setup(width = screen_dimensions[0], height = screen_dimensions[1])
user_bet = screen.textinput(title = "Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
turtles_distance = 30
lowest_y = -((len(colors)-1) * turtles_distance)/2
for i in range(len(colors)):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.up()
    new_turtle.color(colors[i])
    turtles.append(new_turtle)
    new_turtle.goto(x=-screen_dimensions[0]/2 + 20, y = lowest_y + turtles_distance * i)

# tim = t.Turtle(shape="turtle")
# tim.up()
# tim.goto(x=-screen_dimensions[0]/2 + 20, y = 0)

screen.exitonclick()