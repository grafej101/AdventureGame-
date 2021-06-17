import file
import random 

things = [
creature = ['dragon', 'wicked fairie', 'troll', 'dinosaur', 'monster']


random_creature = random.choice(creature)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + random_creature +
                " is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.")


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Please enter a valid input.")
    return response


def choice(items):
    game_choice = valid_input("\n"
                              "Enter 1 to knock on the door of the house.\n"
                              "Enter 2 to peer into the cave.\n"
                              "What would you like to do?\n"
                              "(Please enter 1 or 2.)\n",
                              "1", "2")
    if "1" in game_choice:
        choice_house(items)
    elif "2" in game_choice:
        choice_cave(items)
    else:
        print_pause("Please enter a valid input.")


def choice_house(items):
    print_pause("You approach the door of the house. ")
    print_pause("You are about to knock when the door opens"
                "and out steps a " + random_creature + ".")
    print_pause("Eep! This is the " + random_creature + "\'s house!")
    print_pause("The " + random_creature + " attacks you!")
    if "sword" in items:
        response = valid_input("Would you like to (1) fight "
                               "or (2) run away?\n",
                               "1", "2").lower()
        if "1" in response:
            print_pause("As the " + random_creature + " moves to attack, "
                        "you unsheathe your new sword. "
                        "The Sword of Ogoroth shines brightly in your hand "
                        "as you brace yourself for the attack. "
                        "But the " + random_creature + " takes one look "
                        "at your shiny new toy and runs away! "
                        "You have rid the town of the " + random_creature +
                        ".\n"
                        "You are victorious!")
            play_again_prompt()
        if "2" in response:
            print_pause("You run back into the field. Luckily, you don't seem "
                        "to have been followed.")
            choice(items)
        else:
            print_pause("Please enter a valid input.")
    else:
        print_pause("You feel a bit under-prepared for this, "
                    "with only having a tiny dagger.")
        response = valid_input("Would you like to (1) fight "
                               "or (2) run away?" "\n", "1", "2").lower()
        if "1" in response:
            print_pause("You do your best..."
                        "but your dagger is no match "
                        "for the " + random_creature + ".\n"
                        "You have been defeated!")
            play_again_prompt()
        if "2" in response:
            print_pause("You run back into the field. "
                        "Luckily, you don't seem to have been followed.")
            choice(items)
        else:
            print_pause("Please enter a valid input.")


def choice_cave(items):
    print_pause("You peer cautiously into the cave.")

    if "sword" in items:
        print_pause("You've been here before, and gotten all the good stuff.\n"
                    "It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave. "
                    "Your eye catches a glint of metal behind a rock. "
                    "You have found the magical Sword of Ogoroth! "
                    "You discard your silly old dagger "
                    "and take the sword with you. ")
        items.append("sword")
    print_pause("You walk back out to the field.")
    choice(items)


def play_again_prompt():
    response = valid_input("Would you like to play again? (yes/no) ",
                           "yes", "no").lower()
    while True:
        if "yes" in response:
            print_pause("Excellent! Restarting the game ...")
            play_game()
        elif "no" in response:
            print_pause("Thanks for playing! See you next time.")
            exit()


def play_game():
    items = []
    intro()
    choice(items)


play_game()
