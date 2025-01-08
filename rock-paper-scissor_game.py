#rock-paper-scissor_game.py

#intro:
print("~~~~~ROCK, PAPER, SCISSOR~~~~~")
#importing the random module & define a list for it :
import random
list = ['ROCK', 'PAPER','SCISSOR']
#programming:
while True:
    my_choice = input("\nEnter your choice from [Rock/Paper/Scissor] to start.. or 'Exit' to exit... = ").strip().upper()
    computer_choice = random.choice(list)
    if my_choice == 'EXIT':
        print("\nClosing......")
        break
    elif my_choice == computer_choice:
        print(f"\nYou Choose : {my_choice}  ;  Computer Choose : {computer_choice}")
        print("\nMatch tie...")
    elif my_choice == 'ROCK':
        print(f"\nYou Choose : {my_choice}  ;  Computer Choose : {computer_choice}")
        if computer_choice == 'PAPER':
            print("\nPaper covers Rock ; Computer Win..")
        else:
            print("\nRock smashes Scissor ; You Win..")
    elif my_choice == 'PAPER':
        print(f"\nYou Choose : {my_choice}  ;  Computer Choose : {computer_choice}")
        if computer_choice == 'ROCK':
            print("\nPaper covers Rock ; You Win..")
        else:
            print("\nScissor cuts Paper ; Computer Win..")
    elif my_choice == 'SCISSOR':
        print(f"\nYou Choose : {my_choice}  ;  Computer Choose : {computer_choice}")
        if computer_choice == 'ROCK':
             print("\nRock smashes Scissor ; Computer Win..")
        else:
             print("\nScissor cuts Paper ; You Win..")
    else:
        print("\nInvalid input.... please enter the correct one..")

#cradit:
print("\n\n\n© Copyright By JPM")
