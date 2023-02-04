import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgpic("clouds.png")
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
t.begin_fill()
t.forward(120)
t.left(50)
t.forward(20)
t.left(130)
t.forward(140)
t.end_fill()

#teefs
t.penup()
t.goto(30,15)
	
t.setheading(60)


t.fillcolor("white")
t.begin_fill()
for i in range(6):
    t.forward(10)
    t.right(120)
    t.forward(10)
    t.left(120)
t.end_fill()

#eyeBall
t.penup()
t.goto(40,40)
t.pensize(5)
t.dot("black")


#back legs

t.penup()
t.goto(-245,-90)
t.fillcolor("green")
t.begin_fill()
t.right(150)
t.forward(30)
t.left(90)
t.forward(35)
t.left(90)
t.forward(30)
t.right(90)
t.forward(15)
t.right(90)
t.forward(30)
t.left(90)
t.forward(35)
t.left(90)
t.forward(30)
t.right(90)
#front legs
t.forward(70)
t.right(90)
t.forward(30)
t.left(90)
t.forward(35)
t.left(90)
t.forward(30)
t.right(90)
t.forward(15)
t.right(90)
t.forward(30)
t.left(90)
t.forward(35)
t.left(90)
t.forward(30)
t.end_fill()

#yellow scales
t.penup()
t.goto(-30,-30)
t.dot("yellow")

t.goto(-120,-30)
t.dot("yellow")

t.goto(-90,-50)
t.dot("yellow")
t.goto(-210,-65)
t.dot("yellow")
t.goto(-190,-20)
t.dot("yellow")
t.goto(-140,-10)
t.dot("yellow")

#red scales
t.pensize(2)
t.goto(-50,-30)
t.dot("red")

t.goto(-20,-75)
t.dot("red")

t.goto(-80,-23)
t.dot("red")
t.goto(-220,-60)
t.dot("red")
t.goto(-175,-25)
t.dot("red")
t.goto(-145,-15)
t.dot("red")

#wings
t.penup()
t.goto(-90,0)
t.fillcolor("dark green")
t.begin_fill()
t.left(30)
t.forward(150)
for i in range(4):
    t.left(120)
    t.forward(30)
    t.right(120)
    t.forward(30)
t.goto(-90, 0)
t.end_fill()

#fire breath
t.fillcolor("orange")
t.begin_fill()
t.penup()
t.goto(90, 15)
t.setheading(90)
t.right(60)
t.forward(200)
t.right(120)
t.forward(10)
t.left(120)
t.forward(10)
t.right(120)
t.forward(10)
t.left(120)
t.forward(10)
t.right(120)
t.goto(90,15)
t.end_fill()
t.penup()
t.home()
s.exitonclick()
