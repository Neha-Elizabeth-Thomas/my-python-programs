from turtle import Turtle
def cCurve(t,x1,y1,x2,y2,level):
    if(level==0):
        t.up()
        t.goto(x1,y1)
        t.down()
        t.goto(x2,y2)
    else:
        xm=(x1+x2+y1-y2)//2
        ym=(y1+y2+x2-x1)//2
        cCurve(t,x1,y1,xm,ym,level-1)
        cCurve(t,xm,ym,x2,y2,level-1)
        
#level=int(input("Enter level: "))
t=Turtle()
cCurve(t,5,5,100,100,10)