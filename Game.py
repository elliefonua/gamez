

# (variable) what each path causes to happen to the user - ellie, sofia, lindsey


print("\nWelcome to Monkey Island! There will be little to no golden bananas around the island, you only need to collect 5!\n")


path1 = "\nYou enter the jungle, explore for a few hours until sundown, and see a shiny object in the distance. You run to it and grab it, only to realize it's a fake! :( It's getting late, you should find a place to sleep.\n"

path2 = "\nYou continue walking along the shore, and after a few hours, you see something shiny in the sand! You run up and find a golden banana!! You lift it up, only to discover that it's a fake :( The sun is setting, and you need a place to sleep.\n"

path3 = "\nYou enter the cave and set up for sleep. The next morning, you wake up and head back into the jungle.\n"

path4 = "\nYou get comfortable on the beach and rest well. The next morning, you set off into the jungle to find your golden bananas!\n"

path5 = "\nYou decide to explore a cave and discover a grand pile of what seems to be thousands of pieces of golden bananas!\n"

path6 = "\nYou decide to take a rest; something about the cave is intriguing. You go inside and discover thousands of pieces of golden bananas!\n"

path7 = "\nskibidi sigmaa! you're out! Leave, bum! [Don't worry, you can play again!]\n"

path8 = "\nYou have chosen to accept this duel!\n"

path9 = "\nYou toss the banana out of the cave, not knowing that the monkey was actually starving. The monkey king dashes out, following the banana without a second thought. You are surprised but happy as you run over and take his golden banana!\n"

path10 = "\nYou throw the banana at the monkey king, and it pokes him right in the eye! Suddenly, the monkey starts to cry as you run over and steal his golden bananas!\n"

path11 = "\nYou walk over to the bush and suddenly see something shiny. You look closer and realize it's a golden banana! You rub it and discover that the gold is coming off (ITS A FAKE).\n"


# (function) ask the quests questions and where they want to go for the different locations on the game map - ellie


def hello(name):
    return input(f"What is your {name}")


print(hello("name?\n"))


def walky(walk):
    return input(f"Would you like to {walk}")


walker = walky("go into the 'jungle' or keep walking the 'shore'?\n")


if walker == "shore":
    print(path2)
else:
    print(path1)


golden_banana = 0

# (loop) how many lives the user has and whether they would like to restart or continue and controls how long the condition goes for until game is done - lindsey
while golden_banana < 5:
    sleeping = input("Would you like to sleep on the 'beach', in the 'cave', or in the 'bushes'?\n")


    if sleeping == "cave":
        print(path3)
    elif sleeping == "bushes":
        golden_banana += 1
        print(path11)
    else:
        print(path4)
        
    print("you climb a mountain and at the top is cave")

    sleep = input("Do you want to 'explore' it or 'take a rest'?\n")


    if sleep == "explore":
        print(path5)
    else:
        print(path6)

    defeat_monkey = input("Monkey King: 'What brings you here, filthy mortal?' Would you like to accept the duel? (yes/no)\n")

# (condition) conditoning wether the user takes path one or two and what happens when user chooses different answers - sofia

    if defeat_monkey.lower() == "no":
        print(path7)
        break
    else:
        
        print(path8)
        print("You: 'Well, no WONDER there weren't any golden bananas around, this monkey took it ALL! Not FAIR! You must take back what is yours!'\n")


    banana = input("\n\nSuddenly, you see the fake golden banana in your pocket that you picked up earlier.\nWill you 'throw' it at the monkey or 'toss' it outside the cave?\n")


    if banana == "toss":
        print(path9)
        print("Congrats, my skibidi sigma! You have collected all the gold you needed!\n")
        print("Thanks for playing! Hope to see you again soon![MERP]\n")
        break
    else:
        print(path10)
        print("Congrats, my skibidi sigma! You have collected all the gold you needed!\n")
        print("Thanks for playing! Hope to see you again soon![MERP]\n")
        break
