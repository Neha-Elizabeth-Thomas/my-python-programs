from turtle import Turtle
import turtle

def drawPolygon(t,numsides,dist,x=0,y=0):
    angle=360/numsides
    t.up()
    t.goto(x,y)
    t.down()
    t.fillcolor("red")
    t.pencolor("green")
    t.begin_fill()
    for _ in range(numsides):
        t.forward(dist)
        t.left(angle)
    t.end_fill()
t=Turtle()
t.up()
drawPolygon(t,6,40,-200,-200)
drawPolygon(t,360,1)
turtle.done()