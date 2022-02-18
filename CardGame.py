#Prabath Girish
#2/16/22

import os,random
os.system('cls')

# Create the "i" function to form the list
numbercards=[]
for i in range (2,11):
    numbercards.append(i)
    numbercards[i-2]=str(numbercards[1-2])
numbercards.insert(0,'A')
suits=['s','h','d','c']
royals=['J','Q',"K"]
# We have to make a final deck that compiles all the cards in a deck
fulldeck=[]
# define a function to create this deck
def deck(cardnumber):
    global suits
    global fulldeck
    global fulldeck
    for i in range(len(suits)):
        suits[i]=str(numbercards[cardnumber])+str(suits[i])
    fulldeck.extend(suits)
#Exapnding the full deck to include all the suits and royals
for l in range(0,8):
    deck(l)
fulldeck.extend(royals) #Extend to include the royals
print("The deck is:\n"+str(fulldeck))