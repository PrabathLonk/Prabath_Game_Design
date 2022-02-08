import os, random
os.system('cls')


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



menu()



Wordbank_Food= ["onion", "grape", "bread", "pizza", "pasta", "artichoke", "lychee", "baguette", "yogurt"]
WordBank_Colors=["crimson", "black", "lilac", "white", "orange", "violet", "emerald", "mustard", "sapphire"]
WordBank_CompParts=["monitor", "motherboard", "keyboard", "mouse", "speakers", "processor", "battery"]
levelchoice=input("What is your level choice:")
def selectWord():
    global word
    if int(levelchoice)==1:
        word=random.choice(Wordbank_Food)
    elif int(levelchoice)==2:
        word=random.choice(WordBank_Colors)
    elif int(levelchoice)==3:
        word=random.choice(WordBank_CompParts)


def guessCheck():
    global answer
    check =True
    while check:
        answer = input("guess a letter: ")
        if len(answer)>1 or not answer.isalpha():
            print("NOOOOO")
        else:
            check = False

Gameon = True
tries = 0
letterguessed  = " "
while Gameon:
    guessCheck()
    if answer not in word:
        tries=tries+1
    for answer in word:
        if answer in word:
            print (answer, end= " ")
            tries=tries+1
        else:
            print("_", end=" ")
        

   



# if answer not in letterguessed:
#         tries=tries+1
#         print("Thats not in the word") # for testing
#     countletter=0
#     for answer in letterguessed:
#         if answer in letterguessed:
#             print(answer, end= " ")
#             tries=tries+1
#         else:
#             print("_", end=" ")
#     if tries > 6:
#         print("\nyou ran outta chances")
#         # playgame()
#     if countletter == len(word):
#         print("you guessed it!")
#         # calculatescore()
#         # playgame()