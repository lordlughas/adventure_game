"""
Adventure game that takes user
input choice and give them
a task or instructions according
to their choice. A winner is decided
through the actions of the player
"""

# get time and random modules
import time
import random


def print_pause(message):
    """
    function to print state
    with a delay
    """
    print(message)
    time.sleep(2)

def start_game():
    """
    function to start the game
    and give intro about the game
    """
    print_pause("You find yourself in a mystical land where gods and mortals coexist.")
    print_pause("The villagers speak of a secret cave hidden deep in the mountains,"
                " said to contain the power of the gods themselves.")
    print_pause("What do you want to do?")
    print_pause("1. Embark on a treacherous journey to find the secret cave and open the mythical box.")
    print_pause("2. Seek the guidance of the village elder before making a decision.")

    # get user input to start the game
    player_choice = input("Enter 1 or 2: ")

    if player_choice == "1":
        find_cave()
    elif player_choice == "2":
        seek_guidance()
    else:
        print_pause("Sorry, I don't understand. Please enter 1 or 2.")
        start_game()

def find_cave():
    """
    function to find the cave for the power
    of the gods
    """
    print_pause("You set off on a perilous adventure, navigating through dense" 
                " forests and treacherous terrain until you finally reach the hidden cave.")
    print_pause("Inside, you find an ornate box with ancient inscriptions. What do you want to do?")
    print_pause("1. Open the box and claim the power of the gods.")
    print_pause("2. Leave the cave without opening the box.")

    player_choice = input("Enter 1 or 2: ")

    if player_choice == "1":
        claim_power()
    elif player_choice == "2":
        leave_cave()
    else:
        print_pause("Sorry, I don't understand. Please enter 1 or 2.")
        find_cave()

def claim_power():
    """
    function to get the power inside
    the cave
    """
    print_pause("You cautiously open the box, and a surge of divine energy envelops you.")
    print_pause("You can feel the power of the gods coursing through your veins,"
                " making you nearly invincible.")
    print_pause("With newfound strength, you set out to confront the gods who threaten this land.")
    print_pause("Your epic battle against the gods begins.")
    print_pause("With the power of the gods on your side, " 
                "you defeat them one by one, restoring peace to the land.")
    print_pause("Congratulations, you've won the game!")
    print_pause("You WON! Game over!")

    # option to play again 
    play_again()

def leave_cave():
    """
    function to leave the cave
    after getting the power
    """
    print_pause("You decide not to tamper with the unknown and leave the cave.")
    print_pause("As you exit, you hear whispers among the villagers about your wise decision.")
    print_pause("Unfortunately, your decision to avoid the gods' power means you cannot challenge them.")
    print_pause("You LOOSE! Game over!")
    
    # option to play again 
    play_again()

def seek_guidance():
    """
    function for player to decide
    to follow elder's advice or disregard it
    """
    print_pause("You consult the village elder, who imparts ancient wisdom.")
    print_pause("They caution you about the dangers of meddling with divine "
                "power and advise against seeking the gods.")
    print_pause("What do you want to do now?")
    print_pause("1. Follow the elder's advice and avoid the secret cave.")
    print_pause("2. Disregard the elder's counsel and proceed to find the cave and open the box.")

    # option for player choice
    player_choice = input("Enter 1 or 2: ")
    if player_choice == "1":
        follow_advice()
    elif player_choice == "2":
        find_cave()
    else:
        print_pause("Sorry, I don't understand. Please enter 1 or 2.")
        seek_guidance()

def follow_advice():
    """
    function for player to follow the
    elders advice or not
    """
    print_pause("You heed the elder's wisdom and live a peaceful "
                "life in the village, avoiding any encounters with the gods.")
    # the decision of win or loose is picked at random
    if random.choice([True, False]):
        print_pause("You WIN, because you found peace and happiness!")
        print_pause("Game over!")
    else:
        print_pause("Ouch, The demons took over the village and caused chaos!")
        print_pause("You LOOSE! Game over!")
    # option to play again 
    play_again()

def find_demon():
    """
    function to meet demon
    """
    print_pause("As you continue your journey, you return to "
                "the village and discover a terrible secret.")
    print_pause("A demon has been terrorizing the village, causing suffering and chaos.")
    print_pause("What do you want to do?")
    print_pause("1. Confront the demon and fight it to protect the village.")
    print_pause("2. Choose to run away from the village to avoid the demon's wrath.")

    # get player choice
    player_choice = input("Enter 1 or 2: ")

    if player_choice == "1":
        confront_demon()
    elif player_choice == "2":
        run_away()
    else:
        print_pause("Sorry, I don't understand. Please enter 1 or 2.")
        find_demon()


def confront_demon():
    """
    function for player to confront
    the demon and either fight to win or loose
    """
    print_pause("You bravely decide to confront the demon to protect the villagers.")
    print_pause("With the power of the gods on your side, "
                "you engage in a fierce battle with the demon.")
    print_pause("Suddenly, a bolt of lightning strikes the "
                "demon, weakening it significantly.")
    
    # the decision of win or loose is picked at random
    if random.choice([True, False]):
        print_pause("You summon the gods' power and defeat the demon.")
        print_pause("The village is saved, and you are hailed as a hero!")
        print_pause("Congratulations, you've won the game with the "
                    "gratitude of the villagers and the power of the gods!")
        print_pause("You WIN! Game over!")
    else:
        print_pause("Unfortunately, the demon's strength proves "
                    "too much, and you are defeated.")
        print_pause("The village continues to suffer.")
        print_pause("You LOOSE! Game over!")
    # option to play again     
    play_again()

def run_away():
    """
    function to make the player
    run away as he makes this choice
    """
    print_pause("Fearing the demon's immense power, you make the "
                "difficult decision to run away from the village to avoid its wrath.")
    print_pause("You leave behind the villagers who continue to suffer.")
    print_pause("You LOOSE! Game over!")
    # option to play again 
    play_again()

def play_again():
    """
    function to request the user to play
    again or end the game
    """
    print_pause("Do you want to play again? (yes/no)")
    # get player choice to continue the game
    player_choice = input().lower()

    if player_choice == "yes":
        # user choose to continue 
        start_game()
    elif player_choice == "no":
        # user ends game
        print_pause("Okay, Thank you for playing.")
    else:
        print("Sorry I don't understand. Please enter 'yes' or 'no'.")
        play_again()


# Start the game
start_game()
