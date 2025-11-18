#Felipe Garcia
#Homework 10
#17 November 2025

#1)
#s1 = [2, 1, 4, 3]
#s2 = ['c', 'a', 'b']

    #a) s1 + s2
        #[2, 1, 4, 3, 'c', 'a', 'b']

    #b) 3 * s1 + 2 * s2
        #[2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 'c', 'a', 'b', 'c', 'a', 'b']

    #c) s1[1]
        #1

    #d) s1[1:3]
        #[1, 4]

    #e) s1 + s2[-1]
        #TypeError: can only concatenate list (not "str") to list


#2)
#Write and test a function shuffle(myList) that scrambles a list into a
#random order, like shuffling a deck of cards
import random
def shuffle(myList):
    random.shuffle(myList)
    return myList
#print(shuffle(['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'])) #uncomment to test the function


#3)
#Write and test a function removeDuplicates(somelist) that 
#removes duplicate values from a list
def removeDuplicates(somelist):
    noDuplicates = []
    for item in somelist:
        if item not in noDuplicates:
            noDuplicates.append(item)
    return noDuplicates
#print(removeDuplicates([1, 2, 2, 2, 3, 4, 4, 5, 1, 6, 7, 8, 8])) #uncomment to test the function

#4)
#   garciafelipe.pythonanywhere.com