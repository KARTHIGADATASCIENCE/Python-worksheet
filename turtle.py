# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:07:04 2024

@author: 1mscds24
"""

import turtle
def draw():
    turtle.speed(2)
    turtle.bgcolour("lightblue")
    #bear head
    turtle.penup()
    turtle.goto(0,-100)
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    turtle.circle(80)
    turtle.end_fill()
    #ear
    turtle.penup()
    turtle.goto(-30,50)
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(30,50)
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    #eyes
    turtle.penup()
    turtle.goto(-20,10)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(8)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(20,10)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(8)
    turtle.end_fill()
    #nose
    turtle.penup()
    turtle.goto(0,-5)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()
    #smiling mouth
    turtle.penup()
    turtle.goto(-20,-20)
    turtle.pendown()
    turtle.color("black")
    turtle.width()
    turtle.right(8)
    turtle.circle(20,180)
    #hide
    turtle.hideturtle()
    turtle.done()
    draw()
    
    