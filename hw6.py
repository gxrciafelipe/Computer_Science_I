#Felipe Garcia
#Computer Science 1
#4 October 2023

#1) The use of exception handling like "try-except" is different from using conditional statements like "if-else" in that exception handling is used to manage errors that occur during the execution of a program, mainly rare erros, while conditional statements are used to control the flow of a program based on certain conditions. Exception handling allows you to catch and handle errors gracefully, preventing the program from crashing, whereas conditional statements allow you to make decisions based on specific criteria. I feel like it is also more professional than to use a bunch of elif's.
# They are similar in that they both makes the program have different pathways based on certain conditions. Both can be used to improve the robustness and reliability of a program.

#2)
# Program to convert grades to letter grades
def convert_grade():
    grade = float(input("Enter your grade (0-100): "))
    if grade < 0:
        print ("Error: Grade cannot be negative.")
    elif grade < 60:
        print("Your letter grade is: F")
    elif grade >= 60 and grade < 70:
        print("Your letter grade is: D")
    elif grade >= 70 and grade < 80:
        print("Your letter grade is: C")
    elif grade >= 80 and grade < 90:
        print("Your letter grade is: B")
    else: #sometimes grade is more than 100 due to extra credits so if that happens it will still give an A
        print("Your letter grade is: A")

#convert_grade() #uncomment this line to run the function

#3)
# Program that calculates the total bill of a babysitter

def babysitter_bill():
    try:
        start_time = input("Enter the start time (in 24-hour format HH:MM): ")
        start_hour, start_minute = start_time.split(':')
        start_time = float(start_hour) + float(start_minute) / 60
        end_time = input("Enter the end time (in 24-hour format HH:MM): ")
        end_hour, end_minute = end_time.split(':')
        end_time = float(end_hour) + float(end_minute) / 60
        
        if float(end_minute) < 0 or float(end_minute) >= 60 or float(start_minute) < 0 or float(start_minute) >= 60:
            print("Error: Minutes must be between 0 and 59.")
            return

        if start_time < 6 or end_time > 24 or start_time >= end_time:
            print("Error: Invalid time range. Start time must be after 6 am, and end time must be after start time.")
            return
        
        total_bill = 0
        
        if start_time < 21 and end_time <= 21:
            hours = end_time - start_time
            total_bill = hours * 2.50
        elif start_time < 21 and end_time > 21:
            hours_before_21 = 21 - start_time
            hours_after_21 = end_time - 21
            total_bill = (hours_before_21 * 2.50) + (hours_after_21 * 1.75)
        elif start_time >= 21:
            hours = end_time - start_time
            total_bill = hours * 1.75
        
        print(f"Total babysitting bill: ${total_bill}")
    
    except ValueError:
        print("Error: Please enter valid integer times.")

#babysitter_bill() #uncomment this line to run the function

#4)
# Eligibility for the Senate and the House
def check_eligibility():
    age = int(input("Enter your age: "))
    years = int(input("Enter the number of years you have been a U.S. citizen: "))
    if age >= 30 and years >= 9:
        print("You are eligible to be a US Senator!")
    else:
        print("Sorry, you are not eligible to be a US Senator yet!")
    if age >= 25 and years >= 7:
        print("You are eligible to be a US Representative!")
    else:
        print("Sorry, you are not eligible to be a US Representative yet!")

#check_eligibility() #uncomment this line to run the fucntion

#5)
def sumList(nums):
    total = 0
    for n in nums:
        total += n
    return total

def mainsumList():
    nums = []
    try:
        count = int(input("Please enter the amount of numbers you want to sum (Other than 0): "))
        if count <= 0:
            raise ValueError("non_positive") #If the amount of numbers is not greater than 0 raise this label
        for x in range(count):
            number = int(input("Please enter a number: "))
            nums.append(number)
        print("The sum of the numbers you input is " + str(sumList(nums)))
    except ValueError as e:
        #Handle two different runtime errors
        if str(e) == "non_positive": #Message if the amount of numbers <= 0
            print("Error: Please enter a number greater than 0 for the amount.")
        else: #Message if the input is not an integer
            print("Error: Please enter a valid integer for the amount of numbers.")

#mainsumList() #uncomment to run the mainsumList function
