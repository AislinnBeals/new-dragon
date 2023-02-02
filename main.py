import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("Coral")
#head
t.fillcolor("Green")
t.begin_fill()
for i in range(4):
    t.forward(90)
    t.left(90)
#Body
for i in range(2):
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(250)


#Back Scales
t.left(120)
for i in range(8):
    t.forward(30)
    t.left(120)
    t.forward(30)
    t.right(120)
t.end_fill()
#tail
t.fillcolor("green")
t.begin_fill("green")
t.forward(120)
t.left(50)
t.forward(20)
t.left(130)
t.forward(140)
t.end_fill()

s.exitonclick()
