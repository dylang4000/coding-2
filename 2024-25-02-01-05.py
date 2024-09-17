from turtle import *

width(5)
s=Screen()
s.setup(1020,1050)
size=int(numinput('Enter an odd number',"Enter an odd number"))
#hideturtle()
boxW=round(1020/size)
boxH=round(1000/size)
positionT=[]
rowcount=0
boxcount=0
rowsCount=0
columnCount=0
input=[]
keys=["1","2","3","4","5","6","7","8","9","r","o","y","g","b","i","v"]

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
    for i in range(int(size)):
        
        penup()
        goto(-510+((1020/size)*columnCount),500)
        pendown()
        forward(1020)
        columnCount+=1
speed(0) 


width(4)
penup()
grid()
penup()
goto(-510,534)
seth(0)
pendown()
begin_fill()
color('dimgray')
forward(1021)
right(90)
forward(30)
right(90)
forward(1021)
right(90)
forward(30)
end_fill()
penup()
backward(30)
right(90)
forward(10)
hideturtle()
color('white')
write('>>',font=('Arial',17, "normal"))
forward(25)
def r():
    global input
    write('r',font=('Arial',17, "normal"))
    forward(10)
    input.append('r')














onkey(r,"r")
onkey(r,"o")
onkey(r,"y")
onkey(r,"g")
onkey(r,"b")
onkey(r,"i")
onkey(r,"v")
onkey(r,"1")
onkey(r,"2")
onkey(r,"3")
onkey(r,"4")
onkey(r,"5")
onkey(r,"6")
onkey(r,"7")
onkey(r,"8")
onkey(r,"9")
onkey(r,"0")

listen()
mainloop()
