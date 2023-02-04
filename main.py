import time
from turtle import Screen
from sneak import Sneak
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Sneak Game")
screen.tracer(0)

sneak = Sneak()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(sneak.up, "Up")
screen.onkey(sneak.down, "Down")
screen.onkey(sneak.right, "Right")
screen.onkey(sneak.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    sneak.move()

    if sneak.head.distance(food) < 15:
        food.refresh()
        sneak.extend()
        score.increas_score()

    if sneak.head.xcor() < -280 or sneak.head.xcor() > 280 or sneak.head.ycor() < -280 or sneak.head.ycor() > 280:
        score.reset()
        sneak.reset()

    for segment in sneak.segments[1:]:
        if sneak.head.distance(segment) < 15:
            score.reset()
            sneak.reset()

screen.exitonclick()
