#Interface Design

#circle - radius r-parameter

#polygon-->>to draw 50-sided polygon

import math

import turtle
bob = turtle.Turtle()
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
polygon(bob,n = 7,length = 70)

def circle(t, r):
    circumference = 2 * math.pi * r#2pir
    n = 50# n is no of line segments in our approximation of circle
    length = circumference / n
    polygon(t, n, length)
        
        
        