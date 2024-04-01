#Take Your Pick is a simple game where the user is asked to choose between two options. The user is given a choice between two options and must choose one. 
#The game will keep track of the user's choices and display the results at the end. The game will be implemented using Python and will be run in the terminal.

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
           ('board games', 'card games'), ('all', 'none'), ('anger', 'sadness'), ('volcano', 'underwater cave'), ('Raptor', 'Rex'), ('tornado', 'hurricane'), ('flood', 'fire'), 
           ('earthquake', 'tidal wave'), ('elevator', 'escalator'), ('hello', 'goodbye'), ('motorcycle', 'jet ski'), ('city', 'country'), ('camping', 'rafting'), ('rainbow', 'waterfall'), 
           ('fame', 'fortune'), ('near', 'far'), ('stay', 'go'), ('Christmas', 'Thanksgiving'), ('surfing', 'snowboarding'), ('fork', 'spoon'), ('rare', 'common'), ('twist', 'turn'), 
           ('Halloween', 'birthday'), ('twist', 'turn'), ('phoenix', 'griffin'), ('fridge', 'stove'), ('add', 'subtract'), ('light', 'dark'), ('burp', 'fart'), ('garlic', 'onion'), 
           ('art', 'music'), ('piano', 'violin'), ('indoors', 'outdoors'), ('day', 'night'), ('butterflies', 'dragonflies'), ('dogs', 'cats'), ('lemon', 'lime'), ('shark', 'whale'), 
           ('kick', 'punch'), ('sit', 'stand'), ('thick', 'thin'), ('stingray', 'jellyfish'), ('orca', 'dolphin'), ('Alaska', 'Hawaii'), ('heart', 'mind'), ('open', 'closed'), 
           ('elephant', 'rhinoceros'), ('genie', 'fortune teller'), ('bath', 'shower'), ('water park', 'amusement park'), ('Spiderman', 'Batman'), ('dishes', 'laundry'), ('on', 'off'), 
           ('movies', 'TV shows'), ('sandwiches', 'burgers'), ('pillow', 'blanket'), ('guitar', 'drums'), ('hoodie', 'jacket')]

fates = [('You have chosen well.'), ('Some of your choices have been questionable.'), ("You didn't make very good choices."), 
         (''), (''), (''), (''), (''), (''), ('Not the best decision. You must go back and make an additional 3 choices.'), ("I'm sorry. You must go back at the beginning. Try again."), 
         ('You have died. Game over.'), ('Congratulations! You have found the meaning of life. You win!')]

win = ['42', 'light', 'pizza', 'dogs', 'above']

lose = ['fame', 'money', 'zombies', 'power', 'immortal']

reset = ['longer life with smaller brain', 'goodbye', 'receive', 'grumpy', 'empty']

setback = ['simple', 'none', 'no', 'shallow', 'identical']

all_triggers = []

for i in win:
    all_triggers.append(i)
for i in lose:
    all_triggers.append(i)
for i in reset:
    all_triggers.append(i)
for i in setback:
    all_triggers.append(i)

used_indices = []

used_choices = []

#Introduction
print("Welcome to Take Your Pick!")
name = input("What is your name? ")
print("Hello, " + name + "! Let's play a game. You will be given a series of choices and you must choose one each time. Let's begin!")


#Function to play the game
def first():
    if used_choices == [] or len(used_choices) < 10:
        ran = random.randint(0, (len(choices) - 1))
        while ran not in used_indices:
            r1 = input('\nChoice 1: ' + choices[ran][0] + '\n\n           OR        ' + '\n\nChoice 2: ' + choices[ran][1] + '\n\nPlease type 1 or 2: ')
            while r1 != '1' and r1 != '2':
                print('Invalid input. Please try again.')
                r1 = input('\nChoice 1: ' + choices[ran][0] + '\n\n           OR        ' + '\n\nChoice 2: ' + choices[ran][1] + '\n\nPlease type 1 or 2: ')
            if r1 == '1':
                used_indices.append(ran)
                used_choices.append(choices[ran][0])
                return first()
            elif r1 == '2':
                used_indices.append(ran)
                used_choices.append(choices[ran][1])
                return first()
    elif len(used_choices) == 10:
        print('You have made your final choice. Here is your fate...')
        used_indices.clear()
        used_choices.clear()
        return
          

#Function to restart the game
def restart():
    answer = input("If you would like to play again, type 'y'. If not, type 'n'... ")
    while True:
        if answer.lower() == 'y':
            return first()
        elif answer.lower() == 'n':
            print('Thank you for playing. Goodbye.')
            break
        else:
            print('Invalid input. Please try again.')
            answer = input("If you would like to play again, type 'y'. If not, type 'n'... ")



#Start the game
first()



    