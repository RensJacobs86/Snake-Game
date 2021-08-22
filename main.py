from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_running = True
while game_running:
    screen.update()
    time.sleep(.07)
    snake.move()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_running = False
        scoreboard.game_over()

    for seg in range(1, len(snake.segments)):
        if snake.head.distance(snake.segments[seg]) < 10:
            game_running = False
            scoreboard.game_over()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.point_up()
        screen.update()
        snake.body_up()















screen.exitonclick()