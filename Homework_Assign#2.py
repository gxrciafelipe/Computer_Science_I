#Felipe Garcia
#Computer Science 1
#05 September 2025
#Homework 2
import math

#1.
#a)
for i in range (5) :
    print (i * i)
    #OUTPUT: 
    # 0
    # 1
    # 4
    # 9
    # 16
#b)
for d in [3,1,4,1,5]:
    print (d, end=" ")
    #OUTPUT: 3 1 4 1 5
#c)
for i in range (4) :
    print ("Hello")
    #OUTPUT: Hello
    #        Hello
    #        Hello
    #        Hello
#d)
for i in range (5) :      
    print (i, 2 **i)
    #OUTPUT: 0 1
    #        1 2
    #        2 4
    #        3 8
    #        4 16
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#2.
#a
print (4.0 / 10.0 + 3.5 * 2)
    #OUTPUT: 7.4 (FLOAT)   
#c
print (abs(4 - 20 // 3) ** 3)
    #OUTPUT: 8 (INTEGER)
#e
print (3 * 10 // 3 + 10 % 3)
    #OUTPUT: 11 (INTEGER)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#3.
#b
    #n*(n-1)/2

#c
    #4*math.pi*r**2
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#4.
#b
for i in [1,3,5,7,9]:
    print (i, ":", i**3)
print (i)
    #OUTPUT: 
    #1 : 1
    #3 : 27
    #5 : 125    
    #7 : 343
    #9 : 729
    #9   
#c
x = 2
y = 10
for j in range (0, y, x) :
    print (j, end="")
    print (x + y)
print ("done")
    #OUTPUT:
    #012
    #212
    #412
    #612
    #812
    #done
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#5.
#Program to calculate the slope of a line
def slope():
    print("Enter the first point (x1, y1):")
    x1 = eval(input("x1: "))
    y1 = eval(input("y1: "))
    print("Enter the second point (x2, y2):")
    x2 = eval(input("x2: "))
    y2 = eval(input("y2: "))
    slope = (y2 - y1) / (x2 - x1)
    print("The slope of the line between the points (", x1, ",", y1, ") and (",x2, ",",y2, ") is: ", slope)
slope()
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#6.
#Program to calculate the distance between two points
def distance():
    print("Enter the first point (x1, y1):")
    x1 = eval(input("x1: "))
    y1 = eval(input("y1: "))
    print("Enter the second point (x2, y2):")
    x2 = eval(input("x2: "))
    y2 = eval(input("y2: "))
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("The distance between the points (", x1, ",", y1, ") and (",x2, ",",y2, ") is: ", distance)
distance()
