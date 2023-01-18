#drawing polygons with any number of sides
import turtle
bob = turtle.Turtle()
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
polygon(bob,n = 7,length = 70)#draws a 7-sided polygon with side length 70