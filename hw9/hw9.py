#Felipe Garcia
#Homework 8
#10 November 2025

import math

#1.
    #1) True
    #2) False
    #3) False
    #4) False
    #5) False

#2.
    #1) b
    #2) c
    #3) d
    #4) b
    #5) c

#3. Explain the similarities and differences between instance variables and "regular" function variables.
#Instance variables and regular function variables are similar because both are used to store data while a program runs.
#They can hold values like numbers, strings, or lists, and both follow the same basic rules for assigning and using data in Python.
#However, they differ in where and how long they exist. Regular function variables are created inside a function and only exist while that function is running,
#they’re temporary and only accessible within that function’s scope. Instance variables, on the other hand, belong to a specific object created from a class. 
#They keep their values as long as the object exists and can be accessed by any method in that class using self. 
#So, while regular variables are short-lived and limited in scope, instance variables are tied to objects and help store information that defines the state of that object.

#4.
class Spheres:
    def __init__ (self, radius):
        self.radius = radius
    def getRadius(self):
        return self.radius
    def surfaceArea(self):
        return 4 * math.pi * self.radius ** 2
    def volume(self):
        return (4/3) * math.pi * self.radius ** 3
    
def main():
    r = float(input("Enter the radius of the sphere: "))
    sphere = Spheres(r)
    print(f"Radius: {sphere.getRadius()}")
    print(f"Surface Area: {sphere.surfaceArea():.2f}") 
    print(f"Volume: {sphere.volume():.2f}")

if __name__ == "__main__":
    main()

#5. Django website
#https://garciafelipe.pythonanywhere.com/