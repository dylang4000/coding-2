import turtle
from cow import draw_cow
from crocodile import draw_crocodile
from deer import draw_deer
from elephant import draw_elephant
from giraffe import draw_giraffe
#from owl import drawShape
from parrot import draw_parrot
from rabbit import draw_rabbit
#from turt import draw_turtle




selector=0

functionsanimals=[draw_parrot,draw_deer,draw_crocodile,draw_cow,draw_rabbit,draw_giraffe,draw_elephant]
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