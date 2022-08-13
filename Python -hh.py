from turtle import *
bgcolor('black')
color('white', 'cyan')
hideturtle()
speed(50)
pensize(1)

def Draw():
    for i in range(80):
        forward(100)
        left(70)
        
def Draw_1():
    for i in range(80):
        forward(100)
        left(55)

def Draw_2():
    for i in range(80):
        forward(150)
        left(66)
    
def Draw_3():
    for i in range(80):
        circle(200, 180)
        forward(20)
        left(70)
    done()
        
    
Draw()
Draw_1()
Draw_2()
Draw_3()
