# Prabath Girish (2/2/22)
# Today we are going to make a word game with the code we learned in class
#Pseudo Code:
# Create a list of at  least 5 words that  we can choose from
# Tell the user if the letter they guessed is in the word
# Give them a certain number of tries and ask them to guess the word at the end
# import os for neatness and random for random selection
import os, random
os.system('cls')
#define our menu
def menu():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$                                                 $")
    print("$     WELCOME TO THE GUESS THE WORD GAME!!!!!!    $")
    print("$                                                 $")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("ALL WORDS ARE 5 LETTERS EACH, you get 5 tries")


menu()

# define our words in our list for the computer to choose from
Wordbank= ["onion", "python", "giant", "phone", "enter", "light", "couch"]
# now we make the computer select the word it wants to use for that round
word=random.choice(Wordbank)
# print(word)  <--- This was used for testing

# create a check to make sure the user can only put in letters, and set game on to true to continue
check=True
while check:
    letter= input("please give your letter guess:")
    if len(letter)>1 or not letter.isalpha():
        print("That's not a real letter")
    else:
        check=False
        GameOn=True

# Set in a function for 5 tries if we can check the letters if they are in the word
tries = 0
while GameOn==True:
    if letter in word:
        print (letter, "is in the word")
        tries=tries+1
        letter=input("please give your letter guess:")
    elif letter not in word:
        print(letter,"is not in the word")
        tries=tries+1
        letter=input("please give your letter guess:")
    elif len(letter)>1 or not letter.isalpha():
        print("Invalid move try again later")
        quit()
    if tries>=5:
        finalGuess=input("what do you think the word is:")
        if finalGuess==word:
            print("OMG! You got the word!")
            response=input("do you want to play again (y for yes, n for no):")
            if response=="y" or response=="Y":
                os.system('cls')
                menu()
                word=word=random.choice(Wordbank)
                letter=input("please give your letter guess:")
            else:
                GameOn=False
                quit()
        else:
            print("oof you didnt get the word, it was:", word)
            response=input("do you want to play again (y for yes, n for no):")
            if response=="y" or response=="Y":
                os.system('cls')
                menu()
                word=word=random.choice(Wordbank)
                letter=input("please give your letter guess:")
            else:
                GameOn=False
                quit()