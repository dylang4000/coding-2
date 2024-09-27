import turtle
from rabbit import draw_rabbit
from cow import draw_cow
from giraffe import draw_giraffe
from elephant import draw_elephant
selector=0

functionsanimals=[draw_rabbit,draw_cow,draw_giraffe,draw_elephant]
turtle.speed(0)


turtle.width(4)


functionsanimals[selector](turtle)
def select():
    print('asdfasdf')
    global selector
    selector+=1
    turtle.home()
    turtle.clear()
    functionsanimals[selector](turtle)
def negativeselect():
    print('asdfasdf')
    global selector
    selector-=1
    turtle.home()
    turtle.clear()
    functionsanimals[selector](turtle)  


turtle.onkeypress(select,'a')
turtle.onkeypress(negativeselect,'d')
turtle.listen()
turtle.mainloop()