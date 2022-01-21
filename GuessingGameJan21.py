# # Prabath Girish (1/21/22)
# # Import the os to make the terminal neater
import os, random
os.system('cls')

# "guessing" is a function that uses the "dif" which gets replaced by the difficulty input
# From in class we learned that in order for the game to loop the function/input ability, we need to set to True to keep the game running infinitley
# This is to help keep the game active unless you get the answer correctly (which results in the end of the program), in the case that you don't it keeps the number the same and gives you more chances to guess
# The input at the beginning allows you to select the difficulty you want and chooses a number from the random ranges as we talked about in class
# While the function is still ongoing (meaning there is no correct answer given), the computer keeps giving the opportunities to what to write, and if you give it wrong , it gives a message
# The final things that was added is the ability to quit the program by typing in "quit"

def guessing(dif):
    if int(dif)==1:
        number=random.randint(1,10)
    if int(dif) == 2:
        number=random.randint(1,50)
    if int(dif) == 3:
        number=random.randint(1,100)
    else:
        print("can u read lol")
        quit()
    # print(number) <-- This was used for testing purposes
    while True:
        guess=input("What is your guess: ")
        if str.isnumeric(guess) and int(guess) == number:
            print("Ur actually a mega gamer")
            quit()
        elif guess=="quit":
            print("rage quit lmao")
            quit()
        if int(guess) < number:
            print("ur bad lol. Try higher")
        if int(guess) > number:
            print("ur bad lol. Try lower")

# ! means not
# # Today we are going to learn about user input, strings, type casing, some branching today, and looping if time permits
# # To ask the user what to do, we declare the variable as user info
# #Ask the user to enter specific data via printing
# print("enter a number 1-100" , end=" :-) ")
# #Using imput() returns a string
# # Because we need specifically to be treated as a number, we need to write "int" to mark it as such
# useless=int(input())
# # print(userInfo*3) (Practice test we did before the final one below)
# print("the number divided by 3 is %.2f" %(useless/3))
# easier way to do this:
# 1-16 were neutralized to only show the guessing game

#The print box + Guess the number print is to be used as the game's menu while the rows following have to do the showing of the options in the menu
#the difficulty input is to decide what level you want by typing in 1-3
# The guessing(difficulty) is to help replace the function "dif" with the difficultly 

print("============================================================")
print("|                                                           |")
print("|                 Guess the Number Game                     |")
print("|                                                           |")
print("=============================================================")

print("Level 1: 1-10")
print("Level 2: 1-50")
print("Level 3: 1-100")
difficulty=input("Which level do you want: ")
guessing(difficulty)






# guess= int(input("try to guess my number:"))

# Next let's talk about branching statements(main part)
# If we use the "if" statements after we define our correct number, set what the computer will say after based on the response 
# Use colons to seperate the result based on what happens, and use two equal signs on the true statement 
# At the beggining we imported random for this purpose, by using the random system, we can ask for the computer to generate a number 1-100
# correct_number= random.randint(1,50)
# GameOn=True
# while(GameOn):
#     if guess > correct_number:
#         print("Sorry, your guess is too big, guess again: ")
       


    

# Next we need to be able to loop this until the user guesses correctly, this is called conditional looping. 
# Here we will give them 4 tries to guess the number
