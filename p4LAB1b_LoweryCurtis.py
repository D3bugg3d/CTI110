import turtle             # Allows us to use turtles
import random
wn = turtle.Screen()      # Creates a playground for turtles
wn.bgcolor("Grey")      # Set the window background color
wn.title("LOOK AT MY CUTE TURTLE!!!")      # Set the window title

alex = turtle.Turtle()    # Create a turtle, assign to alex
alex.width("10")        #Deterine all of turtle's parameters/ color/ var_name/ shape
alex.color("Lawn Green")
alex.shape("turtle")
alex.pensize("5")
alex.color("Green")

alex.penup()
alex.backward(50)
alex.left(90)
alex.forward(10)
alex.pendown()
alex.circle(50,180)
alex.forward(30)
alex.circle(50,180)
alex.penup()
alex.right(90)
alex.forward(25)
alex.right(90)
alex.forward(50)
alex.left(90)
alex.pendown()
alex.forward(80)
alex.left(-180)
alex.forward(80)
alex.right(90)
alex.forward(130)
alex.penup()

wn.mainloop()




