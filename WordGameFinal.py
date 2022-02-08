#Prabath Girish (2/8/22)
# Today we are going to add to the word game except with mulitple levels and a scoring system
# import os and random
import os, random
os.system('cls')

# Make our menu:
def menu():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$                                                 $")
    print("$     WELCOME TO THE GUESS THE WORD GAME!!!!!!    $")
    print("$            Level 1: Foods                       $")
    print("$            Level 2: Colors                      $")
    print("$            Level 3: Computer Parts              $")
    print("$                                                 $")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("Pick the level by typing 1-3")

# Create our word bank for each level and print the menu:
menu()
Wordbank_Food= ["onion", "grape", "bread", "pizza", "pasta", "artichoke", "lychee", "baguette", "yogurt"]
WordBank_Colors=["crimson", "black", "lilac", "white", "orange", "violet", "emerald", "mustard", "sapphire"]
WordBank_CompParts=["monitor", "motherboard", "keyboard", "mouse", "speakers", "processor", "battery"]

# Allow the user to pick the level:
levelchoice=input("Pick your level:")
# Create statements for each choice
 
def selectWord():
    global word
    if int(levelchoice)==1:
        word=random.choice(Wordbank_Food)
    elif int(levelchoice)==2:
        word=random.choice(WordBank_Colors)
    elif int(levelchoice)==3:
        word=random.choice(WordBank_CompParts)
selectWord()
print (word)
#Create a check to make sure only valid letters are inputted
# Also use the global function to make sure the variable is usable everywhere
def guessCheck():
    check=True
    global letter
    while check:
        letter= input("Guess a letter:")
        if len(letter)>1 or not letter.isalpha:
            print("Can't do that. Not a letter guess")
        else:
            check=False

# Set GameOn to true and we need to store letters guessed:
GameOn=True
tries=0
letterguessed=" "
while GameOn:
    guessCheck()
    if letter not in word:
        tries=tries+1
        print ("Thats not in the word")
    for letter in word:
        tries=tries+1
        if letter in letterguessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    if tries==6:
        finalGuess=input("What do you think the word is:")
        if finalGuess==word:
            print ("YOU GUESSED THE WORD HOORAY!")
        else:
            print("OOF! The word was", word)
