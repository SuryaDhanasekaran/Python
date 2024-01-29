import turtle
bob = turtle.Turtle()#turtle Provides a function called Turtle.#Turtle creates a turtle object
print(bob)#<turtle.Turtle object at 0xb7bfbf4c>
#for i in range(4):
    #print('Hello!')
for i in range(4):#has header ends with colon and an indented body:body contain any number of statements
    bob.fd(100)
    bob.lt(90)#runs body four times

turtle.mainloop()#mainloop tells the windows to wait for the user to do something
bob.fd(100)#move the turtle forward

#the method fd is associated with turtle object we are calling bob.
#you are asking bob to move forward.
#the argument of fd is distance in pixels,size depends on your display
#other methods
#bk - move backward
#lt - left turn
#rt - right turn
#pu - pen up
#pd - pen down
#argument of lt and rt are angle in degrees

#bob refers to an object with type Turtle as defined in module turtle.

#once you create a turtle,you can call a methods to move it around the Window.
