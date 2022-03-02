# Prabath Girish
# 3/1/22
#This game will ask the user for three numbers and tell you which one is smallest 
#Import the os
import os
os.system('cls')

#Define our variables and ask the user for our inputs
print("Pick 3 unique numbers and the computer will tell you which one is the greatest")
Number1=int(input("What is your first number choice:"))
Number2=input("What is your second number choice:")
Number3=input("What is your third number choice:")
#Create a function to list the order of the number and do checks for value errors

# check1=True
# while check1==True:
#     try:
#         Number1=int(input("What is your first number choice:"))
#         if :
#             check1=False
#     except ValueError:
#         print("THATS NOT A NUMBER")





def rearranger():
    if int(Number1)<int(Number2) and int(Number1)<int(Number3):
        print("Your smallest value is your first one:", Number1)
        quit()
    elif int(Number2)<int(Number1) and int(Number2)<int(Number3):
        print("Your smallest value is your second one:", Number2)
        quit()
    elif int(Number3)<int(Number1) and int(Number3)<int(Number2):
        print("Your smallest value is your third one:", Number2)
        quit()
    else:
        print("There are some equal numbers in there, try again with some unique numbers")
        quit()


rearranger()