
# (variable) what each path causes to happen to the user - ellie, sofia, lindsey

print("Welcome to Gold Quest Island! There will be gold scattered all around the island, you only need to collect 5\n")
path1 = ("You enter the jungle. You hit somthing on the ground and see its your first piece of gold. Just then a monkey comes and takes it from your hands and runs!\n")
path2 = ("You continue walking the shore, after a few hours you find no gold.\n")
path3 = ("You chase the monkey for a couple minutes and you lose sight of it. Its ok there are more peices of gold around the island\n")
path4 = ("You decide not to chase the monkey because there are other peices of gold on the islnad.\n")

# (function) ask the quests questions and where they want to go for the different locations on the game map- ellie
# (condition) conditoning wether the user takes path one or two and what happens when user chooses different answers - sofia

def location(side):
    return f"Would you like to {side}"

print(location("go into the jungle or keep walking the shore, jungle or shore?\n"))
player_input = input()


if player_input == "shore":
    print(path2)
else:
    print(path4)
# (loop) how many lives the user has and wether they would like to restart or continue and controls how long the condition goes for until game is done - lindsey
monkey(chase):
    return (input(f"do you want {chase}, yes or no?\n"))
    print(monkey("to get your gold back"))
    if player_input == "yes":
        print(path3)
    else:
        print(path4)
    
    
    

