#Prabath Girish
# 02/08/2022
# Word game with 3 levels: 
# 1. Fruits
# 2.Colors
# 3.Computer parts    
# Choice:

import os, random
os.system('cls')
#define menu:
def menu():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$                                                 $")
    print("$     WELCOME TO THE GUESS THE WORD GAME!!!!!!    $")
    print("$            Level 1: Fruits                      $")
    print("$            Level 2: Colors                      $")
    print("$            Level 3: Computer Parts              $")
    print("$                                                 $")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("Pick the level by typing 1-3")

menu()
#Create word lists and a function to check the level values
ValueError!=int
def L():
    global levelchoice
    levelchoice=input("what level do you want:")
    if int(levelchoice)>3 or int(levelchoice)<1:
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        print("L")
        quit()
# define our word lists:
fruits=["bananas", "grapes", "waterMelon", 'blueberries', 'apples', "blackberries",
    "papaya", 'oranges', 'tomatoes', 'mangos', 'kiwis','strawberries', 'monke' ]
WordBank_Colors=["crimson", "black", "lilac", "white", "orange", "violet", "emerald", "mustard", "sapphire", 'monke']
WordBank_CompParts=["monitor", "motherboard", "keyboard", "mouse", "speakers", "processor", "battery", "monke"]

L()
# Create a function to run for each category choice
def selectWord():
    global word
    if int(levelchoice)==1:
        word=random.choice(fruits)
    elif int(levelchoice)==2:
        word=random.choice(WordBank_Colors)
    elif int(levelchoice)==3:
        word=random.choice(WordBank_CompParts)



def guessFunction():
    global guess
    check=True
    while check:
        try:
            guess=input("\nenter a letter to guess the word: ")
            if guess.isalpha() and len(guess)==1:
                check=False
            else:
                print("only one letter please")
        except ValueError:
            print("only one letter please")
            
gameOn=True
tries=0
letterGuessed=" "
selectWord()
while gameOn:
    
    guessFunction()
    letterGuessed += guess  #letterGuessed=letterGuessed + guess
    if guess not in word:
        tries +=1
        print(tries)# for testing delete when game is ready
    countLetter=0
    for letter in word:
        if letter in letterGuessed:
            print(letter, end=" ")
            countLetter +=1
        else:
            print("_", end=" ")
    if tries > len(word):
        print("\n L, the word was", word)
        reply=input("do you want to play agian:")
        if reply=='y':
            os.system('cls')
            menu()
            tries=0
            L()
            selectWord()
            gameOn=True
    if countLetter == len(word):
        print ("\nyou guessed the word! ")
        #Calculate score
        #playGame()