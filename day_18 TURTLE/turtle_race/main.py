import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=500)
user_color = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color : ")
is_game_on = False

color = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
all_turtle = []

if user_color in color:
    is_game_on = True

    for i in range(0, len(color)):
        turtle = Turtle(shape='turtle')
        turtle.color(color[i])
        turtle.penup()
        turtle.goto(x=-280, y=-100 + (i * 50))
        all_turtle.append(turtle)

while is_game_on:
    for turtle in all_turtle:
        if turtle.xcor() > 275.0:
            winning_color = turtle.pencolor()

            if winning_color == user_color:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lose! The {winning_color} turtle is the winner")

            is_game_on = False

        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)

screen.exitonclick()
