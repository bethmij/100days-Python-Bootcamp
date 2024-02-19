import random
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("triangle")

# # Drawing dash line
# for i in range(10):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)


# # Drawing different shapes
# for i in range(8):
#     color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
#     timmy.pencolor(color)
#     sides = i+3
#     angle = 360/sides
#
#     for _ in range(i + 3):
#         timmy.forward(100)
#         timmy.right(angle)


# # Generate random walk
# timmy.pensize(10)
# for _ in range(100):
#     color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
#     timmy.pencolor(color)
#     timmy.forward(size)
#     timmy.setheading(random.choice(angle))


# # Drawing spirograph
# timmy.speed("fastest")
# angle = 0
#
# while angle != 360:
#     color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
#     timmy.pencolor(color)
#     timmy.circle(100)
#     angle += 5
#     timmy.setheading(angle)

screen = Screen()
screen.exitonclick()
