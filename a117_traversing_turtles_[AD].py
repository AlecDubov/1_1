#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl


# create an empty list of turtles
my_turtles = ["arrow", "turtle", "circle", "square", "triangle", "classic"]

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

t.penup()
# Selects starting position
startx = 0
starty = 0
t.penup()
# code for moving turtle
for t in my_turtles:
  t.goto(startx, starty)
  t.right(45)     
  t.forward(50)
  start_x = t.xcor()
  start_y = t.ycor()
  t.pencolor(turtle_colors)
  new_color = turtle_colors.pop()
  


#	adds move length
startx = startx + 50
starty = starty + 50

wn = trtl.Screen()
wn.mainloop()