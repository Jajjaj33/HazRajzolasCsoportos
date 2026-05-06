import turtle

#negyzet
i=0
while i<4:
    turtle.forward(100)
    turtle.left(-90)
    i+=1
turtle.penup()
turtle.right(180)
turtle.forward(100)
turtle.pendown()
turtle.right(75)
turtle.forward(100)

turtle.done()