#Felipe Garcia
#Homework 4
#20 September 2025

#Chapter #5 - Discussion Problem #1
s1="spam"
s2="ni!"
#c
s1[1] 
#output p

#e
s1[2]+s2[:2] 
#output ani

#g
s1.upper() 
#output SPAM 

#Chapter #5 - Discussion Problem #2
#a
s2[:2].upper()
#output NI

#d
s1[:]
#ouput spam

#e
list = [s1[:2], s1[3]]
#ouput ['sp', 'm']

#Chapter #5 - Discussion Problem #3
#b
def ch5_3b():
    for w in "Now is the winter of our discontent...".split():
        print(w)
#ch5_3b()
#output
#Now
#is
#the
#winter
#of
#our
#discontent...

#c
def ch5_3c():
    for w in "Mississippi".split("i"):
        print(w, end=" ")
#ch5_3c()
#output
#M ss ss pp

#e
def ch5_3e():
    msg = ""
    for ch in "secret":
        msg = msg + chr(ord(ch)+1)
    print(msg)
#ch5_3e()
#output 
#tfdsfu

#Write a program that uses five definite loops to produce the following single line of output exactly as specified below
def five_definite_loops():
    print('grades = "', end='')
    for i in range(60):
        print('F', end='')
    for i in range(10):
        print('D', end='')
    for i in range(10):
        print('C', end='')
    for i in range(10):
        print('B', end='')
    for i in range(10):
        print('A', end='')
    print('"', end='')
#five_definite_loops()

#Chapter #5 - Programming Exercise #3
#Program to convert exam scores into letter grades using string indexing.
def ch5_pe3():
    score = int(input("Enter exam score (0-100): "))
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        grades = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDDDDDDDDDDCCCCCCCCCCBBBBBBBBBBAAAAAAAAAAA"
        print("The letter grade for", score, "is", grades[score])
#ch5_pe3()

#Chapter #5 - Programming Exercise #4
#Program that makes an acronym based on a phrase
def ch5_pe4():
    phrase = input("Enter a phrase: ")
    print("The acronym for that phrase is: ", end="")
    for ch in phrase.split():
        print(ch[0].upper(), end="")
#ch5_pe4()

#Chapter #5 - Programming Exercise #5
#Program that tells the numeric value of a name
def ch5_pe5():
    name = input("Enter a single name: ")
    total = 0
    for ch in name.lower():
        if 'a' <= ch <= 'z':
            total += ord(ch) - ord('a') + 1
    print("The numeric value of the name", name, "is:", total)
#ch5_pe5()