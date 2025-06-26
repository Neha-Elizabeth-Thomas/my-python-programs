import turtle

t1=turtle.Turtle()
t1.penup()
t1.goto(-200,-200)
t1.pendown()
for i in range(6):
    t1.right(60)
    t1.fd(50)
    t1.left(120)
    t1.fd(50)
t1.hideturtle()
turtle.done()