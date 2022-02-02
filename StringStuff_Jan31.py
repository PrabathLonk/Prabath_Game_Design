# Prabath Girish
# 1/31/2022
#  today we're going to learn about Strings with an array of characters

from gettext import find
import os,random
os.system('cls')

# # This is a string, a string is an array of characters (below)
# # Each character in this string has an adress called the index, which represents the cell, allowing for the printing of each character individually
# # When counting the indexes you start at zero (P in our scenario), and counts up fro m there to the right
MyName="Prabath Girish"
# # Here we are creating an array with each letter having it own cell with my first name starting at zero counting up by each space
# # If we print this we can select a number and it will print the specifc letter we chose (must use square brackets to show cell #)
# # The first letter starts at zero
# print(MyName[0])

# # IF we use 3 quotation marks before our print variable, it prints exactly what we wrote with our formatting, removing the need for us to type cast the formatting
# # MyParagraph= """ I like to go to school and talk to my friends because
# #                                     they
# # are very nice  """

mystatement1="HEEBEEJEEBEE"

# print(mystatement1)

# # you can also print additional statements based on what is in your statement
# if 'nice' in mystatement1:
#     print("I agree")

# # Find() is a system/function that lets your computer find a specific index or character in your string. It allows you to find the cell #/index of the character you asked to find
# #
# INDEX=MyName.find("G")
# print(INDEX)

# # By using 'len' we can determine the length of the word in our string
# wordLength= len(MyName)
# print (wordLength)

# # print (MyName[14])
# #But if we print the statement above the computer fails because it starts at zero, therefore the length of the word is actually one less than given
# # So to print the last letter we have to do this:
# print(MyName[13])

# # Now we are going to talk about 'for' loops, which is different then the 'while' loops we used earlier
# # This type of loop is used when we want to only loop the program for a certain number of times and by doing so we can run the program a certain numer of times
# # In the loop below has "i" as your looping variable, it will keep on looping the indez until you hit 13(which is the range given being the word length minus 1)
# # We have to make sure our looping varibales are all the same (EX: the 3 "i"s in the loop below), which can allow us to print all the points where we can find that letter 
# # Then the space and DONE at the bottom are just kinda there for asthetic purposes
# for i in range(wordLength-1):
#     if "r" in MyName[i]:
#         print(i, end=", ")
# print(" ")
# print("DONE")
# # When making our upcoming word game, you can make it case sensitive or not
# # These statements were moved below but commoned here for notes
# # lower is a function that converts it all to lower case, which can allow us to answer guesses in lower case. Upper is a function that does the opposite that allows us to answer in uppercase
mystatement=mystatement1.lower()
# print(mystatement)
# # letter= input("please give a nice letter user:")
# # print("Thank you the letter is:", letter)

# # But we can print out words and numbers so we need to define our value error before taking in our input
# # .isalpha() is a function that only allows for alphabetical inputs allowing for you to resist
# # The not is to not allow things that are not alphabets
# check=True
# while check:
#     letter= input("please give a nice letter user:")
#     if len(letter)>1 or not letter.isalpha():
#         print("bad boi")
#     else:
#         check=False

# print("Thank you the letter is:", letter)
# print("Ready for playing")

# The elem makes a space between every character in the array being in the my statement: heebeejeebee
for elem in mystatement:
    print(elem, end= ", ")

#This function selects a random letter from MyName 
guess=random.choice(MyName)
print(guess)

# below we are making a list of word for guessing, we use square brackets for guessing
# words= ["radio" , "adeiu" , "suite" ,"chain"]
# # Now we make it select a random choice from our words
# word= random.choice(words)
# print (word)
# check=True
# while check:
#     letter= input("please give a nice letter user:")
#     if len(letter)>1 or not letter.isalpha():
#         print("bad boi")
#     else:
#         check=False

# Now we can do our game and allow for the user to select a letter 

words= ["radio" , "adeiu" , "suite" ,"chain"]
# Now we make it select a random choice from our words and allow the user to guess letter
word= random.choice(words)
print (word)
check=True
while check:
    letter= input("please give a nice letter user:")
    if len(letter)>1 or not letter.isalpha():
        print("bad boi")
    else:
        check=False

while check==False:
    if letter in word:
        print("Yay you guessed a letter in the word")
        quit()
    else:
        print("that letter is not in the word")