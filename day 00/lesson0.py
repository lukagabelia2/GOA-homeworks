from turtle import *
speed(3)
#draw a squeer
width(3)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
#end draw a squeer

#door
left(90)
forward(75)
color("purple")
begin_fill()
color("purple")
left(90)
forward(90)
right(90)
forward(60)
right(90)
forward(90)
end_fill()
#end drawing(door)

#drawing a roof
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
left(220)
forward(155)
left(100)
forward(155)
end_fill()

#end draw a roof

#draw window(1)
penup()
goto(0,100)
pendown() 

color("brown")
begin_fill()
left(130)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

#draw window (2)
penup()
goto(200,100)
pendown()

color("brown")
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

exitonclick()