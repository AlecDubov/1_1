import turtle as Scireaim

def Scireaims_head():
  Scireaim.penup()
  Scireaim.goto(-100,100)
  Scireaim.pendown()
  Scireaim.circle(100)
  

def Scireaims_face():
  Scireaim.penup()
  Scireaim.goto(-170,200)
  Scireaim.pendown()
  Scireaim.fillcolor("red")
  Scireaim.begin_fill
  Scireaim.circle(10)
  Scireaim.end_fill
  Scireaim.penup()
  Scireaim.goto(-25,200)
  Scireaim.pendown()
  Scireaim.begin_fill
  Scireaim.circle(10)
  Scireaim.end_fill


    
Scireaim.pencolor("Black")
Scireaims_head()
Scireaims_face()


wn = Scireaim.Screen()
wn.mainloop()