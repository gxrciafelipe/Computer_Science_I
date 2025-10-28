#Felipe Garcia
#Homework 5
#29 September 2025
from graphics import *
import math

#Problem 1
#old macdonald
def animal(name, sound):
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    print("And on that farm he had a " + name + ", Ee-igh, Ee-igh, Oh!")
    print("With a " + sound + ", " + sound + " here and a " + sound + ", " + sound + " there")
    print("Here a " + sound + ", there a " + sound + ", everywhere a " + sound + ", " + sound)
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    print()

def song():
    animal("cow", "moo")
    animal("pig", "oink")
    animal("duck", "quack")
    animal("cat", "meow")
    animal("dog", "woof")

#song() #uncomment to run the song

#Problem 2
#avg of numbers
def avg(numbers):
    total = 0
    for n in range(numbers):
        number=int(input("Please enter a number: "))
        total += number
    return float(total / numbers)

def user():
    numbers = int(input("Please enter the amount of numbers you want to average (Other than 0): "))
    print("The average of the numbers you input is " + str(avg(numbers)))

#user() #uncomment to run the user function

#Problem 3

def slopefunction(dx, dy):
    if dx == 0:
        raise ValueError("dx cannot be zero")
    return dy / dx

def distance(dx, dy):
    return math.sqrt(dx**2 + dy**2)

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
    slope = slopefunction(dx, dy)
    slope_text = Text(Point(200, 20), f"Slope: {slope:.2f}")
    slope_text.setTextColor("blue")
    slope_text.setSize(12)
    slope_text.setStyle("bold")
    slope_text.draw(win)
    length = distance(dx, dy)
    length_text = Text(Point(200, 40), f"Length: {length:.2f}")
    length_text.setTextColor("red")
    length_text.setSize(12)
    length_text.setStyle("bold")
    length_text.draw(win)
    #Checking the coordinates of the points
    #x1_text = Text(Point(p1.getX(), p1.getY()), f"({p1.getX():.1f}, {p1.getY():.1f})")
    #x1_text.draw(win)
    #x2_text = Text(Point(p2.getX(), p2.getY()), f"({p2.getX():.1f}, {p2.getY():.1f})")
    #x2_text.draw(win)
    input("Press <Enter> to close")
    win.close()

#line_segment() #uncomment to run the line segment function

#Problem 4
def sumList(nums):
    total = 0
    for n in nums:
        total += n
    return total

def mainsumList():
    nums = []
    count = int(input("Please enter the amount of numbers you want to sum (Other than 0): "))
    if count <= 0:
        raise ValueError("count must be > 0")
    for x in range(count):
        number = int(input("Please enter a number: "))
        nums.append(number)
    print("The sum of the numbers you input is " + str(sumList(nums)))

#mainsumList() #uncomment to run the mainsumList function

#Problem 5
def get_some_strings(count):
    strings = []
    if count <= 0:
        raise ValueError("count must be > 0")
    for x in range(count):
        string = input("Please enter a string: ")
        strings.append(string)
    return strings

def main_get_some_strings():
    count = int(input("Please enter the amount of strings you want to input: "))
    strings = get_some_strings(count)
    print("The strings you input are: ")
    for s in strings:
        print(s)
#main_get_some_strings() #uncomment to run the main_get_some_strings function