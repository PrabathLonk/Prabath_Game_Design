import os
#Prabath_Girish
#Jan14_2022
#Learn to declare variables and print variables and learn about types of data and some operators
# is for commons (computer will ignore)
# To clear my terminal I write os.system (clear)
os.system('cls')

#declaring and assigning values
test1=89
test2=78.5
test3=86
Flag=False


#Learning to display things on the screen: we use the function Print for this
print (type(test1), (type(test2)), (type(Flag)))

# declare the sum and add using the + symbol and then make it a print variable (replace with average later)
# All programming languages are case sensitive
# TO turn a line of code into a common type Ctrl and / at the same time
Sum=test1+test2+test3


#Define the average
average=Sum/3


#We want to see the average of the 3 tests so we should:
# Always use quotations when writing in text 
#We also want to display the test values so we do the following
print ("Test1=", test1)
print ("Test2=", test2)
print ("Test3=", test3)
print ("the average of three tests is", average)



