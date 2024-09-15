from turtle import *

width(5)
s=Screen()
s.setup(1020,1000)
size=int(numinput('Enter an odd number',"Enter an odd number"))
hideturtle()
boxW=round(1020/size)
boxH=round(1000/size)
positionT=[]
rowcount=0
boxcount=0
rowsCount=0
columnCount=0


while size % 2 ==0:
    size=numinput('Enter an ODD number',"Enter an ODD number")


def grid():
    global columnCount
    global rowsCount
    penup()
    goto(-510,500)
    pendown()
    rowsCount+=1
    forward(1020)
    for i in range(int(size)):
        
        penup()
        goto(-510,500-(boxW*rowsCount))
        pendown()
        forward(1020)
        rowsCount+=1
    
    right(90)
    penup()
    goto(-510,500)
    pendown()
    columnCount+=1
    forward(1020)
    for i in range(size):
        
        penup()
        goto(-510+((1020/size)*columnCount),500)
        pendown()
        forward(1020)
        columnCount+=1
speed(0) 


width()
penup()
grid()





listen()
mainloop()
