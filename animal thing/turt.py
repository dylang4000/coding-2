#from turtle import *
#
#
#s.setup(900, 900)
#pensize(4)
#speed("fastest")
#color("black")
#penup()

def drawLeftEye(t):
    t.goto(-107.0, -125.0)
    t.pendown()
    t.goto(-131.0, -77.0)
    t.goto(-66.0, -77.0)
    t.goto(-48.0, -115.0)
    t.goto(-70.0, -126.0)
    t.penup()

def drawRightEye(t):
    t.goto(110.0, -127.0)
    t.pendown()
    t.goto(132.0, -77.0)
    t.goto(68.0, -76.0)
    t.goto(51.0, -116.0)
    t.goto(72.0, -127.0)
    t.penup()

def drawHead(t):
    t.goto(-25, 60)
    t.pendown()
    t.goto(-107.0, 310.0)
    t.goto(-302.0, 416.0)
    t.goto(-278.0, 369.0)
    t.goto(-170.0, 254.0)
    t.goto(-72.0, 34.0)
    t.goto(-119.0, 11.0)
    t.goto(-168.0, -39.0)
    t.goto(-169.0, -104.0)
    t.goto(-204.0, -191.0)
    t.goto(-120.0, -328.0)
    t.goto(-69.0, -351.0)
    t.goto(-123.0, -259.0)
    t.goto(-70.0, -201.0)
    t.goto(-70.0, -126.0)
    drawLeftEye()
    goto(-69.0, -350.0)
    t.pendown()
    t.goto(1.0, -350.0)
    t.goto(1.0, -301.0)
    t.goto(-44.0, -275.0)
    t.goto(-38.0, -288.0)
    t.goto(-28.0, -285.0)
    t.penup()
    t.goto(0.0, -301.0)
    t.pendown()
    t.goto(44.0, -280.0)
    t.goto(43.0, -290.0)
    t.goto(30.0, -288.0)
    t.penup()
    t.goto(1.0, -349.0)
    t.pendown()
    t.goto(77.0, -350.0)
    t.goto(126.0, -259.0)
    t.goto(72.0, -201.0)
    t.goto(73.0, -127.0)
    drawRightEye()
    t.goto(78.0, -349.0)
    t.pendown()
    t.goto(118.0, -330.0)
    t.goto(202.0, -192.0)
    t.goto(166.0, -104.0)
    t.goto(166.0, -38.0)
    t.goto(119.0, 9.0)
    t.goto(70.0, 33.0)
    t.goto(167.0, 252.0)
    t.goto(276.0, 369.0)
    t.goto(302.0, 416.0)
    t.goto(105.0, 311.0)
    t.goto(23.0, 58.0)
    t.goto(-26.0, 57.0)
    t.penup()

def drawMouth(t):
    t.goto(-69.0, -351.0)
    t.pendown()
    t.goto(-48.0, -400.0)
    t.goto(1.0, -408.0)
    t.goto(47.0, -399.0)
    t.goto(67.0, -351.0)
    t.goto(-69.0, -351.0)
    t.penup()

def drawLeftEar(t):
    t.goto(-302.0, 414.0)
    t.pendown()
    t.goto(-291.0, 312.0)
    t.goto(-291.0, 213.0)
    t.goto(-127.0, 3.0)
    t.goto(-120.0, 13.0)
    t.goto(-71.0, 32.0)
    t.goto(-169.0, 253.0)
    t.goto(-277.0, 365.0)
    t.goto(-301.0, 414.0)
    t.penup()

def drawRightEar(t):
    t.goto(302.0, 414.0)
    t.pendown()
    t.goto(290.0, 311.0)
    t.goto(290.0, 215.0)
    t.goto(125.0, 2.0)
    t.goto(119.0, 9.0)
    t.goto(109.0, 14.0)
    t.goto(70.0, 33.0)
    t.goto(167.0, 250.0)
    t.goto(274.0, 365.0)
    t.goto(301.0, 410.0)
    t.penup()

def draw_rabbit(t):
    drawHead(t)
    drawMouth(t)
    drawLeftEar(t)
    drawRightEar(t)





# code to get coords (UNEEDED!!!)

#def clickprint(x, y):
#    goto(x, y)
#    print(f"goto{x, y}")
#
#def printPenUp():
#    print("penup()")
#    penup()
#
#def printPenDown():
#    print("pendown()")
#    pendown()

# s.onclick(clickprint)
# s.onkeypress(printPenUp, "w")
# s.onkeypress(printPenDown, "s")
# 
# s.listen()

