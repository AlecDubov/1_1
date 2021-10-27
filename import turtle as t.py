import turtle as t
x = int(input("What x-value do you want to plot? "))
m = int(input("What do you want your slope to be? "))
b = int(input("What do you want your y-intercept to be? "))
y = m*x +b
#Pseudocode: need grid lines for this

t.goto(x, y)
t.pendown()
t.stamp()

wn = t.Screen()
wn.mainloop()