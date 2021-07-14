import random

def play():
    ''' this function prompts the user to give input and helps computer with its choice. '''
    print("Rules of the Game: \n1. Rock > Scissors \n2. Scissors > Paper \n3. Paper > Rock")
    print("You can opt for the following: \n 1. R -> Rock \n 2. S -> Scissors \n 3. P - Paper")
    
    valid_choices_list = ['R', 'P', 'S']
    user_choice = input("Please Enter your Input: ").upper()
    computer_choice = random.choice(valid_choices_list)

    if user_choice not in valid_choices_list:
        return ("Invalid Input Given. Please try again with valid Inputs.")

    if user_choice == computer_choice:
        return ("It is a tie. No one win....")

    if checkWinner(user_choice, computer_choice):
        return ("Congrats Player, You Won..!!")
    
    return ("Sorry Player, You Lost. Computer Won..!!")


def checkWinner(player, comp):
    ''' this function checks who is winner between the player and the computer and 
        returns True if our user/player is the winner'''
    if(player == 'R' and comp == 'S') or (player == 'S' and comp == 'P') or (player == 'P' and comp == 'R'):
        return True 

print(play())