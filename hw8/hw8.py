#Felipe Garcia
#Homework 8
#31 October 2025

#1 In the .vsdx file

#2
#racketball with alternating first server
from random import random
def main():
    printlntro()
    probA, probB, n = getlnputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)
def printlntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. The servers alternate each game.")
def getlnputs():
    # Returns the three simulation parameters
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n
def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB
def simOneGame(probA, probB):
    # Simulates a single game or racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB
def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    return a== 15 or b== 15
def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1: 0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1: 0.1%})".format(winsB, winsB/n))
#main() #uncomment to run the function

#3
#racketball with shutouts, pct of wins that are shutouts
from random import random
def main_2():
    printlntro_2()
    probA, probB, n = getlnputs_2()
    winsA, winsB, shutA, shutB = simNGames_2(n, probA, probB)
    printSummary_2(winsA, winsB, shutA, shutB)
def printlntro_2():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")
def getlnputs_2():
    # Returns the three simulation parameters
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n
def simNGames_2(n, probA, probB):
    winsA = winsB = shutA = shutB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame_2(probA, probB)

        if scoreA > scoreB:
            winsA += 1
            if scoreB == 0:  # A shutout
                shutA += 1
        else:
            winsB += 1
            if scoreA == 0:  # B shutout
                shutB += 1

    return winsA, winsB, shutA, shutB
def simOneGame_2(probA, probB):
    # Simulates a single game or racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver_2(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB
def gameOver_2(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    return a== 15 or b== 15
def printSummary_2(winsA, winsB, shutA, shutB):
    n = winsA + winsB
    print("\nGames simulated:", n)
    print(f"Wins for A: {winsA} ({winsA/n:0.1%})")
    print(f"Wins for B: {winsB} ({winsB/n:0.1%})")

    if winsA > 0:
        print(f"Shutouts for A: {shutA} ({shutA/winsA:0.1%} of A's wins)")
    else:
        print("Shutouts for A: 0 (0.0%)")

    if winsB > 0:
        print(f"Shutouts for B: {shutB} ({shutB/winsB:0.1%} of B's wins)")
    else:
        print("Shutouts for B: 0 (0.0%)")
#main_2() #uncomment to run the function

#4
#An API (Application Programming Interface) is basically a set of rules that lets different software systems talk to each other.
#The API makes sure both sides understand each other without needing to know how everything works behind the scenes.
#APIs interacts with endpoints, which are specific points of interaction in the API where requests are made and responses are received.
#The endpoints are more specific aspects of a given API that allow the client to access particular functions provided by the API.
#An example of an API could be using the Google Maps API to show your companie's address in the map in your companie's website.

#5
#A language is a set of commands with syntax and semantics, kind of tools, that can be used to create software applications.
#A framework is a pre-built collection of code, built with a language, that makes it easier to build apllications by providing structure and reusable components.
#Example of framework and its underlying language: Rails is a framework built on Ruby programming language.
#Example of a real world company using Django: Instagram uses Django as its web framework.