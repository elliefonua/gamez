
# (variable) what each path causes to happen to the user - ellie, sofia, lindsey

print("\nWelcome to Gold Quest Island! There will be gold scattered all around the island, you only need to collect 5!\n")
path1 = ("\nYou enter the jungle, you explore for a few hours until sundown, you found no gold today.\nYou realize it's getting late and that you need a place to sleep.\n")
path2 = ("\nYou continue walking the shore, after a few hours you find no gold. the sun is setting and you need a place to sleep.\n")
path3 = ("\nYou enter the cave and set up for sleep. You wake up the next morning and head back into the jungle\n")
path4 = ("\nYou get comfortable on the beach and rest well. The next morning you set off into the jungle to find your gold!\n")
path5 = ("\nYou decide to explore the cave and you discover a grand pile of what seems to be thousands of peices of gold!\n")
path6 = ("\nYou decide to take a rest, something about the cave is intriguing. you go inside and discover thousands of peices of gold!\n")
# (function) ask the quests questions and where they want to go for the different locations on the game map - ellie

def hello(name):
    return (input(f"what is your {name}"))

    print(hello("name?\n"))


player_input = input()

# (condition) conditoning wether the user takes path one or two and what happens when user chooses different answers - sofia

def locations(side):
    return f"Would you like to {side}"

print(locations("go into the 'jungle' or keep walking the 'shore'?\n"))

player_input = input()

if player_input == "shore":
    print(path2)  
else:
    print(path1)
          
def locations(side):
    return f"Would you like to {side}"

print(locations(" sleep on the 'beach' or in the 'cave'?\n"))
player_input = input()

if player_input == "cave":
     print(path3)
else:
     print(path4)

print("You 'climb' up a mountain and find a cave, do you want to explore it or take a 'rest'?\n")

def rest(sid):
    return f"explore it or take a rest?{sid}"
player_input = input()
if player_input == "explore":
    print(path5)
else:
    print(path6)

    

def monkey(boss):
    return f"Monkey King:\n '{boss}'"

print(input("What brings you here filthy mortal?(say 'gold')\n"))


if player_input == "gold":
    print("I've spent my whole life collecting this mountain of gold!")
print("I will not lose it to some peasant who doesn't even have a tail!")


print("\nWell, no WONDER there wasn't that much gold around, this monkey took it ALL!\nNot FAIR! You must take back what is yours!\n")



# (loop) how many lives the user has and wether they would like to restart or continue and controls how long the condition goes for until game is done - lindsey



player_hp = 100



if player_hp > 0:


    print("the monkey lunges toward you in defense of it's stolen gold.\n")
    player_hp -= 60
    print("You lost 40 hp!")




if player_hp > 0:
    print(f"You have {player_hp} hp remaining.")
    action = input("Do you want to 'continue' the battle or 'quit'? ")



if action == "quit":
     print("\nThanks for playing! Goodbye![TEEHEE]\n")

else:
    print("\n\nSuddenly, you see a banana in your pocket that you picked up from the climb to eat for dinner.\n\nWill you 'throw' it at the monkey or 'toss' it ouside the cave?")

    player_input

    print("\nYou've finished 'Gold Quest Island!' Hope to see you again!\n")







          
    
sibling = ["jungle", "shore", "beach", "cave", "mountain"]

for ling in sibling:
    print(input(f"would you like to go to {ling}?\n"))
    
player_input


if player_input == "no":
    print("dummy")

if player_input == "yes":
    print("pen pineapple apple pen")







