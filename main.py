import random
import turtle as t

tim = t.Turtle()
tim.speed("fastest")

# def move_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
#
# def move_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)


# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()


screen = t.Screen()
screen.listen()
screen.setup(height=500, width=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
turtle_colors = ["violet", "blue", "yellow", "green", "orange", "red"]
y_position = [-100, -60, -20, 20, 60,100]
all_turtles = []

for position in range(0, 6):
    tommy = t.Turtle(shape="turtle")
    tommy.penup()
    tommy.color(turtle_colors[position])
    tommy.goto(x=-230, y=y_position[position])
    all_turtles.append(tommy)
    tim.hideturtle()


if user_bet:
    game_on = True

while game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 250:
            game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!! The winner is {winning_color}")
            else:
                print(f"You've lost...Better luck next tym.The winner is {winning_color}")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
