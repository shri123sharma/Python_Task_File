import turtle

colors=["red","purple","blue","green","orange","yellow"]

t=turtle.pen()

turtle.bgcolor("black")

t.speed(10)

for i in range(360):

    t.pencolor(colors[i%6])
    t.width(i//100+1)
    t.forword(i)
    t.left(59)






