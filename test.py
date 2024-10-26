# This code manages player lives in a game.

# Variable to track player's lives
player_lives = 3

def display_lives():
    """Function to display the player's current lives."""
    print(f"You have {player_lives} lives remaining.")

# Main game loop
while player_lives > 0:
    action = input("Do you want to 'continue' the adventure or 'quit'? ").lower()

    if action == "continue":
        print("You continue your adventure!")
        # Simulate a situation that could cause losing a life
        player_lives -= 1  # Deduct one life for continuing
        print("You faced a challenge and lost a life!")
        display_lives()  # Show lives only after losing a life
    elif action == "quit":
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 'continue' or 'quit'.")

if player_lives == 0:
    print("Game Over! You have run out of lives.")
