#ask user for odd number, create grid using odd number

from turtle import *
import tkinter
s=Screen()
s.setup(1020,1000)
boxW=0
boxH=0
size=numinput('Enter an odd number',"Enter an odd number")


boxW=round(1020/size)
boxH=round(1000/size)


    
    


def square():
    global size
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
goto(-507,500)    
  
print(window_height())
for i in range(int(size)):
    square()


mainloop()
