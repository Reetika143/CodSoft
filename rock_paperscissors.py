#python program for rock,paper,scissors.

import random

def rock_paper_scissors():
    actions = ['rock','paper','scissors']

    while True:
    # Get user's action
     user_action = input("Enter rock,paper,or scissors (or 'q' to quit):")
     if user_action.lower() =='q':
       break 
    # Validate users action
    while user_action not in actions:
        print("Invalid choice.Please enter rock,paper,or scissors.")
        user_action = input("enter rock,paper,or scissors:")

        #Computer makes a random action
        computer_action = random.choice(actions)
        print(f"Computer chooses:{computer_action}")

        #Determine the winner
        if user_action == computer_action:
            print("its a tie!")
        elif(user_action == 'paper' and computer_action == 'rock')or\
            (user_action == 'rock' and computer_action == 'scissors')or\
            (user_action == 'scissors' and computer_action == 'paper'):
            print("You win!")
        else:
            print("computer wins!")

 #Run the game
rock_paper_scissors()    

