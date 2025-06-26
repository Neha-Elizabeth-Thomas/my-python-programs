import turtle

list=[(10,28),(46,64),(17,90)]
t=turtle.Turtle()
t.up()
t.goto(list[-1])
t.down()
t.speed(1)
for p in list:
    t.goto(p)
turtle.done()