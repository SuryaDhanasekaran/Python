#Generalization-adding a paramter to a function.

#add a length parameter to square
import turtle
bob = turtle.Turtle()
def square(t, length):#parameter-lenght
    for i in range(4):
        t.fd(length)
        t.lt(90)
square(bob, 1000)
turtle.mainloop()