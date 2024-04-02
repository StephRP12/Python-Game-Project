#File for testing purposes only. Not the final version of the game.

import random

#Lists of all possible choices and fates
choices = [('sun', 'moon'), ('magic', 'time travel'), ('deep space', 'deep ocean'), ('mountains', 'seaside'), ('fly', 'teleport'), ('Lamborghini', 'Ferrari'), ('hot', 'cold'), 
           ('salty', 'sweet'), ('left', 'right'), ('werewolf', 'vampire'), ('fire', 'ice'), ('past', 'future'), ('stars', 'planets'), ('octopus', 'squid'), ('east', 'west'),
           ('sand', 'surf'), ('plane', 'wings'), ('high', 'low'), ('classic', 'new'), ('jungle', 'desert'), ('North Pole', 'South Pole'), ('popcorn', 'chips'), ('cake', 'pie'), 
           ('solo', 'group'), ('sing', 'dance'), ('read', 'write'), ('now', 'later'), ('long', 'short'), ('milkshake', 'smoothie'), ('birds', 'bees'), ('north', 'south'), 
           ('give', 'receive'), ('summer', 'winter'), ('spring', 'fall'), ('snakes', 'lizards'), ('spiders', 'scorpions'), ('yes', 'no'), ('pearls', 'crystals'), ('rain', 'snow'), 
           ('love', 'money'), ('icicle', 'snowflake'), ('well', 'garden'), ('nuts', 'berries'), ('slither', 'hiss'), ('first', 'last'), ('fight', 'flight'), ('Europe', 'Asia'), 
           ('gold', 'silver'), ('speed', 'strength'), ('bullet', 'blade'), ('soup', 'salad'), ('rice', 'noodles'), ('ranch', 'bleu cheese'), ('sword', 'knife'), ('rifle', 'pistol'), 
           ('diamonds', 'all other gems'), ('fairy', 'mermaid'), ('extra eyes', 'extra arms'), ('sneakers', 'boots'), ('enlarge', 'shrink'), ('front', 'back'), ('loud', 'silent'), 
           ('small', 'large'), ('lightning', 'thunder'), ('blind', 'deaf'), ('above', 'below'), ('basement', 'attic'), ('ladder', 'stairs'), ('road', 'bridge'), ('pizza', 'sandwiches'), 
           ('pb&j', 'grilled cheese'), ('curvy', 'straight'), ('funny', 'smart'), ('extra hairy', 'bald'), ('tired', 'grumpy'), ('soft', 'hard'), ('table', 'chair'), ('pencil', 'pen'), 
           ('cursive', 'print'), ('crazy', 'alone'), ('full', 'empty'), ('100', '42'), ('shallow', 'deep'), ('catch', 'release'), ('dragons', 'dinosaurs'), ('lions', 'tigers'), 
           ('stripes', 'spots'), ('horizontal', 'vertical'), ('unique', 'identical'), ('swim', 'climb'), ('sick', 'hungry'), ('here', 'there'), ('top', 'bottom'), ('Jupiter', 'Saturn'), 
           ('aliens', 'zombies'), ('knowledge', 'power'), ('dimples', 'freckles'), ('train', 'boat'), ('rushed', 'halted'), ('immortal', 'omniscient'), ('land', 'sea'), ('water', 'sky'), 
           ('mind reading', 'invisibility'), ('Grim Reaper', 'ghosts'), ('longer life with smaller brain', 'shorter life with larger brain'), ('butter', 'salt & pepper'), ('chicken', 'beef'), 
           ('breakfast', 'dinner'), ('pancakes', 'waffles'), ('baked', 'grilled'), ('simple', 'complex'), ('pudding', 'jello'), ('coffee', 'chocolate'), ('vanilla', 'caramel'), 
           ('sticky', 'chewy'), ('creamy', 'crunchy'), ('cupcakes', 'donuts'), ('centaur', 'minotaur'), ('Pegasus', 'unicorn'), ('puzzle', 'maze'), ('choose', 'chosen'), ('this', 'that'), 
           ('board games', 'card games'), ('all', 'none'), ('anger', 'sadness'), ('volcano', 'underwater cave'), ('Raptor', 'T-Rex'), ('tornado', 'hurricane'), ('flood', 'fire'), 
           ('earthquake', 'tidal wave'), ('elevator', 'escalator'), ('hello', 'goodbye'), ('motorcycle', 'jet ski'), ('city', 'country'), ('camping', 'rafting'), ('rainbow', 'waterfall'), 
           ('fame', 'fortune'), ('near', 'far'), ('stay', 'go'), ('Christmas', 'Thanksgiving'), ('surfing', 'snowboarding'), ('fork', 'spoon'), ('rare', 'common'), ('twist', 'turn'), 
           ('Halloween', 'birthday'), ('twist', 'turn'), ('phoenix', 'griffin'), ('fridge', 'stove'), ('add', 'subtract'), ('light', 'dark'), ('burp', 'fart'), ('garlic', 'onion'), 
           ('art', 'music'), ('piano', 'violin'), ('indoors', 'outdoors'), ('day', 'night'), ('butterflies', 'dragonflies'), ('dogs', 'cats'), ('lemon', 'lime'), ('shark', 'whale'), 
           ('kick', 'punch'), ('sit', 'stand'), ('thick', 'thin'), ('stingray', 'jellyfish'), ('orca', 'dolphin'), ('Alaska', 'Hawaii'), ('heart', 'mind'), ('open', 'closed'), 
           ('elephant', 'rhinoceros'), ('genie', 'fortune teller'), ('bath', 'shower'), ('water park', 'amusement park'), ('Spiderman', 'Batman'), ('dishes', 'laundry'), ('on', 'off'), 
           ('movies', 'TV shows'), ('sandwiches', 'burgers'), ('pillow', 'blanket'), ('guitar', 'drums'), ('hoodie', 'jacket')]


