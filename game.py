
# (variable) what each path causes to happen to the user - ellie, sofia, lindsey

print("\nWelcome to Gold Quest Island! There will be gold scattered all around the island, you only need to collect 5!\n")

path1 = "\nYou enter the jungle, you explore for a few hours until sundown, you found no gold today. You realize it's getting late\nyou need a place to sleep.\n"
path2 = "\nYou continue walking the shore, after a few hours you find no gold. The sun is setting and you need a place to sleep.\n"
path3 = "\nYou enter the cave and set up for sleep. You wake up the next morning and head back into the jungle.\n"
path4 = "\nYou get comfortable on the beach and rest well. The next morning you set off into the jungle to find your gold!\n"
path5 = "\nYou decide to explore a cave and you discover a grand pile of what seems to be thousands of pieces of gold!\n"
path6 = "\nYou decide to take a rest, something about the cave is intriguing. You go inside and discover thousands of pieces of gold!\n"
path7 = "\nskibidi sigmaa! your out! leave bumm! [dw pookie wookie, you can play again!]\n"
path8 = "\nYou have chosen to accept this duel!\n"
path9 = "\nYou toss the banana out the cave unknowingly that the monkey was actually starving.\nthe monkey king dashes out the cave following the banana without giving it a second thought.\nyou are surprised, but happy\n you run over and take his gold\n"
path10 = "\nYou throw the banana at the monkey king and it pokes him right in the eye\nsuddenly the monkey starts to cry as you run over and steal his gold\n"

# (function) ask the quests questions and where they want to go for the different locations on the game map - ellie


def hello(name):
    return (input(f"What is your {name}"))

print(hello("name?\n"))

def walky(walk):
    return (input(f"Would you like to {walk}"))

walker = (walky("go into the 'jungle' or keep walking the 'shore'?\n"))

if walker == "shore":
    print(path2)
else:
    print(path1)

def locations(side):
    return (input(f"Would you like to {side}"))

sleeping = (locations(" sleep on the 'beach' or in the 'cave'?\n"))

if sleeping == "cave":
    print(path3)
else:
    print(path4)

print("You climb up a mountain and find a cave.")

def rest(sid):
    return (input(f"do you want to 'explore' it or {sid}"))

sleep = (rest("take a 'rest'?\n"))


if sleep == "explore":
    print(path5)
else:
    print(path6)


def monkey(boss):
    return (input(f"Monkey King:\n '{boss}"))

print(monkey("What brings you here filthy mortal'\n"))
print(monkey("I've spent my whole life collecting this mountain of gold!'\n"))
print(monkey("I will not lose it to some peasant who doesn't even have a tail!'\n\n"))

duel = (input("This calls for a duel! Will you 'accept' or 'decline'?\n"))

        
if duel == "accept":
    print(path8)
else:
    print(path7)





# (condition) conditoning wether the user takes path one or two and what happens when user chooses different answers - sofia

print("you:\nWell, no WONDER there wasn't that much gold around, this monkey took it ALL!\nNot FAIR! You must take back what is yours!\n")


# (loop) how many lives the user has and whether they would like to restart or continue and controls how long the condition goes for until game is done - lindsey

        

banana = (input("\n\nSuddenly, you see a banana in your pocket that you picked up from the climb to eat for dinner.\n\nWill you 'throw' it at the monkey or 'toss' it outside the cave?\n"))



if banana == 'toss':
    print(path9)
else:
    print(path10)
    print("congrats my skibidi sigma! you have collected all the gold you needed!\n")
    print("Thanks for playing! Hope to see you again soon![MERP]\n")

while banana == player_golden banana 