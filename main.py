# import
import turtle
import time
import random

delay = 0.1

# score
score = 00
high_score = 00

# screen tracer() This function is used to turn turtle animation on or off and set a delay for update drawings.
# Parameters: n: If n is given, only each n-th regular screen update is really performed
ws = turtle.Screen()
ws.title("Snake Game")
ws.bgcolor("yellow")
ws.setup(width=600, height=600)
ws.tracer(0)

# head
# penup or pu means pick pen up, so you can move turtle without leaving tracks. pendown or pd means pick pen down, so you can move the turtle and leave tracks.
# goto(x,y=none)  #goto=navigator
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
head.goto(0, 100)

segments = []
# Segment is the simplest way to integrate analytics into your application


# scoreboard

sb = turtle.Turtle()
sb.speed(0)
sb.shape("square")
sb.color("black")
sb.penup()
sb.hideturtle()
sb.goto(0, 260)
sb.write("score: 00, High score : 00", align="center", font=("ds-digital", 24, "normal"))


# functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"


# xcor() This function is used to return the turtle's x coordinate of the current position of turtle. It doesn't require any argument
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard binding

ws.listen()
ws.onkeypress(go_up, "w")
ws.onkeypress(go_down, "s")
ws.onkeypress(go_left, "a")
ws.onkeypress(go_right, "d")

# mainloop

while True:
    ws.update()

    # check collision with border

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hide the segment of body

        for segment in segments:
            segment.goto(1000, 1000)  # outnofrange
            # clear the segment
        segments.clear()

            # reset score
        score = 0

        # reset dalay
        delay = 0.1

        sb.clear()
        sb.write("score: {} Highest Score : {}".format(score, high_score), align="center",
                 font=("ds-digital", 24, "normal"))

# check collision with food
    if head.distance(food) < 20:

        # move the food to random place
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add mew segment to the head
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

        # shortan the delay

        delay -= 0.001

        # increase the score
        score += 10

        if score > high_score:
            high_score = score

        sb.clear()
        sb.write("score : {} high score : {} ".format(score, high_score), align="center",
                 font=("ds-digital", 24, "normal"))

        # move the segment in reverse oreder
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    move()

# check for collision with body

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

        # hide segment
            for segment in segments:
                segment.goto(1000, 100)

            segment.clear()
            score = 0
            delay = 0.1

            # update the score
            sb.clear()
            sb.write("score: {} high score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))
    time.sleep(delay)
ws.mainloop()