fates = [('It seems you have trouble making up your mind. You need to be more decisive and confident in your choices.'), 
         ('You have a balanced way of looking at things. This will take you far.'), 
         ("You haven't made very good choices. You should be more thoughtful of the impact and consequences of your actions."), 
         ('Your responses are suspicious. You need to be more honest with yourself and others.'), 
         ('Some of your choices have been questionable. You have a lot more to learn, but if you keep an open mind, you have the potential to live a successful life.'), 
         ('Your future is uncertain. Take great care and seek wise counsel when making important decisions.'), 
         ('You are a mystery. Your fate cannot be determined at this time. Please come back later and try again.'), 
         ('You have chosen well. Keep your head up and trust your instincts. You have the potential to achieve great things.'), 
         ("You've made good choices. Just be careful not to get too comfortable. There's always room for improvement."), 
         ("A bit hard to tell, but you seem to be on the right track. Just be careful and don't be afraid to ask for advice."),
         ('\n\nNot the best decision. You must go back and make up to an additional 3 choices.'), ("\n\nI'm sorry. You must go back at the beginning. Try again."), 
         ('\nYou have died. Game over.'), ('\nCongratulations! You have found the meaning of life. You win!')]


win = ['42', 'light', 'pizza', 'dogs', 'above']

lose = ['fame', 'money', 'zombies', 'power', 'immortal']

reset = ['longer life with smaller brain', 'goodbye', 'receive', 'grumpy', 'empty']

setback = ['simple', 'none', 'no', 'shallow', 'identical']

all_restarts = []

for i in win:
    all_restarts.append(i)
for i in lose:
    all_restarts.append(i)
for i in reset:
    all_restarts.append(i)


#Introduction
print("\nWelcome to Doors of Fate!")
name = input("\nWhat is your name? ")
print("\nHello, " + name + """! Let's play a game. You are in a room with only two doors. Each door represents a choice. You must decide which is the right one.
Whichever door you choose leads to another room with two more doors. This will continue until the culmination of your decisions is enough to determine your fate. 
                                                                    Let's begin!""")


#Function to play the game
def main():
    print("\n\nSTART")
    used_indices = []
    used_choices = []
    count1 = 0
    count2 = 0
    while used_choices == [] or len(used_choices) < 10:
        ran = random.randint(0, (len(choices) - 1))
        while ran not in used_indices:
            res = input('\n\nDOOR 1: ' + choices[ran][0] + '\n\n        OR        ' + '\n\nDOOR 2: ' + choices[ran][1] + '\n\nPlease type 1 or 2: ')
            while res != '1' and res != '2':
                print('Invalid input. Please try again.')
                res = input('\n\nDOOR 1: ' + choices[ran][0] + '\n\n        OR        ' + '\n\nDOOR 2: ' + choices[ran][1] + '\n\nPlease type 1 or 2: ')
            if res == '1':
                if choices[ran][0] in all_restarts:
                    if choices[ran][0] in win:
                        print(fates[-1])
                        return restart()
                    elif choices[ran][0] in lose:
                        print(fates[-2])
                        return restart()
                    elif choices[ran][0] in reset:
                        print(fates[-3])
                        return main()
                elif choices[ran][0] in setback:
                    used_indices.append(ran)
                    used_choices.append(choices[ran][0])
                    used_choices = used_choices[:-3]
                    print(fates[-4])
                    print('\n\nRESET STARTS HERE')
                else:
                    used_indices.append(ran)
                    used_choices.append(choices[ran][0])
                    count1 += 1
            elif res == '2':
                if choices[ran][1] in all_restarts:
                    if choices[ran][1] in win:
                        print(fates[-1])
                        return restart()
                    elif choices[ran][1] in lose:
                        print(fates[-2])
                        return restart()
                    elif choices[ran][1] in reset:
                        print(fates[-3])
                        return main()
                elif choices[ran][1] in setback:
                    used_indices.append(ran)
                    used_choices.append(choices[ran][1])
                    used_choices = used_choices[:-3]
                    print(fates[-4])
                    print('\n\nRESET STARTS HERE')
                else:
                    used_indices.append(ran)
                    used_choices.append(choices[ran][1])
                    count2 += 1
    else:
        print('\nYou have made your final choice. ' + name + ', here is your fate...\n')
        if count1 == count2:
            ran2 = random.randint(0, 1)
            print(fates[ran2])
        elif count1 or count2 == 0:
            ran3 = random.randint(2, 3)
            print(fates[ran3])
        elif count1 or count2 == 1:
            ran4 = random.randint(4, 5)
            print(fates[ran4])
        else:
            ran5 = random.randint(0, 9)
            print(fates[ran5])
        return restart()

#Function to restart the game
def restart():
    answer = input("\nIf you would like to play again, type 'y'. If not, type 'n'... ")
    while answer.lower() != 'y' and answer.lower() != 'n':
        print('Invalid input. Please try again.')
        answer = input("\nIf you would like to play again, type 'y'. If not, type 'n'... ")
    if answer.lower() == 'n':
        print('\nThank you for playing. Goodbye.\n')
    elif answer.lower() == 'y':
        return main()
        
    
        
#Start the game
main()


