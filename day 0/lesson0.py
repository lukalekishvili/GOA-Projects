from turtle import *

#we want to paint a house

#step 1: draw a square
speed(7)
width(7)
color("purple")
begin_fill()
forward(300)
left(90)

forward(300)
left(90)

forward(300)
left(90)

forward(300)
left(90)
end_fill()
#end of square

#drawing a door

forward(120)
color("yellow")
begin_fill()
left(90)
forward(140)      #height of the door   
right(90)
forward(60)
right(90)
forward(140)
end_fill()

penup()
goto(300, 300)
pendown()

color("red")
begin_fill()
right(150)
forward(300)
left(120)
forward(300)
end_fill()
#end of drawing a door

#drawing windows

penup()
goto(250,250)
pendown()

color("blue")
begin_fill()
left(30)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
end_fill()

right(90)
forward(36)
right(90)
color("light blue")
forward(70)

penup()
goto(215, 250)
pendown()

left(90)
forward(70)

penup()
goto(125, 250)
pendown()

color("blue")
begin_fill()
forward(70)
right(90)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
right(90)
end_fill()

forward(36)
color("light blue")
right(90)
forward(70)

penup()
goto(90, 250)
pendown()

left(90)
forward(70)
#end of drawing windows

#drawing GOA
penup()
goto(-250, -100)
pendown()

right(90)
width(15)
color("black")
forward(120)
left(90)
forward(140)
left(90)
forward(120)
left(90)
forward(70)
left(90)
forward(70)

penup()
goto(-210, -110)
pendown()

left(90)
width(40)
color("green")
forward(120)
left(90)
forward(90)
left(90)
forward(120)
left(90)
forward(90)

penup()
goto(-90,-240)
pendown()

right(125)
width(15)
color("black")
forward(160)
left(215)
forward(132)
left(180)
forward(55)
left(90)
forward(45)
#end of drawing GOA




exitonclick()