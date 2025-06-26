import turtle

# Set up the turtle
star = turtle.Turtle()
star.color("gold")
star.pensize(2)

# Draw a 5-pointed star
for _ in range(5):
    star.forward(100)
    star.right(144)  # Exterior angle for a 5-pointed star

# Hide turtle and finish
star.hideturtle()
turtle.done()
