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
# the key as their object and the computer chose one of the subkeys;
# if the inverse is true, then that means it is a losing combination, from the
# perspective of the human;
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



# One of these will be tacked onto the ends of the print statements from the 
# dictionary above (unless it was a draw);

win_msg = ", therefore you win!"

lose_msg = ", therefore you lose!"


# This if statement ensures the rest of the program doesn't run in the case
# of improper input, e.g. "Bicycle";
if human in objects:
    
    if human == computer:
        print(f"You and the computer both chose {human}, it's a draw!")
        print()

    # The win_combos dictionary keys are the human's choice, and the subkeys
    # are the computer's choice; ergo if the combination of these choices can
    # be found in the dictionary, in this order, then the human must have won;
    elif computer in win_combos[human]:
        print(win_combos[human][computer]+win_msg)
        print()
   
    # Conversely, if the combination cannot be found in win_combos, then it 
    # must be a losing combination; ergo we swap the positions of the key and
    # subkey, which means it must be a losing combination;
    elif human in win_combos[computer]:
        print(win_combos[computer][human]+lose_msg)
        print()

else:
    print("This is an invalid input, please run the program again from the\n"
            "beginning.")
    print()

