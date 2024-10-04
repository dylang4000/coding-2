#tiger
#900x900
#pensize 4
#one function (draw_tiger)
from turtle import *

width(4)
sc=Screen()
sc.setup(900,900)
color('red')


bgpic('head_06.png')
    

penup()
def w():
    forward(5)
    
def a():
    left(5)
def s():
    backward(1)

def d():
    right(5)
def space():
   print(f'{xcor()},{ycor()}')
sc.onkey(w,'w')
sc.onkey(a,'a')
sc.onkey(s,'s')
sc.onkey(d,'d')
sc.onkey(space,"space")
sc.listen()


mainloop()