print("\nWelcome to Gold Quest Island! There will be gold scattered all around the island, you only need to collect 5!\n")
path1 = ("You enter the jungle. You hit something on the ground and see it's your first piece of gold. Just then a monkey comes and takes it from your hand and dashes the other way!\n")
path2 = ("You continue walking the shore, after a few hours you find no gold.\n")
path3 = ("You chase the monkey for a couple of minutes and you lose sight of it. It's okay, there are more pieces of gold around the island.\n")
path4 = ("You decide not to chase the monkey because there are other pieces of gold on the island.\n")
path5 = ("You enter the cave only to realize that it belonged to an evil witch!\nThe witch casts a spell on you and you fall deeply asleep.\nYou wake up in the middle of a swamp, and realize there is a pack of crocodiles all around the swamp waters.\n")
path6 = ("You sleep peacefully on the beach and wake up to a bird pecking your face! You ~shoo~ it away and decide to venture into the jungle.\n")

def location(side):
    return f"Would you like to {side}"

print(location("go into the jungle or keep walking the shore, jungle or shore?\n"))

player_input = input()

if player_input == "shore":
    print(path2)  
else:
    print(path1)

def check_input():
    global player_input
    print("Night approaches, would you like to sleep on the beach or in the cave?")
    player_input = input()

check_input()

if player_input == "cave":
    print(path5)
else:
    print(path6)

print(location("would you like to chase the monkey?('yes' or 'no')\n"))
player_input = input() 

if player_input == "yes":
    print(path3)
else:
    print(path4)

player_lives = 3

while player_lives > 0:
    print("A jaguar jumps outta nowhere. You have no choice but to face it head on.")
    player_lives -= 1
    print("You lost a life!")

    if player_lives > 0:
        print(f"You have {player_lives} lives remaining.")
        action = input("Do you want to 'continue' the adventure or 'quit'? ")

        if action == "quit":
            print("Thanks for playing! Goodbye!")
            break
        elif action != "continue":
            print("Invalid choice. Defaulting to continue.")
    else:
        print("Game Over! You have run out of lives.")