import turtle
window = turtle.Screen()
window.bgcolor("#00adef")
window.title("Akash Program")

v=turtle.Turtle()
v.pencolor("black")
v.speed(1)
v.width(1)
v.hideturtle()

#position o design
v.color("white")
v.goto(-50,60)
v.begin_fill()
v.goto(100,100)
v.goto(100,-100)
v.goto(-50,-60)

v.goto(-50,60)
v.end_fill()

v.color("#00adef")
v.goto(15,100)
v.color("#00adef")
v.width(12)
v.goto(15,-80)
v.penup()

v.goto(100,0)
v.pendown()
v.goto(-100,0)
turtle.done()