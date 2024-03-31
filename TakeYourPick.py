#Take Your Pick is a simple game where the user is asked to choose between two options. The user is given a choice between two options and must choose one. The game will keep track of the user's choices and display the results at the end. The game will be implemented using Python and will be run in the terminal.

import random

#Introduction
print("Welcome to Take Your Pick!")
name = input("What is your name? ")
print("Hello, " + name + "! Let's play a game. You will be given a series of choices and you must choose one. Let's begin!")


#Function for first, second, and third choices
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

#Call starting function
first()

#Next 8 functions are options for fourth, fifth, and sixth choices
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


#Options for fourth, fifth, and sixth choices
def choice2():
    print("You chose red, yellow, and 2.")
    r4 = input("magic or time travel: ")
    while True:
        if r4.lower() == "magic":
            r5 = input("fire or ice: ")
            while True:
                if r5.lower() == "fire":
                    r6 = input("diamonds or all other gems: ")
                    while True:
                        if r6.lower() == "diamonds":
                            p
                        elif r6.lower() == "all other gems":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("diamonds or all other gems: ")
                elif r5.lower() == "ice":
                    r6 = input("lightning or thunder: ")
                    while True:
                        if r6.lower() == "lightning":
                            p
                        elif r6.lower() == "thunder":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("lightning or thunder: ")
                else:
                    print("Invalid input. Please try again.")
                    r5 = input("fire or ice: ")
        elif r4.lower() == "time travel":
            r5 = input("past or future: ")
            while True:
                if r5.lower() == "past":
                    r6 = input("pb&j or grilled cheese: ")
                    while True:
                        if r6.lower() == "pb&j":
                            p
                        elif r6.lower() == "grilled cheese":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("pb&j or grilled cheese: ")
                elif r5.lower() == "future":
                    r6 = input("cursive or print: ")
                    while True:
                        if r6.lower() == "cursive":
                            p
                        elif r6.lower() == "print":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("cursive or print: ")
                else:
                    print("Invalid input. Please try again.")
                    r5 = input("past or future: ")
        else:
            print("Invalid input. Please try again.")
            r4 = input("magic or time travel: ")


#Options for fourth, fifth, and sixth choices
def choice3():
    print("You chose red, orange, and 3.")
    r4 = input("deep space or deep ocean: ")
    while True:
        if r4.lower() == "deep space":
            r5 = input("stars or planet: ")
            while True:
                if r5.lower() == "stars":
                    r6 = input("lion or tiger: ")
                    while True:
                        if r6.lower() == "lion":
                            p
                        elif r6.lower() == "tiger":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("lion or tiger: ")
                elif r5.lower() == "planet":
                    r6 = input("Jupiter or Saturn: ")
                    while True:
                        if r6.lower() == "Jupiter":
                            p
                        elif r6.lower() == "Saturn":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("Jupiter or Saturn: ")
                else:
                    print("Invalid input. Please try again.")
                    r5 = input("stars or planet: ")
        elif r4.lower() == "deep ocean":
            r5 = input("octopus or squid: ")
            while True:
                if r5.lower() == "octopus":
                    r6 = input("longer life with a smaller brain or shorter life with a larger brain: ")
                    while True:
                        if r6.lower() == "longer life with a smaller brain":
                            ran_num = random.randint(1, 8)
                            p
                        elif r6.lower() == "shorter life with a larger brain":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("longer life with a smaller brain or shorter life with a larger brain: ")
                elif r5.lower() == "squid":
                    r6 = input("butter or salt & pepper: ")
                    while True:
                        if r6.lower() == "butter":
                            p
                        elif r6.lower() == "salt & pepper":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("butter or salt & pepper: ")
                else:
                    print("Invalid input. Please try again.")
                    r5 = input("octopus or squid: ")
        else:
            print("Invalid input. Please try again.")
            r4 = input("deep space or deep ocean: ")


