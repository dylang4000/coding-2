#ask user for odd number, create grid using odd number

from turtle import *
import tkinter
s=Screen()
s.setup(1020,1000)
size=numinput('Enter an odd number',"Enter an odd number")
def square():
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
    
   
print(window_height())
for i in range(int(size)):
    square()


mainloop()