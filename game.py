
# (variable) what each path causes to happen to the user - ellie, sofia, lindsey

print("\nWelcome to Gold Quest Island! There will be gold scattered all around the island, you only need to collect 5!\n")
path1 = ("You enter the jungle. You hit somthing on the ground and see its your first piece of gold. Just then a monkey comes and takes it from your hand and dashes the other way!\n")
path2 = ("You continue walking the shore, after a few hours you find no gold.\n")
path3 = ("You chase the monkey for a couple minutes and you lose sight of it. Its ok there are more peices of gold around the island\n")
path4 = ("You decide not to chase the monkey because there are other peices of gold on the island.\n")

# (function) ask the quests questions and where they want to go for the different locations on the game map - ellie
# (condition) conditoning wether the user takes path one or two and what happens when user chooses different answers - sofia

def location(side):
    return f"Would you like to {side}"



print(location("go into the jungle or keep walking the shore, jungle or shore?\n"))
player_input = input()

if player_input == "shore":
        print(path2) 
    else:
 if player_input == "shore":
    question = input("night aproaches, where will you sleep? the cave or on the beach?")        print(path1)

def location1(side):
    return f"Would you like to {side}"

    print(location1("would you like to chase the monkey?('yes' or 'no')\n"))
    player_input = input() 

    if player_input == "yes":
        print(path3)
    else:
        print(path4)




# (loop) how many lives the user has and wether they would like to restart or continue and controls how long the condition goes for until game is done - lindsey

# Variable to track player's lives
player_lives = 3
player_livez = 2

# Main game loop
while player_lives > 0:
    # Simulate a situation that causes losing a life
    print("A jaguar jumps outta nowhere. You have no choice but to face it head on.")
    player_lives -= 1  # Deduct one life for the challenge
    print("You lost a life!")






    if player_lives > 0:
        # Show lives and ask for action only if the player still has lives left
        print(f"You have {player_livez} lives remaining.")
        action = input("Do you want to 'continue' the adventure or 'quit'? ").lower()
        
        if action == "quit":
            print("Thanks for playing! Goodbye!")
            break
        elif action != "continue":
            print("Invalid choice. Defaulting to continue.")
    else:
        print("Game Over! You have run out of lives.")

