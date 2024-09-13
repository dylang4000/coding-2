from turtle import *
import tkinter
s=Screen()
s.setup(1020,1000)
size=numinput('Enter an odd number',"Enter an odd number")
def square():
    global size
    for i in range(int(size)):
        pendown()
        forward(200)
        right(90)
        forward(200)
        right(90)
        forward(200)
        right(90)
        forward(200)
        penup()
        right(90)
        forward(200)
goto(-507,500)    
  
print(window_height())
square()


mainloop()
