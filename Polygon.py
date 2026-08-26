import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(100,120)
polygon=turtle.Turtle()

num_sides= 8
side_length=100
angle=360.0/num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()
