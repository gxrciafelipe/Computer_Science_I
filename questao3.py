from graphics import *

win=GraphWin("Formas", 200,200)
win.setBackground('light gray')

t = Text(Point(100,100), "Hello World!")
t.setFace("courier")
t.setSize(16)
t.setStyle("italic")

t.draw(win)
input ( " Press <Enter> to quit " )
win.close( )