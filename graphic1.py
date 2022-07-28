import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('red')
t.speed(0)


for i in range(180):
    t.pencolor('yellow')
    t.circle(-i+10 , 200)
    t.rt(120)


turtle.done()