from turtle import Turtle,Screen
import random
def randomwalk(t,turns,dist,x,y):
    t.up()
    t.goto(x,y)
    t.down()
    for _ in range(turns):
        angle=random.randint(0,360)
        t.forward(dist)
        t.setheading(angle)
        
t=Turtle()
t.screen.bgcolor("light blue")
randomwalk(t,20,30,2,2)
