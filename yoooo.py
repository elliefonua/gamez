




def locater():
    print("welcome to Gold Quest Island!")
    print("where would you like to go?\n")
    locations = ["cave", "forest", "mountain", "river", "desert"]
    for index, location in enumerate(locations):
        print(f"{index + 1}. {location}")
    


    choice = int(input("choose a number: \n"))
    return locations[choice - 1]



def fighter(boss_name):
    print(f"you encounter the {boss_name}!")
    action = input("do you want to fight head-on or quit the game? (fight/quit): ").strip().lower()
    

    if action == "fight":
        print(f"you out rozzed that sigma, the {boss_name}, and won~!")
        return True
    else:
        print("you've chosen to quit the game... bye.. for now. [TEEHEE]")
        return False



def player():
    goldchatt = 0
    while goldchatt < 5:
        location = locater()
        print(f"you have chosen to go to the {location}.")
        
        if location == "cave":
            if fighter("goblin"):
                goldchatt += 1
        elif location == "forest":
            if fighter("troll"):
                goldchatt += 1
        elif location == "mountain":
            if fighter("dragon"):
                goldchatt += 1
        elif location == "river":
            print("you found a banana! It gives you energy.")
        elif location == "desert":
            print("you found a hidden treasure! You collect 1 gold.")
            goldchatt += 1
        


        print(f"gold collected: {goldchatt}/5")
    

    print("congratulations! You have collected all the gold!\n")
    print("now, you face the monkey king to steal his mountain of gold!\n")


player()
