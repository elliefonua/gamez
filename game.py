

# (variable) what each path causes to happen to the user - ellie, sofia, lindsey

print("\nWelcome to Monkey Island! There will be little to no golden bananas around the island, you only need to collect 5!\n")

path1 = "\nYou enter the jungle, you explore for a few hours until sundown, in the distance you see a shiny object, could it be..! you run to it and grab it, You realize it's a fake!:( its  getting late /n you should find a place to sleep a place to sleep.\n"

path2 = "\nYou continue walking the shore, after a few hours you see something shiny in the sand! you run up and see a golden banana!! you lift it up only to find that its a fake:(\nThe sun is setting and you need a place to sleep.\n"

path3 = "\nYou enter the cave and set up for sleep. You wake up the next morning and head back into the jungle.\n"

path4 = "\nYou get comfortable on the beach and rest well. The next morning you set off into the jungle to find your golden bananas!\n"

path5 = "\nYou decide to explore a cave and you discover a grand pile of what seems to be thousands of pieces of golden bananas!\n"

path6 = "\nYou decide to take a rest, something about the cave is intriguing. You go inside and discover thousands of pieces of golden bananas!\n"

path7 = "\nskibidi sigmaa! your out! leave bumm! [dw pookie wookie, you can play again!]\n"

path8 = "\nYou have chosen to accept this duel!\n"

path9 = "\nYou toss the banana out the cave not knowing that the monkey was actually starving.\nthe monkey king dashes out the cave following the banana without giving it a second thought.\nyou are surprised, but happy\n you run over and take his golden banana\n"

path10 = "\nYou throw the banana at the monkey king and it pokes him right in the eye\nsuddenly the monkey starts to cry as you run over and steal his golden bananas\n"

path11 = "\nYou walk over to the bush and suddenly see something shiny, you look closer to see that its a golden banana!\nYou rub it and realize that the gold is coming off (ITS A FAKE)"


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
    
golden_banana = 0

while golden_banana <= 0:
    print("would you like to sleep on the 'beach', in the 'cave', or in the 'bushes'?\n")
    break
    if golden_banana > 0:
        print("you have {golden_banana} ")
        break
    if golden_banana < 0:
        print("would you like to sleep on the 'beach', in the 'cave', or in the 'bushes'?\n")
    break
def locations(side):
    return (input(f"Would you like to {side}"))

sleeping = (locations(" sleep on the 'beach' in the 'cave' or in the 'bushes'?\n"))

if sleeping == "cave":
    print(path3)
if sleeping == "bushes":
    golden_banana += 1
    print(path11)
else:
    print(path4)




print("You climb up a mountain and find a cave.")

def rest(sid):
    return (input(f"do you want to 'explore' it or {sid}"))
    pass
sleep = (input("take a 'rest'?: \n"))

while sleep == "explore":
    print(path5)
if sleep == "no":
    print(path6)


def monkey(boss):
    return (input(f"Monkey King:\n '{boss}"))

print(monkey("What brings you here filthy mortal'\n"))
print(monkey("I've spent my whole life collecting this mountain of golden bananas!'\n"))
print(monkey("I will not lose it to some peasant who doesn't even have a tail!'\n\n"))

duel = (input("This calls for a duel! Will you 'accept' or 'decline'?\n"))

        
if duel == "decline":
    print(path7)
else:
    print(path8)
    print("you:\nWell, no WONDER there wasn't that much gold around, this monkey took it ALL!\nNot FAIR! You must take back what is yours!\n")
    





# (condition) conditoning wether the user takes path one or two and what happens when user chooses different answers - sofia

print("you:\nWell, no WONDER there wasn't that much gold around, this monkey took it ALL!\nNot FAIR! You must take back what is yours!\n")



# (loop) how many lives the user has and whether they would like to restart or continue and controls how long the condition goes for until game is done - lindsey

        

banana = (input("\n\nSuddenly, you see a banana in your pocket that you picked up from the climb to eat for dinner.\n\nWill you 'throw' it at the monkey or 'toss' it outside the cave?\n"))



if banana == 'toss':
    print(path9)
else:
    print(path10)
    print("Congrats my skibidi sigma! you have collected all the gold you needed!\n")
    print("Thanks for playing! Hope to see you again soon![MERP]\n")







