import tkinter.colorchooser
from turtle import *
import tkinter
s=Screen()
s.setup(1020,1000)
tkinter.colorchooser.askcolor()
size=numinput('Enter an odd number',"Enter an odd number")
while size % 2 ==0:
    size=numinput('Enter an ODD number',"Enter an ODD number")
boxW=round(1020/size)
boxH=round(1000/size)
positionT=[]
rowcount=0
def nextrow():
    goto(-507,500)
    goto(-507,ycor()-boxH*rowcount)

speed(0) 
def square():
    global size
    global rowcount
    for i in range(int(size)):
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
    
penup()
goto(-507,500)    
for i in range(int(size)):
    square()
    nextrow()

mainloop()
