from turtle import Screen
from Snakes import snakes
from food import Food
from Scoreboard import score
import time

s = Screen()
s.setup(width=600, height=600)
s.title("The Legendary Snake Game")
s.bgcolor('green')
s.tracer(0)

snake = snakes()
food = Food()
Sc = score()

s.listen()
s.onkey(key="Up", fun=snake.up)
s.onkey(key="Down", fun=snake.down)
s.onkey(key="Right", fun=snake.right)
s.onkey(key="Left", fun=snake.left)

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        Sc.increment()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
        Sc.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            Sc.game_over()

s.exitonclick()