from turtle import Turtle, Screen
import random

my_color = ["red", "blue", "green", "black", "purple", "green yellow", "firebrick", "cornflower blue", "medium violet red", "orchid", "medium slate blue", "lavender", "saddle brown", "deep pink", "orange", "salmon", "orange red", "magenta"] 
my_screen = Screen()
user_color = my_screen.textinput(title="Get conntest", prompt="Which turle will win the race? Ennter the color")
my_screen.setup(width=500, height=400)
y_position = [-125, -75, -25 , 25 , 75, 125]
turtle_list = []

for i in range(0,5):
    tim = Turtle(shape="turtle") 
    tim.penup()    
    tim.color(my_color[i])
    tim.goto(x=-230, y=y_position[i])
    turtle_list.append(tim)

if user_color:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_color:
                print(f"You have won! The {wining_color} win the race.")
            else:
                print(f"You have lost! The {wining_color} win the race.")

        turtle.forward(random.randint(0,10))
        

my_screen.exitonclick()