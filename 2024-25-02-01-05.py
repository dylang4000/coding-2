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
keys=["1","2","3","4","5","6","7","8","9","r","o","y","g","b","i","v"]

while size % 2 ==0 :
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
        forward(1000)
        columnCount+=1
        print(i)
speed(0) 


width(4)
penup()
grid()

def test():
    print('asdasdf')

onkeypress(test,"1")
onkeypress(test,"2")
onkeypress(test,"3")
onkeypress(test,"4")
onkeypress(test,"5")
onkeypress(test,"6")
onkeypress(test,"7")
onkeypress(test,"8")
onkeypress(test,"9")
onkeypress(test,"0")
onkeypress(test,"r")
onkeypress(test,"o")
onkeypress(test,"y")
onkeypress(test,"g")
onkeypress(test,"b")
onkeypress(test,"i")
onkeypress(test,"v")


listen()
mainloop()