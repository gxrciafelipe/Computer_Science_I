#Felipe Garcia
#Computer Science 1
#31 August 2025
#Homework 1

#2)
#a. The difference is that the first print prints the entire message, including the comma, whereas the second one the comma represents a space between the two words and it's not shown on the terminal.
#b. The first print prints the integer 3, and the second one prints 3.0 which is a floating point number.
#c. The first prints the integer sum between 2 and 3, which is 5, the second prints the floating sum, which is 5.0, and the last one prints the concatenation of the two strings "2" and "3", which is "23".
#d. The first prints the multiplication of 2 and 3, and the second one prints 2 raised to the power of 3, which is 8.
#e. The first prints the division of 7 and 3, which is 2.333..., and the second one prints the integer division of 2 and 3, which is 0. (If it was 2/3 it would be 0.666...)

#3)
#Chaos function
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print?  "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)

main()

#4)
#km to miles converter
def km_to_miles():
    print("This program converts kilometers to miles")
    km = eval(input("Enter a distance in kilometers: "))
    miles = km * 0.62
    print(km, "kilometers is", miles, "miles.")

km_to_miles()

#5)
#Execise #5 from Chapter 2
def compound_interest():
    p = 10000
    n = 12
    r = 0.08
    t = eval(input("Enter the number of years the money will be compounded for: "))
    print("The amount after", t, "years is:", p * (1 + r/n)**(n*t))

compound_interest()
