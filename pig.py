'''
Created on Apr 24, 2012
'testtest
@author: user
'''
import random

def main():
    print("Welcome to the PIG game.")
    print("You have the option of either playing a beginner or advanced player.")
    mode = 0
    while mode != 1 and mode != 2:
            mode = input("Please enter 1 for beginner, 2 for advanced.")
            if mode == 1:
                    startGame(1)
            if mode == 2:
                    startGame(2)
                    
def coinFlip():
    r = random.randint(1,2)
    return r

def startGame(mode):
    total1 = 0
    total2 = 0
    hold = 0
    flip = coinFlip()
    if mode == 1:
            hold = 3
    if mode == 2:
            hold = 5
    if flip == 1:
            print("You will start this game.")
            while total1 < 100 and total2 < 100:
                    total1 += humanTurn(total1)
                    print("Your point total is now " + total1.__str__() + ".")
                    if total1 >= 100:
                            break
                    total2 += computerTurn(total2, hold)
                    print("The computer's point total is now " + total2.__str__() + ".")
    if flip == 2:
            print("The computer will start this game.")
            while total1 < 100 and total2 < 100:
                    total2 += computerTurn(total2, hold)
                    print("The computer's point total is now " + total2.__str__() + ".")
                    if total2 >= 100:
                            break
                    total1 += humanTurn(total1)
                    print("Your point total is now " + total1.__str__() + ".")
    if total1 >= 100:
        print("You have won!")
    if total2 >= 100:
        print("The computer has won.")
    again = input("Would you like to play again? 1 for yes. 2 for no.")
    if again == 1:
        main()    
        
def humanTurn(total):
        newPoints = 0
        hold = 1
        while hold == 1:
                hold = input("Would you like to roll or hold? Enter 0 for hold. Enter 1 for roll.")
                if hold == 1:
                        result = roll() 
                        if result == 1:
                                newPoints = 0
                                print("You rolled a 1. You earn no points this turn.")
                                return newPoints
                        else:
                                newPoints += result
                                print("You rolled a " + result.__str__() + ". You now have earned " + newPoints.__str__() + " points this round.")   
                                if total + newPoints >= 100:
                                        return newPoints                 
        return newPoints
      
def computerTurn(total, holdCount):
    hold = 0
    newPoints = 0
    result = 0
    while hold != holdCount and result != 1:
            result = roll()
            if result == 1:
                    newPoints = 0
                    print("The computer rolled a 1. It loses all points from this round. It is now your turn.")
                    return newPoints
            else:
                    newPoints += result  
                    print("The computer rolled a " + result.__str__() + " It now has " + newPoints.__str__() + " new points this round.")
                    if total + newPoints >= 100:
                            return newPoints    
            hold = hold + 1
    print("The computer decides to hold.")    
    return newPoints
              
def roll():
    points = random.randint(1,6)
    return points
    
main()
