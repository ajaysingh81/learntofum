import turtle
import random
import time
highestscore = 0
score = 0

# snake bodies
bodies = []

# getting screen |canvas
s = turtle.Screen()
s.bgcolor("grey")

delay = 0.1
s.title("SnakeGame")
s.setup(width=600, height=600)

# Create a Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("green")
head.fillcolor("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food of snake
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0, 200)
food.st()

# score board
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250, -250)
sb.write("score:0 | Highest Score : 0")

def moveup():
  if head.direction != "down":
    head.direction = "up"
def movedown():
  if head.direction != "up":
    head.direction = "down"
def moveleft():
  if head.direction != "right":
    head.direction = "left"
def moveright():
  if head.direction != "left":
    head.direction = "right"
def movestop():
    head.direction = "stop"

def move():
  if head.direction == "up":
    y = head.ycor()
    head.sety(y + 20)
  if head.direction == "down":
    y = head.ycor()
    head.sety(y-20)
  if head.direction == "left":
    x = head.xcor()
    head.sety(x-20)
  if head.direction == "right":
    x = head.xcor()
    head.sety(x+20)

# Event handing-key mapping
s.listen()
s.onkey(moveup, "w")
s.onkey(movedown, "s")
s.onkey(moveleft, "a")
s.onkey(moveright, "d")
s.onkey(movestop, "space")

# main loop
while True:
    s.update()  # this is a check update on screen
# check collision with border
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() > -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() > -290:
        head.sety(290)
# check collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

# increase the length of snake
    body = turtle.Turtle()
    body.speed(0)
    body.penup()
    body.shape("square")
    body.color("red")
    bodies.append(body)  # append new body

# increase the score
    score += 10

# change delay
    delay -= 0.001

# update the highest score
    if score > highestscore:
        highestscore = score
        sb.clear()
        sb.write("Score: () Highest Score: ()" .format(score, highestscore))
# move the snake bodies
    for index in range(len(bodies)-1, 0, -1):
        x = bodies[index-1].xcor()
        y = bodies[index-1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)
    move()
# check collision with snake body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

# hide bodies
        for body in bodies:
            body.ht()
        bodies.clear()

        score = 0
        delay = 0.1

# update Score board
        sb.clear()
        sb.write("Score: () Highest Score: ()" .format(score, highestscore))
    time.sleep(delay)
s.mainloop()