#Options for fourth, fifth, and sixth choices
def choice4():
    print("You chose red, orange, and 4.")
    r4 = input("mountain or beach: ")
    while True:
        if r4.lower() == "mountain":
            r5 = input("east or west: ")
            while True:
                if r5.lower() == "east":
                    r6 = input("centaur or minotaur: ")
                    while True:
                        if r6.lower() == "centaur":
                            p
                        elif r6.lower() == "minotaur":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("centaur or minotaur: ")
                elif r5.lower() == "west":
                    r6 = input("tornado or hurricane: ")
                    while True:
                        if r6.lower() == "tornado":
                            p
                        elif r6.lower() == "hurricane":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("tornado or hurricane: ")
                else:
                    print("Invalid input. Please try again.")
                    r5 = input("east or west: ")
        elif r4.lower() == "beach":
            r5 = input("sand or surf: ")
            while True:
                if r5.lower() == "sand":
                    r6 = input("camping or rafting: ")
                    while True:
                        if r6.lower() == "camping":
                            p
                        elif r6.lower() == "rafting":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("camping or rafting: ")
                elif r5.lower() == "surf":
                    r6 = input("surfing or snowboarding: ")
                    while True:
                        if r6.lower() == "surfing":
                            p
                        elif r6.lower() == "snowboarding":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("surfing or snowboarding: ")
                else:
                    print("Invalid input. Please try again.")
                    r5 = input("sand or surf: ")
        else:
            print("Invalid input. Please try again.")
            r4 = input("mountain or beach: ")


#Options for fourth, fifth, and sixth choices
def choice5():
    print("You chose blue, purple, and 5.")
    r4 = input("fly or teleport: ")
    while True:
        if r4.lower() == "fly":
            r5 = input("plane or wings: ")
            while True:
                if r5.lower() == "plane":
                    print("I'm sorry. You must go back to the beginning.")
                    return first()
                elif r5.lower() == "wings":
                    r6 = input("phoenix or griffin: ")
                    while True:
                        if r6.lower() == "phoenix":
                            p
                        elif r6.lower() == "griffin":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("phoenix or griffin: ")
                else:
                    print("Invalid input. Please try again.")
                    r5 = input("plane or wings: ")
        elif r4.lower() == "teleport":
            r5 = input("high or low: ")
            while True:
                if r5.lower() == "high":
                    r6 = input("strawberries or blueberries: ")
                    while True:
                        if r6.lower() == "strawberries":
                            p
                        elif r6.lower() == "blueberries":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("strawberries or blueberries: ")
                elif r5.lower() == "low":
                    r6 = input("garlic or onion: ")
                    while True:
                        if r6.lower() == "garlic":
                            p
                        elif r6.lower() == "onion":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("garlic or onion: ")
                else:
                    print("Invalid input. Please try again.")
                    r5 = input("high or low: ")
        else:
            print("Invalid input. Please try again.")
            r4 = input("fly or teleport: ")


#Options for fourth, fifth, and sixth choices
def choice6():
    print("You chose blue, purple, and 6.")
    r4 = input("Lamborghini or Ferrari: ")
    while True:
        if r4.lower() == "Lamborghini":
            r5 = input("classic or new: ")
            while True:
                if r5.lower() == "classic":
                    r6 = input("dogs or cats: ")
                    while True:
                        if r6.lower() == "dogs":
                            p
                        elif r6.lower() == "cats":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("dogs or cats: ")
                elif r5.lower() == "new":
                    r6 = input("shark or whale: ")
                    while True:
                        if r6.lower() == "shark":
                            p
                        elif r6.lower() == "whale":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("shark or whale: ")
                else:
                    print("Invalid input. Please try again.")
                    r5 = input("classic or new: ")
        elif r4.lower() == "Ferrari":
            r5 = input("race or auto show: ")
            while True:
                if r5.lower() == "race":
                    r6 = input("orca or dolphin: ")
                    while True:
                        if r6.lower() == "orca":
                            p
                        elif r6.lower() == "dolphin":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("orca or dolphin: ")
                elif r5.lower() == "auto show":
                    print("Pick a number between 1 - 8: ")
                    p
                else:
                    print("Invalid input. Please try again.")
                    r5 = input("race or auto show: ")
        else:
            print("Invalid input. Please try again.")
            r4 = input("Lamborghini or Ferrari: ")


