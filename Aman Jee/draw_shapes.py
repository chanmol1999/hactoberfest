# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 05:50:44 2019

@author: amanj
"""

import turtle

def draw_square(some_turtle):
  
    for i in range(1,5):    
        some_turtle.forward(100)
        some_turtle.right(89)

#added draw_star method        
def draw_star(some_turtle):
  
    for i in range(5):
        some_turtle.forward(100)
        some_turtle.right(144)
        
        
def draw_art():
    
    window = turtle.Screen();
    window.bgcolor("blue")
    
    mike = turtle.Turtle()
    mike.shape("turtle")
    mike.color("black")
    mike.speed(9)

    for i in range(1,37):
        draw_square(mike)
        mike.right(10);

    ana = turtle.Turtle()
    ana.shape("arrow")
    ana.color("black")
    ana.circle(200)

    window.exitonclick()

    
draw_art()
