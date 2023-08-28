from turtle import Turtle, Screen
import random

my_turtle_color = ["red", "blue", "green", "black", "purple", "green yellow", "firebrick", "cornflower blue", "medium violet red", "orchid", "medium slate blue", "lavender", "saddle brown", "deep pink", "orange", "salmon", "orange red", "magenta"]
my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.width(15)
my_turtle.speed(10)


def draw_random_walk():
    random_side = [0, 90, 180, 270]
    my_turtle.backward(30)
    my_turtle.setheading(random.choice(random_side))


for i in range(3 , 200):
    my_turtle.color(random.choice(my_turtle_color))
    draw_random_walk()

my_screen = Screen()
my_screen.exitonclick()