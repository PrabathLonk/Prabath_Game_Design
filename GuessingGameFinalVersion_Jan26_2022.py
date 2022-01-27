
# Prabath Girish
# Game Design Class (Guessing Game Contd.)
# 1/25/21

# we are going to learn about input() function,type casting, branching, and looping

# declare the variable
#print("Enter a number from 1-10:")
#userInfo= int(input()) #input returns string, we must type cast because we need a number
#print("The number is %.2f " %(userInfo/3)) #we use .2 float to get the correct formatting


import os, random
os.system('cls')

#guess = int(input("Please give me a number"))
 
def menu():
    print(" ==========================================================================")
    print(" |                                                                        |")
    print(" |     Get Ready To Play: THE NUMBER GUESSING GAME! (Type number 1-3)     |")
    print(" |             level 1(3 tries): 1-10 (higher or lower mode)              |")
    print(" |                 level 2(4 tries): 1-50 (division mode)                 |")
    print(" |                 level 3(5 tries): 1-100 (evil mode)                    |")
    print(" ==========================================================================")
    print("LVL 1:Higher or lower tells you if the answer is higher or lower than your guess")
    print("LVL 2:The computer will give you ONE clue, regarding a number the answer is or isn't divisible by")
    print("LVL 3:Try it out...IF YOU DARE 😈😈😈")
    
    
menu()
tries=0
ValueError != int
check = True
while check:
        try:
            choice =int(input("level choice:"))
            check = False
        except ValueError:
            print("Can u read lol. Put a level number 1-3 please.")

difficulty= int(choice)  

def guessing(dif):
    if int(dif)==1:
        number_onetoten= random.randint(1,10)
    elif int(dif)==2:
        number_onetothrity= random.randint(1,30)
    elif int(dif)==3:
        number_onetofifty= random.randint(1,50)    
    elif int(dif)>3:
        print("That's not a level.Error404")
        quit()
        

Level1Ans = random.randint(1,10)
Level2Ans = random.randint(1,50)
Level3Ans = random.randint(1,100)
divisor=random.randint(1,3)



while int(difficulty) == 1:
        guess = input("What is your guess:")   
        if int(guess) > Level1Ans:
                print("Ur bad lol. The number is too big")
                tries = tries+1
                if tries>=3:
                    print("oof! You ran out of tries, the number was:", Level1Ans)
                    response= input("Do you want to play again (Y for yes, N for no)")
                    if response=="y":
                        os.system('cls')
                        menu()
                        tries=0
                        choice =int(input("level choice:"))
                        Level1Ans = random.randint(1,10)
                        if int(choice)>3:
                            print("That's not a level.Error404")
                            quit()
                    elif response=="n":
                        quit()
        elif int(guess) < Level1Ans:
                print("Ur bad lol. The number is too small.")
                tries = tries+1
                if tries>=3:
                    print("oof! You ran out of tries, the number was:", Level1Ans)
                    response= input("Do you want to play again (Y for yes, N for no)")
                    if response=="y":
                     os.system('cls')
                     menu()
                     tries=0
                     choice =int(input("level choice:"))
                    Level1Ans = random.randint(1,10)
                    if int(choice)>3:
                        print("That's not a level.Error404")
                        quit()
                    elif response=="n":
                     quit()
        elif int(guess) == Level1Ans:
                print("Ur a Mega Gamer")
                response= input("Do you want to play again (Y for yes, N for no)")
                if response=="y":
                    os.system('cls')
                    menu()
                    tries=0
                    choice =int(input("level choice:"))
                    Level1Ans = random.randint(1,10)
                    if int(choice)>3:
                        print("That's not a level.Error404")
                        quit()
                elif response=="n":
                    quit()

# if tries==3:
#             print("oof! You ran out of tries, the number was:", Level1Ans)
#             response= input("Do you want to play again (Y for yes, N for no)")
#             if response=="y":
#                     os.system('cls')
#                     menu()
#                     choice =int(input("level choice:"))
#                     Level1Ans = random.randint(1,10)
#                     if int(choice)>3:
#                         print("U dumb lol. That's not a level")
#                         quit()
#             elif response=="n":
#                     quit()




               
while  int(difficulty) == 2:
        guess = input("What is your guess:")
        if int(guess) != Level2Ans and Level2Ans%divisor==0:
            print("Ur bad lol. The number is divisible by" , divisor)
            tries = tries + 1
            if tries>=4:
                print("oof! You ran out of tries, the number was:", Level1Ans)
                response= input("Do you want to play again (Y for yes, N for no)")
                if response=="y":
                    os.system('cls')
                    menu()
                    tries=0
                    choice =int(input("level choice:"))
                    Level2Ans = random.randint(1,50)
                    divisor=random.randint(1,10)
                    if int(choice)>3:
                        print("That's not a level.Error404")
                        quit()
                elif response=="n":
                    quit()
        elif int(guess) != Level2Ans and Level2Ans%divisor!=0:
            print("Ur bad lol. The number is not divisible by" , divisor)
            tries = tries + 1
            if tries>=4:
                print("oof! You ran out of tries, the number was:", Level1Ans)
                response= input("Do you want to play again (Y for yes, N for no)")
                if response=="y":
                    os.system('cls')
                    menu()
                    choice =int(input("level choice:"))
                    Level1Ans = random.randint(1,50)
                    divisor=random.randint(1,10)
                    if int(choice)>3:
                        print("That's not a level.Error404")
                        quit()
                elif response=="n":
                    quit()
        if str.isnumeric(guess) and int(guess) ==Level2Ans:
            print("Ur a Mega Gamer")
            response= input("Do you want to play again (Y for yes, N for no)")
            if response=="y":
                    os.system('cls')
                    menu()
                    tries = 0
                    choice =int(input("level choice:"))
                    Level2Ans = random.randint(1,50)
                    divisor= random.randint(1,10)
                    if int(choice)>3:
                        print("That's not a level.Error404")
                        quit()
            elif response=="n":
                        quit()

while int(difficulty) == 3:
        guess = input("What is your guess:")
        if int(guess) > Level3Ans:
            print("Ur bad lol. The number is too small")
            tries=tries+1
            if tries>=5:
                print("oof! You ran out of tries, the number was:", Level1Ans)
                response= input("Do you want to play again (Y for yes, N for no)")
                if response=="y":
                    os.system('cls')
                    menu()
                    tries=0
                    choice =int(input("level choice:"))
                    Level1Ans = random.randint(1,100)
                    if int(choice)>3:
                        print("That's not a level. Error404")
                        quit()
                elif response=="n":
                    quit()
        if int(guess) < Level3Ans:
            print("Ur bad lol. The number is too big.")
            tries=tries+1
            if tries>=5:
                print("oof! You ran out of tries, the number was:", Level1Ans)
                response= input("Do you want to play again (Y for yes, N for no)")
                if response=="y":
                    os.system('cls')
                    menu()
                    tries=0
                    choice =int(input("level choice:"))
                    Level3Ans = random.randint(1,100)
                    if int(choice)>3:
                        print("That's not a level. Error404")
                        quit()
                elif response=="n":
                    quit()
        if str.isnumeric(guess) and int(guess) ==Level3Ans:
            print("Ur actually a mega gamer")
            response= input("Do you want to play again (Y for yes, N for no)")
            if response=="y":
                    os.system('cls')
                    menu()
                    tries=0
                    choice=int(input("level choice:"))
                    Level3Ans = random.randint(1,100)
                    if int(difficulty)>3:
                        print("That's not a level.Error404")
                        quit()
            elif response=="n":
                    quit()

if int(difficulty)>3:
    print("U dumb lol. That's not a level")
    quit()