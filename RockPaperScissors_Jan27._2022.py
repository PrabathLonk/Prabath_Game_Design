# Prabath Girish (1/27/2022)
# Today we're going to make a rock paper scissors game and figure out how to pit the user against the computer

# Psuedo code:
# Make a menu for the game to return to
# Get the computer to generate rock, paper, scissors in the form of numbers
# Convert the user's attempt into a number and compare it with the computer's generated number
# Make a mispell scenario if the user mispells the work
# Create a lop to reset the game after it is over
# Failsafe to prevent crashing if there is no valide input

# import the os
import os, random
os.system('cls')

def menu():
    print("++++++++++++++++++++++++++++++++++++++++")
    print("|                                      |")
    print("|   Welcome to ROCK, PAPER, SCISSORS   |")
    print("|                                      |")
    print("++++++++++++++++++++++++++++++++++++++++")
    
menu()
CompAction = random.randint(1,3)
print(CompAction)
UserAction = input("Type in your choice (1 for rock, 2 for paper, 3 for scissors):")

if int(UserAction)==int(CompAction):
    print ("You tied! Want to try again")
elif int(UserAction)==1 and int(CompAction)==2:
    print("Paper covered your rock! You lose.")
elif int(UserAction)==2 and int(CompAction)==3:
    print ("Your paper was cut by scissors. You lose.")
elif int(UserAction)==3 and int(CompAction)==1:
    print("Your scissors were crushed by rock. You lose.")
elif int(UserAction)==2 and int(CompAction)==1:
    print ("Your paper covers the opposing rock! You win!")
elif int(UserAction)==3 and int(CompAction)==2:
    print("Your scissors cut the opposing paper.You win!")
elif int(UserAction)==1 and int(CompAction)==3:
    print("Your rock crushed the opposing scissors. You win!")
else:
    print("Illegal rock paper scissors move. Try again ")
    response = input("do you want to play again (y for yes, n for no): ")
    if response =="y":
        os.system('cls')
        menu()
        CompAction= random.randint(1,3)

