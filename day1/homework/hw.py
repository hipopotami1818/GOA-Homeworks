from turtle import *

#we want to point a house

#step 1:  draw a square
speed(30)
width(7)
color("blue")
begin_fill()
forward(200)
left (90)
forward(200)
left (90)
end_fill()


forward(200)
left (90)

forward(200)
left (90)

#end of square

#drowing a door

forward(70)
color("red")
begin_fill()
left(90)          



forward(120)     
                  #height of the door
right(90)

forward(60)

right(90)


forward(120)

end_fill()

penup()
goto(200, 200)
pendown()

color("pink")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
penup()
goto(100,100)
pendown()
right(60)
penup()
goto(20,100)
pendown()
right(90)
forward(50)
right(90)
forward(30)
right(90)
forward(50)
left(270)
forward(25)


#window





exitonclick()



