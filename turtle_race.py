from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
userbet = screen.textinput(title="Make Your Bet", prompt="Which turtle do you think will win the race? Enter the "
                                                         "color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

y_axis = -150
for turtle_index in range(0, 6):
    y_axis += 50
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_axis)
    turtles.append(new_turtle)

if userbet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        random_dist = random.randint(0, 3)
        turtle.forward(random_dist)

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == userbet:
                print("You've won the bet! ")
            else:
                print(f"You Lost! {winning_color} won the race!")

screen.exitonclick()
