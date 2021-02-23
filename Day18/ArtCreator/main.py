import turtle as t
import random
# import colorgram
#
# extracted_colors = colorgram.extract("DamienHirst.jpg", 30)
# colors = list(map(lambda color: (color.rgb.r, color.rgb.g, color.rgb.b), extracted_colors))
# print (colors)

color_list = [(231, 251, 242), (198, 12, 32), (250, 237, 17), (39, 77, 189), (38, 217, 67), (238, 228, 5), (229, 159, 46), (27, 39, 158), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 247, 252), (244, 33, 165), (229, 17, 122), (73, 9, 31), (60, 14, 8), (224, 141, 211), (222, 160, 8), (10, 98, 61), (17, 18, 43), (47, 214, 232), (11, 227, 239), (79, 72, 215), (237, 155, 222), (73, 213, 169), (78, 234, 201), (50, 234, 244), (3, 66, 40)]

tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)

def damienhirst(turtle, rows, columns, distance = 50, dot_diam = 20):
    turtle.up()
    for r in range(rows):
        for c in range(columns):
            turtle.setposition(c * distance - 225, r * distance - 225)
            turtle.dot(dot_diam, random.choice(color_list))

damienhirst(tim, 10, 10)
tim.hideturtle()


screen = t.Screen()
screen.exitonclick()