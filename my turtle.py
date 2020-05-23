#! python
import turtle
my = turtle.Turtle()
def house():   #it's a house 
    my.forward(100)
    my.right(90)
    my.forward(100)
    my.right(90)
    my.forward(60)
    my.right(90)
    my.forward(60)
    my.right(90)
    my.forward(20)
    my.right(90)
    my.forward(60)
    my.right(90)
    my.forward(60)
    my.right(90)
    my.forward(100)
    my.right(45)
    my.forward(70.71)
    my.right(90)
    my.forward(70.71)

def star():     #it's a star
    for i in range(5):
        my.forward(500)
        my.right(144)
        
def polygon(side) :
    ang = 360/side
    for i in range(side) :
        my.right(ang)
        my.forward(100)
    

polygon(8)


#star()
#house()
