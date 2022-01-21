# # Prabath Girish (1/21/22)
# # Import the os to make the terminal neater
import os, random
from pickle import TRUE
os.system('cls')

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
guess= int(input("try to guess my number, it is between 1-50:"))

# Next let's talk about branching statements(main part)
# If we use the "if" statements after we define our correct number, set what the computer will say after based on the response 
# Use colons to seperate the result based on what happens, and use two equal signs on the true statement 
# At the beggining we imported random for this purpose, by using the random system, we can ask for the computer to generate a number 1-100
correct_number= random.randint(1,50)
GameOn=True
while(GameOn):
    if guess > correct_number:
        print("Sorry, your guess is too big, guess again: ")

    if guess < correct_number:
        print ("Sorry, your guess is too small, guess again:")

    if guess == correct_number:
        print("congratulations! You found out my number")

# Next we need to be able to loop this until the user guesses correctly, this is called conditional looping. 
# Here we will give them 4 tries to guess the number
