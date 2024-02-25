# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 20:40:58 2024

@author: hughc
"""
'turtle'

# spirograph

import math 
import turtle

def drawCircleTurtle(x, y, r):
    # move to start circle
    turtle.up()
    turtle.setpos(x + r, y)
    turtle.down()
    
    # draw circle
    for i in range(0, 365, 5):
        a = math.radians(i)
        turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))
    
drawCircleTurtle(100, 100, 50)
turtle.mainloop()

#%%

'tutorial video'

import turtle

turtle.color('red', 'blue')

turtle.begin_fill()

def drawsquare(size):
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)

drawsquare(200)

turtle.end_fill()

turtle.done

















