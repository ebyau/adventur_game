import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def intro(enemy):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here,"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                "(but not very effective) dagger.")


def get_enemy():
    enemies = ['troll', 'dragon', 'pirate',
               'eerie', 'wicked fairie', 'gorgon']
    return random.choice(enemies)


def house(enemy, weapons):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door"
                "opens and out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print(f"The {enemy} attacks you!")
    if 'sword' not in weapons:
        print_pause("You feel a bit under-prepared for this,"
                    " what with only having a tiny dagger.")
    else:
        pass


def choice():
    print_pause("")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")


def fight(enemy, weapons):
    if 'sword' in weapons:
        print_pause(f"As the f{enemy} moves to attack, you unsheath"
                    " your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your"
                    "hand as you brace yourself for the attack.")
        print_pause(f"But the {enemy} takes one look at your"
                    f" shiny new toy and runs away!")
        print_pause(f"You have rid the town of the {enemy}. "
                    f"You are victorious!")
        print('*' * 30)
        print_pause("YOU HAVE WON!!!!!")
        print('*' * 30)
        play_again(enemy, weapons)
    else:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {enemy}.")
        print_pause("You have been defeated!")
        print_pause("YOU HAVE LOST!!! SORRY PAL")

        play_again(enemy, weapons)


def run_back():
    print_pause("You run back into the field. Luckily,"
                " you don't seem to have been followed.")


# ------------ CAVE FUNCTIONS----------------------------

def cave(weapons):
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger and"
                " take the sword with you.")
    print_pause("You walk back out to the field.")


def sword_in_bag(weapons):
    print_pause("You peer cautiously into the cave.")
    print_pause("You've been here before, and gotten all the"
                "good stuff. It's just an empty cave now.")
    print_pause("You walk back out to the field.")


# --------------- PLAY CONTROL FUNCTIONS------------------>


def play(enemy, weapons):
    choice()
    response = input("What would you like to do?\n"
                     "(Please enter 1 or 2.)\n")

    if response == '1':
        house(enemy, weapons)
        action = input("Would you like to (1) fight "
                       "or (2) run away? \n")
        if action == '1':
            fight(enemy, weapons)
            play_again()
            # response = input("Would you like to play again y/n").lower()

        elif action == '2':
            run_back()
            play(enemy, weapons)
        else:
            action = input("(Please enter 1 or 2)")

    elif response == '2':
        if 'sword' in weapons:
            sword_in_bag(weapons)
            play(enemy, weapons)
        else:
            cave(weapons)
            weapons.append('sword')
            play(enemy, weapons)

    else:
        input("Please enter 1 or 2.)\n")


def play_again(enemy, weapons):
    response = input("Would like to play again (y/n)\n").lower()

    if response == 'y':
        print_pause("Excellent! Restarting the game ...")
        start_game()
    elif response == 'n':
        print_pause("Thanks for playing! See you next time.")
    else:
        response = input("Would like to play again (y/n)\n").lower()


def start_game():
    enemy = get_enemy()
    weapons = []
    intro(enemy)
    play(enemy, weapons)


start_game()
