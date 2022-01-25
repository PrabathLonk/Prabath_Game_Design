import random, os

os.system('cls')

 

print('###########W############################')
print('#          Guess A Number Menu         #')
print('#                                      #')
print('#         1.  Choices 1-10             #')
print('#         2.  Choices 1-50             #')
print('#         3.  Choices 1-100            #')
print('#                                      #')
print('########################################')

choice=int(input("What level do you want (Type the number of the level): "))
if choice == 1:
    myNumber= random.randint(1,10)
elif choice == 2:
    myNumber= random.randint(1,50)
elif choice == 3:
  myNumber= random.randint(1,100)
print(choice)
GameOn=True
while(GameOn):
    userGuess=int(input("What is your guess: "))
    if myNumber ==userGuess:
        print("You guessed it!")
        quit()
    else:
        print("Try again... ", myNumber)
# print("The number to guess was " + str(myNumber))