#Options for fourth, fifth, and sixth choices
def choice7():
    print("You chose blue, green, and 7.")  
    r4 = input("hot or cold: ")
    while True:
        if r4.lower() == "hot":
            r5 = input("the Amazon or the Sahara: ")
            while True:
                if r5.lower() == "the Amazon":
                    r6 = input("gorilla or chimpanzee: ")
                    while True:
                        if r6.lower() == "gorilla":
                            p
                        elif r6.lower() == "chimpanzee":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("gorilla or chimpanzee: ")
                elif r5.lower() == "the Sahara":
                    r6 = input("crocodiles or turtles: ")
                    while True:
                        if r6.lower() == "crocodiles":
                            p
                        elif r6.lower() == "turtles":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("crocodiles or turtles: ")
                else:
                    print("Invalid input. Please try again.")
                    r5 = input("the Amazon or the Sahara: ")
        elif r4.lower() == "cold":
            r5 = input("Antarctica or the North Pole: ")
            while True:
                if r5.lower() == "Antarctica":
                    r6 = input("penguins or beluga whales: ")
                    while True:
                        if r6.lower() == "penguins":
                            p
                        elif r6.lower() == "beluga whales":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("penguins or beluga whales: ")
                elif r5.lower() == "the North Pole":
                    r6 = input("Santa or elves: ")
                    while True:
                        if r6.lower() == "Santa":
                            p
                        elif r6.lower() == "elves":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("Santa or elves: ")
                else:
                    print("Invalid input. Please try again.")
                    r5 = input("Antarctica or the North Pole: ")
        else:
            print("Invalid input. Please try again.")
            r4 = input("hot or cold: ")


#Final options for fourth, fifth, and sixth choices
def choice8():
    print("You chose blue, green, and 8.")  
    r4 = input("salty or sweet: ")
    while True:
        if r4.lower() == "salty":
            r5 = input("popcorn or chips: ")
            while True:
                if r5.lower() == "popcorn":
                    r6 = input("movies or TV shows: ")
                    while True:
                        if r6.lower() == "movies":
                            p
                        elif r6.lower() == "TV shows":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("movies or TV shows: ")
                elif r5.lower() == "chips":
                    r6 = input("sandwiches or burgers: ")
                    while True:
                        if r6.lower() == "sandwiches":
                            p
                        elif r6.lower() == "burgers":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("sandwiches or burgers: ")
                else:
                    print("Invalid input. Please try again.")
                    r5 = input("popcorn or chips: ")
        elif r4.lower() == "sweet":
            r5 = input("cake or pie: ")
            while True:
                if r5.lower() == "cake":
                    ran_num = random.randint(1, 8)
                    p
                elif r5.lower() == "pie":
                    r6 = input("snacks or desserts: ")
                    while True:
                        if r6.lower() == "snacks":
                            p
                        elif r6.lower() == "desserts":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input("snacks or desserts: ")
                else:
                    print("Invalid input. Please try again.")
                    r5 = input("cake or pie: ")
        else:
            print("Invalid input. Please try again.")
            r4 = input("salty or sweet: ")







#Function choice template
r4 = input(": ")
    while True:
        if r4.lower() == "":
            r5 = input(": ")
            while True:
                if r5.lower() == "":
                    r6 = input(": ")
                    while True:
                        if r6.lower() == "":
                            p
                        elif r6.lower() == "":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input(": ")
                elif r5.lower() == "":
                    r6 = input(": ")
                    while True:
                        if r6.lower() == "":
                            p
                        elif r6.lower() == "":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input(": ")
                else:
                    print("Invalid input. Please try again.")
                    r5 = input(": ")
        elif r4.lower() == "":
            r5 = input(": ")
            while True:
                if r5.lower() == "":
                    r6 = input(": ")
                    while True:
                        if r6.lower() == "":
                            p
                        elif r6.lower() == "":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input(": ")
                elif r5.lower() == "":
                    r6 = input(": ")
                    while True:
                        if r6.lower() == "":
                            p
                        elif r6.lower() == "":
                            p
                        else:
                            print("Invalid input. Please try again.")
                            r6 = input(": ")
                else:
                    print("Invalid input. Please try again.")
                    r5 = input(": ")
        else:
            print("Invalid input. Please try again.")
            r4 = input(": ")


   




