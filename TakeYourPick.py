#Take Your Pick is a simple game where the user is asked to choose between two options. The user is given a choice between two options and must choose one. The game will keep track of the user's choices and display the results at the end. The game will be implemented using Python and will be run in the terminal.

import random

#Introduction
print("Welcome to Take Your Pick!")


#First, second, and third choices
def first():
    r1 = input("red or blue: ")
    while True:
        if r1.lower() == "red":
            r2 = input("yellow or orange: ")
            while True:
                if r2.lower() == "yellow":
                    r3 = input("1 or 2: ")
                    while True:
                        if r3 == "1":
                            return choice1()
                        elif r3 == "2":
                            return choice2()
                        else:
                            print("Invalid input. Please try again.")
                            r3 = input("1 or 2: ")
                elif r2.lower() == "orange":
                    r3 = input("3 or 4: ")
                    while True:
                        if r3 == "3":
                            return choice3()
                        elif r3 == "4":
                            return choice4()
                        else:
                            print("Invalid input. Please try again.")
                            r3 = input("3 or 4: ")
                else:
                    print("Invalid input. Please try again.")
                    r2 = input("yellow or orange: ")
        elif r1.lower() == "blue":
            r2 = input("purple or green: ")
            while True:
                if r2.lower() == "purple":
                    r3 = input("5 or 6: ")
                    while True:
                        if r3 == "5":
                            return choice5()
                        elif r3 == "6":
                            return choice6()
                        else:
                            print("Invalid input. Please try again.")
                            r3 = input("5 or 6: ")
                elif r2.lower() == "green":
                    r3 = input("7 or 8: ")
                    while True:
                        if r3 == "7":
                            return choice7()
                        elif r3 == "8":
                            return choice8()
                        else:
                            print("Invalid input. Please try again.")
                            r3 = input("7 or 8: ")
                else:
                    print("Invalid input. Please try again.")
                    r2 = input("purple or green: ")
        else:
            print("Invalid input. Please try again.")
            r1 = input("red or blue: ")


def choice1():
    print("You chose red, yellow, and 1.")
    r4 = input("sun or moon: ")
    while True:
        if r4.lower() == "sun":
            r5 = input("left or right: ")
            while True:
                if r5.lower() == "left":
                    r6 = input("solo or team: ")
                    while True:
                        if r6.lower() == "solo":
                            p
                        elif r6.lower() == "team":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("solo or team: ")
                elif r5.lower() == "right":
                    r6 = input("skating or biking: ")
                    while True:
                        if r6.lower() == "skating":
                            p
                        elif r6.lower() == "biking":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("skating or biking: ")
                else:
                    print("Invalid input. Please try again.")
                    r5 = input("left or right: ")
        elif r4.lower() == "moon":
            r5 = input("werewolf or vampire: ")
            while True:
                if r5.lower() == "werewolf":
                    r6 = input("gold or silver: ")
                    while True:
                        if r6.lower() == "gold":
                            p
                        elif r6.lower() == "silver":
                            print("I'm sorry. You must go back to the beginning.")
                            return first()
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("gold or silver: ")
                elif r5.lower() == "vampire":
                    r6 = input("speed or strength: ")
                    while True:
                        if r6.lower() == "speed":
                            p
                        elif r6.lower() == "strength":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("speed or strength: ")
                else:
                    print("Invalid input. Please try again.")
                    r5 = input("werewolf or vampire: ")
        else:
            print("Invalid input. Please try again.")
            r4 = input("sun or moon: ")

def choice2():
    print("You chose red, yellow, and 2.")


def choice3():
    print("You chose red, orange, and 3.")


def choice4():
    print("You chose red, orange, and 4.")


def choice5():
    print("You chose blue, purple, and 5.")


def choice6():
    print("You chose blue, purple, and 6.")


def choice7():
    print("You chose blue, green, and 7.")  


def choice8():
    print("You chose blue, green, and 8.")  





   




