#Suleiman Samantar, Suleiman Alnsour,Maxim
"""
Suleiman Samantar wrote the def setPos function and the def hexagon,circle and square
function for the drawing of the shapes while Suleiman Alnsour wrote the def pattern
functions for the coordinates of the shapes and Maxim wrote the final part,the def main.
""" 
import turtle

"""This sets the position of the turtle according to x and y coordinates"""
def setPos(turta, x,y):
    turta.penup() 
    turta.goto(x,y) # moves to given coordinates
    turta.pendown()
    turta.setheading(0) # This is the starting point of our pointer

"""This function draws the hexagon and fills it with color(hexa_color) as well as border 
color(border_color)"""
def hexagon(turta, hexa_color, border_color):
    turta.pendown()
    turta.pencolor(border_color) 
    turta.fillcolor(hexa_color)
    turta.begin_fill() 
    turta.forward(50)
    turta.right(65)
    turta.forward(50)
    turta.right(65)
    turta.forward(50)
    turta.right(65)
    turta.forward(50)
    turta.right(65)
    turta.forward(50)
    turta.right(65)
    turta.forward(50)
    turta.right(65)
    turta.end_fill()
    turta.penup()

def square(turta, square_color, border_color):
   turta.pendown()
   turta.pencolor(border_color)
   turta.fillcolor(square_color)
   turta.begin_fill()
   turta.forward(90)
   turta.right(90)
   turta.forward(90)
   turta.right(90)
   turta.forward(90)
   turta.right(90)
   turta.forward(90)
   turta.right(90)
   turta.end_fill()
   turta.penup()


def circle(turta, circle_color, border_color):
   turta.pendown()
   turta.pencolor(border_color)
   turta.fillcolor(circle_color)
   turta.begin_fill()
   turta.circle(45) #This is the radius of the circle
   turta.end_fill()
   turta.penup()

"""This function sets the position of each of the three hexagons,circles and squares on the canvas"""
def pattern(turta, hexa_color, circle_color, square_color, border_color):
    setPos(turta, -250, 150)
    hexagon(turta, hexa_color, border_color )
    setPos(turta, -100, 100)
    circle(turta, circle_color, border_color)
    setPos(turta, -40, 200)
    square(turta, square_color, border_color)
   
   
    setPos(turta, -200, 50 )
    hexagon(turta, hexa_color, border_color )
    setPos(turta, -50, 0 )
    circle(turta, circle_color, border_color)
    setPos(turta, 25, 100)
    square(turta, square_color, border_color)


    setPos(turta, -150, -50)
    hexagon(turta, hexa_color, border_color )
    setPos(turta, 0, -100)
    circle(turta, circle_color, border_color)
    setPos(turta, 100, 0)
    square(turta, square_color, border_color)

"""This function is the execution of the code, we have used(turtle.bgcolor)for the canvas background color 
as well as asking the user to input the color of each shape and setting the speed of the pen."""
def main():
    turtle.bgcolor("light blue")
    hexa_color = input("Enter Hexagon color: ")
    circle_color = input("Enter Circle color: ")
    square_color = input("Enter Square color: ")
    border_color = input("Enter Border color: ")
    turtle.speed(50) 
    pattern(turtle, hexa_color, circle_color, square_color, border_color)
    turtle.done()
    input()

main()
