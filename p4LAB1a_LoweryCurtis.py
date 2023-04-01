import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
wn.bgcolor("ivory1")      # Set the window background color
wn.title("LOOK AT MY CUTE TURTLE!!!")      # Set the window title

alex = turtle.Turtle()    # Create a turtle, assign to alex
turtle.width("10")        #Deterine all of turtle's parameters/ color/ var_name/ shape
turtle.color("LightBlue4")
turtle.shape("turtle")
alex.pensize("5")

tess = turtle.Turtle()    # Create a turtle, assign to alex
turtle.width("10")        #Deterine all of turtle's parameters/ color/ var_name/ shape
turtle.color("black")
turtle.shape("turtle")
tess.pensize("5")

clrs = ["yellow", "red", "purple", "blue"]
for c in clrs:
    alex.color(c)
    alex.forward(100)
    alex.left(90)

clrs = ["LightBlue", "LightCyan", "LightGoldenrod"]
for c in clrs:
    tess.color(c)
    tess.left(120)
    tess.forward(100)
    

wn.mainloop()             # Wait for user to close window
