from turtle import *

#we want to build a castle
speed(100)
#step 1 draw a square
color("brown")
width(7)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("red")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(100)
left(120)
forward(100)
end_fill()


color("red")
begin_fill()
right(110)
forward(100)
left(110)
forward(100)
end_fill()


#drawing a window
penup()
left(120)
forward(30)
right(90)
forward(30)
pendown()
begin_fill()
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
end_fill()

penup()
goto(140,155)
left(155)
forward(30)
right(155)
forward(30)
pendown()
begin_fill()
forward(20)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
end_fill()


























































exitonclick()