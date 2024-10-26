print("\nWelcome to Gold Quest Island! There will be gold scattered all around the island, you only need to collect 5!\n")

path1 = "You enter the jungle. You hit something on the ground and see it's your first piece of gold. Just then a monkey comes and takes it from your hand and dashes the other way!\n"
path2 = "You continue walking the shore, after a few hours you find no gold.\n"
path3 = "You chase the monkey for a couple of minutes but you lose sight of it. It's ok, there are more pieces of gold around the island.\n"
path4 = "You decide not to chase the monkey because there are other pieces of gold on the island.\n"
path5 = ("You enter the cave only to realize that it belonged to an evil witch!\n"
          "The witch casts a spell on you and you fall deeply asleep.\n"
          "You wake up in the middle of a swamp, and realize there is a pack of crocodiles all around the swamp.\n")
path6 = "You sleep peacefully on the beach and wake up to a bird pecking your face! You ~shoo~ it away and decide to venture into the jungle.\n"

# Variable to track player's lives
player_lives = 3
gold_collected = 0  # Initialize gold collected

# Function for asking location questions
def location(side):
    return f"Would you like to {side}?\n"

# Main game loop
while player_lives > 0 and gold_collected < 5:
    # Ask initial path decision
    print(location("go into the jungle or keep walking the shore? (Type 'jungle' or 'shore')"))
    player_input = input().lower()

    if player_input == "shore":
        print(path2)
    else:
        print(path1)
        # After entering the jungle, ask if the player wants to chase the monkey
        print(location("chase the monkey? (Type 'yes' or 'no')"))
        player_input = input().lower()

        if player_input == "yes":
            print(path3)
            gold_collected += 1  # Increase gold count for chasing the monkey
        else:
            print(path4)

    # Ask for sleeping location
    print(location("sleep in the cave or on the beach? (Type 'cave' or 'beach')"))
    player_input = input().lower()

    if player_input == "cave":
        print(path5)
        player_lives -= 1  # Losing a life after sleeping in the cave
    else:
        print(path6)

    # Encounter jaguar and reduce lives
    print("A jaguar jumps outta nowhere. You have no choice but to face it head on.")
    player_lives -= 1  # Deduct one life for the challenge
    print(f"You have {player_lives} lives remaining.")

# Game over conditions
if gold_collected >= 5:
    print("Congratulations! You've collected all the gold and completed the quest!")
else:
    print("You've run out of lives! Game over.")
