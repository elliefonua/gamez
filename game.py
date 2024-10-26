
# (variable) what each path causes to happen to the user - ellie, sofia, lindsey

print("\nWelcome to Gold Quest Island! There will be gold scattered all around the island, you only need to collect 5!\n")
path1 = ("You enter the jungle, you explore for a few hours until sundown, you found no gold today\n")
path2 = ("You continue walking the shore, after a few hours you find no gold. the sun is setting and you need a place to sleep.\n")
path3 = ("You enter the cave and set up for sleep. You wake up the next morning and head back into the jungle\n")
path4 = ("You get comfortable on the beach and rest well. The next morning you set off into the jungle to find your gold!")
# (function) ask the quests questions and where they want to go for the different locations on the game map - ellie


# (condition) conditoning wether the user takes path one or two and what happens when user chooses different answers - sofia

def locations(side):
    return f"Would you like to {side}"

print(locations("go into the 'jungle' or keep walking the 'shore'?\n"))

player_input = input()

if player_input == "shore":
    print(path2)  
else:
    print(path1)


def location(side):
    return f"Would you like to {side}"

print(location(" sleep on the beach or in the cave?\n"))
player_input = input() 

if player_input == "cave":
     print(path3)
else:
     print(path4)
print("You climb up a mountain and find a cave, you decide to explore it and find a grand pile of gold!\n")
def monkey(boss):
    return f"'Monkey King:\n {boss}"

print(monkey("What brings you here filthy mortal?\nI've spent my whole life collecting this mountain of gold!\nI will not lose it to some peasant who doesn't even have a tail!'\n"))
print("\nWell, no WONDER there wasn't that much gold around, this monkey took it ALL!\nNot FAIR! You must take back what is yours!\n")



# (loop) how many lives the user has and wether they would like to restart or continue and controls how long the condition goes for until game is done - lindsey



player_hp = 100



if player_hp > 0:


    print("the monkey attacks you in defense of it's stolen gold.\n")
    player_hp -= 60
    print("You lost 40 hp!")




if player_hp > 0:
    print(f"You have {player_hp} hp remaining.")
    action = input("Do you want to 'continue' the battle or 'quit'? ")



if action == "quit":
     print("Thanks for playing! Goodbye![TEEHEE]")

else:
    print("Suddenly, you see a banana in your pocket that you picked up from the climb to eat for dinner.\nThe monkey king pauses as you wave high in the air.\n You throw it out the cave and down the mountain,\n without a second thought, the monkey runs and jumps off the mountain falling to it's death.\nYou secure your 5 gold, and much more!\n")

print("\nJob well done, mortal! You've finished 'Gold Quest Island!' Hope to see you again!\n")