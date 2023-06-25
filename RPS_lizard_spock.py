# Play Rock-Paper-Scissors-Lizard-Spock against the computer!

# The random.choice() method allows you to pick an element at random, in this
# case from a list;
from random import choice

# Throughout this program, I use many print() statements to enhance legibility
# in the terminal, e.g. below;
print()
print("This is Rock-Paper-Scissors-Lizard-Spock! You will be playing\n" 
        "against the computer. Please enter your selection now...")
print()

# We use lower() to control for human error in the input, e.g. "ROCK";
human = input().lower()

# Unlike the other options, "Spock" is a name so the first letter must be
# capitalized, this if statement takes care of that;
if human == "spock":
    human = "Spock"
print()

objects = ["rock","paper","scissors","lizard","Spock"]

# We use the random.choice() method to have the computer's object selected at
# random from the list; we don't need to use lower() in this case since the
# list elements are already spelled out correctly;
computer = choice(objects)

print(f"You chose {human}, and the computer chooses {computer}.")
print()


# Create a dictionary that will contain all possible winning combinations,
# the way it is organized is based on the assumption that the human chose
# the key as their object and the computer chose one of the values; 
# this way we can avoid writing out the numerous if statements we would 
# otherwise need;
win_combos = {
        
        'rock': {
            'scissors': "Rock breaks scissors",
            'lizard': "Rock crushes lizard"
        },
        
        'paper': {
            'rock': "Paper covers rock",
            'Spock': "Paper disproves Spock"
        },

        'scissors': {
            'paper': "Scissors cut paper",
            'lizard': "Scissors decapitate lizard"
        },

        'lizard': {
            'paper': "Lizard eats paper",
            'Spock': "Lizard poisons Spock"
        },

        'Spock': {
            'rock': "Spock vaporizes rock",
            'scissors': "Spock smashes scissors"
        }

}

'''
# Create a dictionary that will contain all possible losing combinations,
# the way it is organized is based on the assumption that the human chose
# the key as their object and the computer chose one of the values; 

lose_combos = {

        'rock': {
            'paper': "Paper covers rock",
            'lizard': "Spock vaporizes rock"
        },
        
        'paper': {
            'rock': "Paper covers rock",
            'Spock': "Paper disproves Spock"
        },

        'scissors': {
            'paper': "Scissors cut paper",
            'lizard': "Scissors decapitate lizard"
        },

        'lizard': {
            'paper': "Lizard eats paper",
            'Spock': "Lizard poisons Spock"
        },

        'Spock': {
            'rock': "Spock vaporizes rock",
            'scissors': "Spock smashes scissors"
        }


}
'''


# These will be tacked onto the ends of the print statements from the 
# dictionary above;

win_msg = ", therefore you win!"

lose_msg = ", therefore you lose!"


# This if statement ensures the rest of the program doesn't run in the case
# of improper input, e.g. "Bicycle";
if human in objects:
   
    if human == computer:
        print(f"You and the computer both chose {human}, it's a draw!")
        print()

    elif computer in win_combos[human]:
        print(win_combos[human][computer]+win_msg)
        print()
    
    elif human in win_combos[computer]:
        print(win_combos[computer][human]+lose_msg)
        print()

else:
    print("This is an invalid input, please run the program again from the\n"
            "beginning.")
    print()

'''
# This if statement ensures the rest of the program doesn't run in the case
# of improper input, e.g. "Bicycle";
if human in objects:

    if human == "rock" and computer == "paper":
        print("Paper covers rock, therefore you lose!")
        print()

    elif human == "rock" and computer == "scissors":
        print("Rock breaks scissors, therefore you win!")
        print()

    elif human == "paper" and computer == "scissors":
        print("Scissors cut paper, therefore you lose!")
        print()

    elif human == "paper" and computer == "rock":
        print("Paper covers rock, therefore you win!")
        print()

    elif human == "scissors" and computer == "rock":
        print("Rock breaks scissors, therefore you lose!")
        print()

    elif human == "scissors" and computer == "paper":
        print("Scissors cut paper, therefore you win!")
        print()

    else:
        print("Both you and the computer chose the same object, therefore it's a stalemate.")
        print()

else:
    print("This is an invalid input, please run the program again from the\n"
            "beginning.")
    print()
'''
