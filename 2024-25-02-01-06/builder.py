import turtle 

turtle.setup(900,900)
turtle.setworldcoordinates(0, 900, 900, 0)
turtle.hideturtle()
turtle.speed(0)
def makerect(width,height,x,y):
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.begin_poly()
    turtle.begin_fill()
    turtle.fd(width)
    turtle.right(90)
    turtle.fd(height)
    turtle.right(90)
    turtle.fd(width)
    turtle.right(90)
    turtle.fd(height)
    turtle.end_fill()
    turtle.end_poly
allrects=[
    [14.816665,2.1166666,4.2358909e-07,0]
    [10.583333,2.1166666,2.1166666,25.4],
    [2.1166666,8.4666662,0,2.1166666],
    [2.1166666,8.4666662,31.75,2.1166666],
    [14.816666,2.1166666,19.049999,0],
    [2.1166663,6.3499999,12.7,2.1166666],
    [2.1166666,6.3499999,19.049999,2.1166666],
    [4.2333331,2.1166666,14.816666,6.3499994],
    [2.1166666,8.4666681,12.7,25.399998],
    [2.116667,8.4666653,16.933332,25.4],
    [12.7,2.1166666,4.9999997e-08,10.583333],
    [2.1166666,8.4666662,10.583333,12.7],
    [8.4666662,2.2129409,2.1166666,18.953724],
    [2.1701441,4.2333336,2.1166666,21.166666],
    [12.699998,2.1166666,-31.749998,25.4],
    [12.7,2.1166666,-33.866665,10.583333],
    [2.1166666,8.4666662,-23.283333,12.7],
    [8.4666662,2.2129409,-31.749998,18.953724],
    [2.1701441,4.2333336,-31.749998,21.166666]

]



for i in range(len(allrects)):
    makerect(allrects[i][0],allrects[i][1],allrects[i][2],allrects[i][3])



#makerect(14.816665,2.1166666,4.2358909e-070,0)
#makerect(10.583333,2.1166666,2.1166666,25.4)
#makerect(2.1166666,8.4666662,0,2.1166666)
#makerect()
makerect
makerect
makerect


turtle.done()
