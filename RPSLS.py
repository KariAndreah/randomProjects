# Rock-paper-scissors-lizard-Spock template

import random
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
def name_to_number(name):
    if name == 'rock':
        return int(0)
    elif name == 'Spock':
        return int(1)
    elif name == 'paper':
        return int(2)
    elif name == 'lizard':
        return int(3)
    elif name == 'scissors':
        return int(4)
    else:
        print "error" 

    # delete the following pass statement and fill in your code below
 
    # convert name to number using if/elif/else
    # don't forget to return the result!                                                                                      


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print 'error' 
   
   
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(name): 
    # delete the following pass statement and fill in your code below
   
    
    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    player_number = name_to_number(name)
    comp_number = random.randrange(0,5) 
    
    print "Player chooses ", name
    print "Computer chooses ", number_to_name(comp_number) 
    
    
    if (comp_number - player_number) % 5 == 1:
        print "Computer Wins!"
    elif (comp_number - player_number) % 5 == 2:
        print "Computer Wins!"
    elif (comp_number - player_number) % 5 == 3:
        print "Player Wins!"
    elif (comp_number - player_number) % 5 == 4:
        print "Player Wins!"
    else: 
        print "Player and Computer tie!"
        
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

