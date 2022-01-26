
# Prabath Girish
# Game Design Class (Guessing Game Contd.)
# 1/25/21

# we are going to learn about input() function,type casting, branching, and looping

# declare the variable
#print("Enter a number from 1-10:")
#userInfo= int(input()) #input returns string, we must type cast bc we need a number
#print("The number is %.2f " %(userInfo/3)) #we use .2 float to get the thingy


import os, random
os.system('cls')

#guess = int(input("Please give me a number"))
 
def menu():
    print(" ==========================================================================")
    print(" |                                                                        |")
    print(" |       Get Ready To Play: THE NUMBER GUESSING GAME!                     |")
    print(" |                     level 1(3 tries): 1-10                             |")
    print(" |                     level 2(4 tries): 1-30                             |")
    print(" |                     level 3(5 tries): 1-50                             |")
    print(" ==========================================================================")
    
menu()

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
        print("U dumb lol. That's not a level")
        quit()
        

Level1Ans = random.randint(1,10)
Level2Ans = random.randint(1,50)
Level3Ans = random.randint(1,100)



while int(difficulty) == 1:
        guess = input("What is your guess:")
        tries = 0
        if int(guess) > Level1Ans:
                print("Ur bad lol. The number is too big")
        elif int(guess) < Level1Ans:
                print("Ur bad lol. The number is too small.")
        elif int(guess) == Level1Ans:
                print("Ur a Mega Gamer")
                response= input("Do you want to play again (Y for yes, N for no)")
                if response=="y":
                    os.system('cls')
                    menu()
                    choice =int(input("level choice:"))
                    Level1Ans = random.randint(1,10)
                    if int(choice)>3:
                        print("U dumb lol. That's not a level")
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
        tries = 0
        if int(guess) > Level2Ans:
            print("Ur bad lol. The number is too big")
            tries = tries + 1
        if int(guess) < Level2Ans:
            print("Ur bad lol. The number is too small.")
            tries = tries + 1
        if str.isnumeric(guess) and int(guess) ==Level2Ans:
            print("Ur a Mega Gamer")
            response= input("Do you want to play again (Y for yes, N for no)")
            if response=="y":
                    os.system('cls')
                    menu()
                    choice =int(input("level choice:"))
                    Level2Ans = random.randint(1,50)
                    if int(choice)>3:
                        print("U dumb lol. That's not a level")
                        quit()
                    elif response=="n":
                        quit()

while int(difficulty) == 3:
        guess = input("What is your guess:")
        if int(guess) > Level3Ans:
            print("Ur bad lol. The number is too big")
        if int(guess) < Level3Ans:
            print("Ur bad lol. The number is too small.")
        if str.isnumeric(guess) and int(choice) ==Level3Ans:
            print("Ur actually a mega gamer")
            response= input("Do you want to play again (Y for yes, N for no)")
            if response=="y":
                    os.system('cls')
                    menu()
                    choice=int(input("level choice:"))
                    Level3Ans = random.randint(1,100)
                    if int(difficulty)>3:
                        print("U dumb lol. That's not a level")
                        quit()
            elif response=="n":
                    quit()

if int(difficulty)>3:
    print("U dumb lol. That's not a level")
    quit()