import tkinter
from turtle import *
import tkinter
s=Screen()
size=numinput('Enter an odd number',"Enter an odd number")
s.setup(1020,1000)
boxW=round(1020/size)
boxH=round(1000/size)
positionT=[]
rowcount=0

while size % 2 ==0:
    size=numinput('Enter an ODD number',"Enter an ODD number")

def nextrow():
    goto(-507,500)
    goto(-507,ycor()-boxH*rowcount)


def square():
    global size
    global rowcount
    global positionT
    for i in range(int(size)):
        positionT.append([xcor(),ycor()])
        pendown()
        forward(boxW)
        right(90)
        forward(boxH)
        right(90)
        forward(boxW)
        right(90)
        forward(boxH)
        penup()
        right(90)
        forward(boxW)
    rowcount+=1
def grid():
    penup()
    goto(-507,500)    
    for i in range(int(size)):
        square()
        nextrow()
speed(0) 
grid()
onkeypress(print("hello"),"a")
listen()
mainloop()
