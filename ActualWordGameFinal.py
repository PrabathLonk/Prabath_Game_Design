#Prabath Girish
# 02/08/2022
# Word game with 3 levels: 
# 1. Fruits
# 2.Colors
# 3.Computer parts    
# Choice:

import os, random
os.system('cls')
highscore=0
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
    print("Pick the level by typing 1-3(q to quit, 4 for highscore)")

menu()
#Create word lists and a function to check the level value
# def L():
#     global levelchoice
#     levelchoice=input("what level do you want:")
#     if int(levelchoice)>3 or int(levelchoice)<1:
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         print("L")
#         quit()


# define our word lists:
fruits=["bananas", "grapes", "watermelon", 'blueberries', 'apples', "blackberries",
    "papaya", 'oranges', 'tomatoes', 'mangos', 'kiwis','strawberries', 'monke' ]
WordBank_Colors=["crimson", "black", "lilac", "white", "orange", "violet", "emerald", "mustard", "sapphire", 'monke']
WordBank_CompParts=["monitor", "motherboard", "keyboard", "mouse", "speakers", "processor", "battery", "monke"]

# Create a function to run for each category choice
levelchoice=" "
def LevelChoice():
    global word
    levelchoice = input("What level do you want:")
    if "q" in levelchoice:
        print("THANKS FOR PLAYING") 
        quit()
        levelchoice=input("What level do you want:")
    levelchoice=(int)(levelchoice)   
    if levelchoice==1:
        word=random.choice(fruits)
    elif levelchoice==2:
        word=random.choice(WordBank_Colors)
    elif levelchoice==3:
        word=random.choice(WordBank_CompParts)
    elif int(levelchoice)>4 or int(levelchoice)<1:
        print("L")
        quit()
    elif levelchoice==4:
        print("The highscore is", highscore)
        levelchoice = input("What level do you want:")
        # print("Thanks for playing.Try again soon!")
        # print("Your high score was", highscore)
        quit()
    



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
LevelChoice()
while gameOn:
    guessFunction()
    letterGuessed += guess  #letterGuessed=letterGuessed + guess
    if guess not in word:
        tries +=1
        # print(tries)<--for testing delete when game is ready
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
            LevelChoice()
            gameOn=True
        if reply=='n':
            os.system('cls')
            print("Thanks for playing.Try again soon!")
            quit()
    if countLetter == len(word):
        print ("you guessed the word!")
        score=len(word)-tries
        if score>highscore:
            highscore=score
            score=0
        reply=input("Do you want to play again(y for yes, n for no):")
        if reply=='y':
            os.system('cls')
            menu()
            countLetter=0
            letterGuessed=" "
            tries=0
            LevelChoice()
            gameOn=True   
        elif reply=='n':
             os.system('cls')
             print("Thanks for playing. Your score was",highscore)
             quit()


# os.system('cls')
#             score=len(word)
#             print("Thanks for playing. Your score was",score)
