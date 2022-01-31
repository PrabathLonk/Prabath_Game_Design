# Prabath Girish
# 1/31/2022
#  today we're going to learn about Strings with an array of characters
import os
os.system('cls')

MyName="Prabath Girish"
# Here we are creating an array with each letter having it own cell with my first name starting at zero counting up by each space
# If we print this we can select a umber and it will print the specifc letter we chose (must use square brackets to show cell #)
# The first letter starts at zero
print(MyName[0])

# IF we use 3 quotation marks before our print variable, it prints exactly what we wrote with our formatting, removing the need for us to type cast the formatting
MyParagraph= """ I like to go to school and talk to my friends because
                                    they
are very nice  """

print(MyParagraph)

# you can also print additional statements based on what is in your statement
if 'nice' in MyParagraph:
    print("I agree")