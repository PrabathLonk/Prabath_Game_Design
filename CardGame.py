#Prabath Girish
#2/16/22
#Previous Draft:
# Create the "i" function to form the list
# numbercards=[]
# for i in range (2,11):
#     numbercards.append(i)
#     numbercards[i-2]=str(numbercards[1-2])
# numbercards.insert(0,'A')
import os,random
os.system('cls')

#Define your deck and the possible suits, while creating a function for the full deck 
suits=['of spades','of hearts','of diamonds','of clubs']
deck=['Ace',2,3,4,5,6,7,8,9,10,"Jack",'Queen','King']
mainDeck=[]
# Create a for function that adds a suit for every number/royal to create the deck of 52
for num in deck:
    for SuitChoice in suits:
        mainDeck.append(str(num)+' '+SuitChoice)

print("MainDeck:\n", mainDeck)
userCard1=random.choice(mainDeck)