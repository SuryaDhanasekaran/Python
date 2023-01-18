#Encapsulation
import turtle
def square(t):#t refers to same turtle bob\
    bob = turtle.Turtle()
    for i in range(4):
        t.fd(100)#indented twice to show that they are inside for loop and function definition
        t.lt(90)#t.lt(90) has same effect as bob.lt(90)
square(bob)
alice = Turtle()
square(alice)
#is flush with the left margin,which indicates the end of both for loop
#and function definition
 
#Wrapping a piece of code up in a function is called encapsulation.
#enables to reuse the code.