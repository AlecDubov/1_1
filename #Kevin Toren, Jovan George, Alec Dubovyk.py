#Kevin Toren, Jovan George, Alec Dubovyk, Liliana Federico
import turtle
from math import atan2, degrees, ceil
painter = turtle.Turtle()
painter.speed(0)

# asks for an equation from the user 
def get_equation():
  equation = input("Please enter an equation in the form of 'y=mx+b' ")
  return equation

# parse the equation
def parse_equation(equation):
  equation = equation.lower().replace(" ", "")

  equals = equation.find("=")
  x = equation.find("x")
  if equals == x:
    m = 1
  elif equation[equals+1:x] == "-":
    m = -1
  else:
    m = float(equation[equals+1:x])

  sign = equation.find("+")
  if sign == -1:
    sign = equation.rfind("-")

  b = float(equation[sign:])

  return (m, b)

# draw gridlines
def draw_gridlines():
  painter.pencolor("gray")
  painter.pensize(1)

  for x in range(40):
    x = -200+(x*10)
    painter.penup()
    painter.goto(x, -200)
    painter.pendown()
    painter.goto(x, 200)
  
  for y in range(40):
    y = 200-(y*10)
    painter.penup()
    painter.goto(-200, y)
    painter.pendown()
    painter.goto(200, y)
    
# draw the axes
def draw_axes():
  painter.pencolor("black")
  painter.pensize(5)
  painter.left(90)
  painter.forward(200)
  painter.backward(400)
  painter.forward(200)
  painter.right(90)
  painter.forward(200)
  painter.backward(400)

# graph the equation
def graph_equation(vals):
  painter.pencolor("red")
  painter.fillcolor("red")
  painter.pensize(2)

  m, b = vals
  right_x = (20-b)/m
  left_x = (-20-b)/m
  right_point = (m*right_x*10)+b*10
  left_point = (m*left_x*10)+b*10
  heading = degrees(atan2(m, 1))

  painter.penup()
  painter.goto(0, b*10)
  painter.pendown()

  painter.goto(right_x*10, right_point)
  painter.setheading(heading)
  painter.shape("arrow")
  painter.stamp()

  painter.goto(left_x*10, left_point)
  painter.setheading(heading+180)

# put it all together
def calculator():
  equation = get_equation()
  vals = parse_equation(equation)
  draw_axes()
  draw_gridlines()
  graph_equation(vals)

calculator()
wn = turtle.Screen()
wn.mainloop()