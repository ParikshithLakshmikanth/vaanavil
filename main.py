import turtle

turtle.Screen().bgcolor("black")

sc = turtle.Screen()
sc.setup(1280,720)

t= turtle.Turtle()
t.speed("fastest")
t.hideturtle()

colors = ["red","purple","blue","green","orange","yellow"]

while True:
    for x in range(200):
        t.pencolor(colors[x%len(colors)])
        t.width(x/100+1)
        t.forward(x)
        t.left(59)
    t.right(239)
    for x in range(200,0,-1):
        t.pencolor("black")
        t.width(x/100+7)
        t.forward(x)
        t.right(59)