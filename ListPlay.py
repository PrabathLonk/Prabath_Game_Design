#Prabath Girish
#2/16/22
#Here we are going to talk about lists

import os,random
os.system('cls')
# First let's create a basic list:
fruits=["bananas", "grapes", "watermelon", 'blueberries', 'apples', "blackberries",
    "papaya", 'oranges', 'tomatoes', 'mangos', 'kiwis','strawberries', 'monke' ]
# Let's check the size of our array and print that value

size=len(fruits)

print(size)


fruits.append("rambutan") #This adds the rambutan to our list of fruits

# for i in range(13): # 13 is not included so that's why it isn't printing rambutan when we put 13
#     print(fruits[i])

for i in range(14): 
    print(fruits[i])

# the "i" allowed us to print the fruits list, and if we want to print the fruits[size] we have to make sure to do [size-1] because 13 is not included
# You can also use the list to find the number of a specifc term in your list. Below we find the number of bananas in our list
print(fruits.count("bananas"))

# WE can also append a list by adding another one to it
List2=[1,2,3]
fruits.append(List2)
print("append:", fruits)
fruits.pop(-1)
fruits.extend(List2) # This extends our list by merging in the new term as indicated by the brackes
print ("extend:", fruits)
size=len(fruits)
print(size)
# The size increases due to the new terms added