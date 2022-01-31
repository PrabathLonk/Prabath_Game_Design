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
#define the menu to call it back to the game when needed
def menu():
    print("++++++++++++++++++++++++++++++++++++++++")
    print("|                                      |")
    print("|   Welcome to ROCK, PAPER, SCISSORS   |")
    print("|                                      |")
    print("++++++++++++++++++++++++++++++++++++++++")
    
#Call the menu and randomize the computer's choice
menu()
CompAction = random.randint(1,3)

# Allow for the user to pick their choice with each number corresponding with the respective choice
UserAction = input("Type in your choice (1 for rock, 2 for paper, 3 for scissors):")

# Set gameOn to true to allow for our function to loop when the game is running
GameOn=True
#Define what our value error is
ValueError!=int

# Create an active functon that runs when the game is on containing each of the possible combinations of what can be done
# Each of these permutations has to do with the combinations of the winning, losing, and tie scenarios
# After each input possibility we give the option to reset the game or quit  
# The first scenario given is 
while GameOn==True:   
    # print(CompAction) <-- Used for testing each choice
    if int(UserAction)==int(CompAction):
        print ("You tied!")
        response = input("do you want to play again (y for yes, n for no): ")
        if response =="y" or response =="Y":
            os.system('cls')
            menu()
            CompAction= random.randint(1,3)
            UserAction = input("Type in your choice (1 for rock, 2 for paper, 3 for scissors):")
        elif response=="n" or response=="N":
            GameOn=False
            quit()
    elif int(UserAction)==1 and int(CompAction)==2:
        print("Paper covered your rock! You lose.")
        response = input("do you want to play again (y for yes, n for no): ")
        if response =="y" or response=="Y":
            os.system('cls')
            menu()
            CompAction= random.randint(1,3)
            UserAction = input("Type in your choice (1 for rock, 2 for paper, 3 for scissors):")
        elif response=="n" or response=="N":
            GameOn=False
            quit()
    elif int(UserAction)==2 and int(CompAction)==3:
        print ("Your paper was cut by scissors. You lose.")
        response = input("do you want to play again (y for yes, n for no): ")
        if response =="y" or response=="Y":
            os.system('cls')
            menu()
            CompAction= random.randint(1,3)
            UserAction = input("Type in your choice (1 for rock, 2 for paper, 3 for scissors):")
        elif response=="n" or response=="N":
            GameOn=False
            quit()
    elif int(UserAction)==3 and int(CompAction)==1:
        print("Your scissors were crushed by rock. You lose.")
        response = input("do you want to play again (y for yes, n for no): ")
        if response =="y" or response=="Y":
            os.system('cls')
            menu()
            CompAction= random.randint(1,3)
            UserAction = input("Type in your choice (1 for rock, 2 for paper, 3 for scissors):")
        elif response=="n" or response=="N":
            GameOn=False
            quit()
    elif int(UserAction)==2 and int(CompAction)==1:
        print ("Your paper covers the opposing rock! You win!")
        response = input("do you want to play again (y for yes, n for no): ")
        if response =="y" or response=="Y":
            os.system('cls')
            menu()
            CompAction= random.randint(1,3)
            UserAction = input("Type in your choice (1 for rock, 2 for paper, 3 for scissors):")
        elif response=="n" or response=="N":
            GameOn=False
            quit()
    elif int(UserAction)==3 and int(CompAction)==2:
        print("Your scissors cut the opposing paper.You win!")
        response = input("do you want to play again (y for yes, n for no): ")
        if response =="y" or response=="Y":
            os.system('cls')
            menu()
            CompAction= random.randint(1,3)
            UserAction = input("Type in your choice (1 for rock, 2 for paper, 3 for scissors):")
        elif response=="n" or response=="N":
            GameOn=False
            quit()
    elif int(UserAction)==1 and int(CompAction)==3:
        print("Your rock crushed the opposing scissors. You win!")
        response = input("do you want to play again (y for yes, n for no): ")
        if response =="y" or response=="Y":
            os.system('cls')
            menu()
            CompAction= random.randint(1,3)
            UserAction = input("Type in your choice (1 for rock, 2 for paper, 3 for scissors):")
        elif response=="n" or response=="N":
            GameOn=False
            quit()
    elif int(UserAction)>3 or ValueError:
        print("Illegal rock paper scissors move. Try again ")
        response = input("do you want to play again (y for yes, n for no): ")
        if response =="y" or response=="Y":
            os.system('cls')
            menu()
            CompAction= random.randint(1,3)
            UserAction = input("Type in your choice (1 for rock, 2 for paper, 3 for scissors):")
        elif response=="n"or response=="N":
            GameOn=False
            quit()
    # if UserAction==ValueError:
    #     print("Invalid move, try again later!")
    #     response = input("do you want to play again (y for yes, n for no): ")
    #     if response =="y" or response =="Y":
    #         os.system('cls')
    #         menu()
    #         CompAction= random.randint(1,3)
    #         UserAction = input("Type in your choice (1 for rock, 2 for paper, 3 for scissors):")
    #     elif response=="n" or response=="N":
    #         GameOn=False
    #         quit()
# Extra notes:
#Tuple is a variable that works like a collection of numbers and can help pull out items in the list needed for certain situations
# An array is a list of items that can be used to collect needed values and use them in specific scenarios or to elect a random one of them
