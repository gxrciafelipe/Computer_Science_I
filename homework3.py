#Felipe Garcia
#20 September 2025
#Homework 3
from graphics import *
import math

#1
#Sum of a series of numbers
def series_sum():
    n=int(input("How many numbers you want to sum? "))
    sum=0
    for i in range(0, n):
        number=float(input("Enter a number: "))
        sum+=number
    print("The sum of the numbers is:", sum)

#series_sum()

#2
#Average of a series of numbers
def series_avg():
    n=int(input("How many numbers you want to average? "))
    sum=0
    for i in range(0, n):
        number=float(input("Enter a number: "))
        sum+=number
    avg=sum/n
    print("The average of the numbers is:", avg)

#series_avg()

#3
#a
    #Point(130, 130) creates an object of class Point with x and y attributes both set to 130.

#b
    #c=Circle(Point(30,40),25)
    #c.setFill('blue')
    #c.setOutline('red')
    #Creates a circle object named c with center at point (30,40) with radius 25. The fill color of the circle is blue and the outline color is red.

#c
    #r = Rectangle(Point(20,20),Point(40,40))
    #r.setFill(color_rgb(0,255,150))
    #r.setWidth(3)
    #Creates a rectangle object named r with opposite corners at points (20,20) and (40,40). The fill color of the rectangle is set to an RGB color with red=0, green=255, blue=150, which is a light green. The outline width of the rectangle is set to 3.

#d
    #l = Line(Point(100,100), Point(100,200))
    #l.setOutline("red4")
    #l.setArrow("first")
    #Creates a line object named l from point (100,100) to point (100,200). The outline color of the line is set to "red4", which is a dark red color. An arrowhead is added to the start of the line.

#e
    #Oval(Point(50,50), Point(60,100))
    #Creates an object of class Oval with a bounding box defined by the points (50,50) and (60,100).

#f
    #shape = Polygon(Point(5,5), Point(10,10), Point(5,10), Point(10,5))
    #shape.setFill("orange")
    #Creates a polygon object named shape with vertices at points (5,5), (10,10), (5,10), and (10,5). The fill color of the polygon is set to orange.

#g
    #t = Text(Point(100,100), "Hello World!")
    #t.setFace("courier")
    #t.setSize(16)
    #t.setStyle("italic")
    #Creates a text object named t with the string "Hello World!" positioned at point (100,100). The font face is set to "courier", the font size is set to 16, and the font style is set to italic.

#4
    #The program creates a graphical window with a red circle. When the user clicks inside the window, the circle moves to the location of the mouse click. This process repeats for a total of 10 mouse clicks, and after the 10 clicks the window closes.

#5
def target():
    win = GraphWin("Target")
    c = Circle(Point(100,100), 100)
    c.setFill("white")
    c.setWidth(5)
    c.draw(win)
    c1 = Circle(Point(100,100), 70)
    c1.setFill("black")
    c1.setWidth(5)
    c1.draw(win)
    c2 = Circle(Point(100,100), 50)
    c2.setFill("blue")
    c2.setWidth(5)
    c2.draw(win)
    c3 = Circle(Point(100,100), 20)
    c3.setFill("red")
    c3.setWidth(5)
    c3.draw(win)
    c4 = Circle(Point(100,100), 5)
    c4.setFill("yellow")
    c4.setWidth(5)
    c4.draw(win)
    input("Press <Enter> to close")
    win.close()
#target()

#6
def face():
    win = GraphWin("Face", 400, 400)
    win.setBackground("light gray")
    head = Oval(Point(50,370), Point(350,50))
    head.setFill("yellow")
    head.draw(win)
    left_eye = Circle(Point(130,150), 30)
    left_eye.setFill("white")
    left_eye.draw(win)
    right_eye = Circle(Point(270,150), 30)
    right_eye.setFill("white")
    right_eye.draw(win)
    left_pupil = Circle(Point(130,150), 10)
    left_pupil.setFill("black")
    left_pupil.draw(win)
    right_pupil = Circle(Point(270,150), 10)
    right_pupil.setFill("black")
    right_pupil.draw(win)
    mouth = Oval(Point(130,250), Point(270,300))
    mouth.setFill("red")
    mouth.draw(win)
    mouth_line = Line(Point(130,275), Point(270,275))
    mouth_line.setWidth(2)
    mouth_line.draw(win)
    nose = Polygon(Point(200,180), Point(180,220), Point(220,220))
    nose.setFill("orange")
    nose.draw(win)
    input("Press <Enter> to close")
    win.close()
#face()

#7

def line_segment():
    win = GraphWin("Line Segment", 400, 400)
    win.setBackground("white")
    p1 = win.getMouse()
    p2 = win.getMouse()
    line = Line(p1, p2)
    line.setFill("black")
    line.setWidth(2)
    line.draw(win)
    mid_x = (p1.getX() + p2.getX()) / 2
    mid_y = (p1.getY() + p2.getY()) / 2
    mid_point = Point(mid_x, mid_y)
    mid = Circle(mid_point, 4)
    mid.setFill("cyan")  
    mid.draw(win)
    dx = p2.getX() - p1.getX()
    dy = p1.getY() - p2.getY() #I had to do this way because the y-axis is inverted in graphics.py
    slope = dy / dx if dx != 0 else float('inf')
    slope_text = Text(Point(200, 20), f"Slope: {slope:.2f}")
    slope_text.setTextColor("blue")
    slope_text.setSize(12)
    slope_text.setStyle("bold")
    slope_text.draw(win)
    length = math.sqrt(dx**2 + dy**2)
    length_text = Text(Point(200, 40), f"Length: {length:.2f}")
    length_text.setTextColor("red")
    length_text.setSize(12)
    length_text.setStyle("bold")
    length_text.draw(win)
    #Checking the coordinates of the points
    x1_text = Text(Point(p1.getX(), p1.getY()), f"({p1.getX():.1f}, {p1.getY():.1f})")
    x1_text.draw(win)
    x2_text = Text(Point(p2.getX(), p2.getY()), f"({p2.getX():.1f}, {p2.getY():.1f})")
    x2_text.draw(win)
    input("Press <Enter> to close")
    win.close()
#line_segment()