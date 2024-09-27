from turtle import *
s = Screen()

s.setup(900, 900)
pensize(4)
speed("fastest")
color("black")
penup()

def drawLeftEye():
    goto(-107.0, -125.0)
    pendown()
    goto(-131.0, -77.0)
    goto(-66.0, -77.0)
    goto(-48.0, -115.0)
    goto(-70.0, -126.0)
    penup()

def drawRightEye():
    goto(110.0, -127.0)
    pendown()
    goto(132.0, -77.0)
    goto(68.0, -76.0)
    goto(51.0, -116.0)
    goto(72.0, -127.0)
    penup()

def drawHead():
    goto(-25, 60)
    pendown()
    goto(-107.0, 310.0)
    goto(-302.0, 416.0)
    goto(-278.0, 369.0)
    goto(-170.0, 254.0)
    goto(-72.0, 34.0)
    goto(-119.0, 11.0)
    goto(-168.0, -39.0)
    goto(-169.0, -104.0)
    goto(-204.0, -191.0)
    goto(-120.0, -328.0)
    goto(-69.0, -351.0)
    goto(-123.0, -259.0)
    goto(-70.0, -201.0)
    goto(-70.0, -126.0)
    drawLeftEye()
    goto(-69.0, -350.0)
    pendown()
    goto(1.0, -350.0)
    goto(1.0, -301.0)
    goto(-44.0, -275.0)
    goto(-38.0, -288.0)
    goto(-28.0, -285.0)
    penup()
    goto(0.0, -301.0)
    pendown()
    goto(44.0, -280.0)
    goto(43.0, -290.0)
    goto(30.0, -288.0)
    penup()
    goto(1.0, -349.0)
    pendown()
    goto(77.0, -350.0)
    goto(126.0, -259.0)
    goto(72.0, -201.0)
    goto(73.0, -127.0)
    drawRightEye()
    goto(78.0, -349.0)
    pendown()
    goto(118.0, -330.0)
    goto(202.0, -192.0)
    goto(166.0, -104.0)
    goto(166.0, -38.0)
    goto(119.0, 9.0)
    goto(70.0, 33.0)
    goto(167.0, 252.0)
    goto(276.0, 369.0)
    goto(302.0, 416.0)
    goto(105.0, 311.0)
    goto(23.0, 58.0)
    goto(-26.0, 57.0)
    penup()

def drawMouth():
    goto(-69.0, -351.0)
    pendown()
    goto(-48.0, -400.0)
    goto(1.0, -408.0)
    goto(47.0, -399.0)
    goto(67.0, -351.0)
    goto(-69.0, -351.0)
    penup()

def drawLeftEar():
    goto(-302.0, 414.0)
    pendown()
    goto(-291.0, 312.0)
    goto(-291.0, 213.0)
    goto(-127.0, 3.0)
    goto(-120.0, 13.0)
    goto(-71.0, 32.0)
    goto(-169.0, 253.0)
    goto(-277.0, 365.0)
    goto(-301.0, 414.0)
    penup()

def drawRightEar():
    goto(302.0, 414.0)
    pendown()
    goto(290.0, 311.0)
    goto(290.0, 215.0)
    goto(125.0, 2.0)
    goto(119.0, 9.0)
    goto(109.0, 14.0)
    goto(70.0, 33.0)
    goto(167.0, 250.0)
    goto(274.0, 365.0)
    goto(301.0, 410.0)
    penup()

def draw_rabbit():
    drawHead()
    drawMouth()
    drawLeftEar()
    drawRightEar()

draw_rabbit()



# code to get coords (UNEEDED!!!)

def clickprint(x, y):
    goto(x, y)
    print(f"goto{x, y}")

def printPenUp():
    print("penup()")
    penup()

def printPenDown():
    print("pendown()")
    pendown()

# s.onclick(clickprint)
# s.onkeypress(printPenUp, "w")
# s.onkeypress(printPenDown, "s")
# 
# s.listen()

hideturtle()
while True:
    forward(0)