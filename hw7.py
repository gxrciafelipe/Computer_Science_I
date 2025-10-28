#Felipe Garcia
#Computer Science 1
#Homework 7
#27 October 2025

#1. I did it in the word file

#2. I did it in the word file

#3. 
#a) sum of the first n counting numbers w/ while
def sum_n(n):
    total = 0
    count = 1
    while count <= n:
        total += count
        count += 1
    return total
#print(sum_n(5)) #Uncomment to run the function

#c) Sum of a series of numbers entered by the user until the value 999 is entered.
def sum_til_999():
    total = 0
    num = float(input("Enter a number (999 to stop): "))
    while num != 999:
        total += num
        num = float(input("Enter a number (999 to stop): "))
    print("The total sum is:", total)
#sum_til_999() #Uncomment to run the function

# Programming Exercise 1
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
#n = int(input("Enter the position of the number you want to know in the Fibonacci sequence: ")) #Uncomment to run the function
#print(f"The number at position {n} in the Fibonacci sequence is: {fibonacci(n)}") #Uncomment to run the function

# Programming Exercise 4
def syracuse(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence
#num = int(input("Enter a positive integer to generate its Syracuse sequence: ")) #Uncomment to run the function
=======
#Felipe Garcia
#Computer Science 1
#Homework 7
#27 October 2025

#1. I did it in the word file

#2. I did it in the word file

#3. 
#a) sum of the first n counting numbers w/ while
def sum_n(n):
    total = 0
    count = 1
    while count <= n:
        total += count
        count += 1
    return total
#print(sum_n(5)) #Uncomment to run the function

#c) Sum of a series of numbers entered by the user until the value 999 is entered.
def sum_til_999():
    total = 0
    num = float(input("Enter a number (999 to stop): "))
    while num != 999:
        total += num
        num = float(input("Enter a number (999 to stop): "))
    print("The total sum is:", total)
#sum_til_999() #Uncomment to run the function

# Programming Exercise 1
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
#n = int(input("Enter the position of the number you want to know in the Fibonacci sequence: ")) #Uncomment to run the function
#print(f"The number at position {n} in the Fibonacci sequence is: {fibonacci(n)}") #Uncomment to run the function

# Programming Exercise 4
def syracuse(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence
#num = int(input("Enter a positive integer to generate its Syracuse sequence: ")) #Uncomment to run the function
#print("The Syracuse sequence is:", syracuse(num)) #Uncomment to run the function