import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200, 0)
t.pendown()

# Define the animation function
def animate():
    for i in range(360):
        t.forward(1)
        t.right(1)

# Call the animation function
animate()

# Keep the window open until the user closes it
turtle.mainloop()
