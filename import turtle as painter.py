#Kevin Toren, Jovan George, Alec Dubovyk, Liliana Federico
import turtle
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
  m = float(equation[equals+1:x])

  sign = equation.find("+")
  if not sign:
    sign = equation.find("-")

  b = float(equation[sign:])

  return (m, b)

# draw gridlines
def draw_gridlines():
  painter.pencolor("gray")
  painter.pensize(1)

  for x in range(80):
    x = -400+(x*10)
    painter.penup()
    painter.goto(x, -400)
    painter.pendown()
    painter.goto(x, 400)
  
  for y in range(80):
    y = 400-(y*10)
    painter.penup()
    painter.goto(-400, y)
    painter.pendown()
    painter.goto(400, y)
    
# draw the axes
def draw_axes():
  painter.pencolor("black")
  painter.pensize(5)
  painter.left(90)
  painter.forward(400)
  painter.backward(800)
  painter.forward(400)
  painter.right(90)
  painter.forward(400)
  painter.backward(800)

# graph the equation
def graph_equation(vals):
  painter.pencolor("red")
  painter.pensize(2)

  m, b = vals
  right_point = (m*40*10)+b*10
  left_point = (m*-40*10)+b*10

  painter.penup()
  painter.goto(0, b*10)
  painter.pendown()

  painter.goto(400, right_point)
  painter.goto(-400, left_point)

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
