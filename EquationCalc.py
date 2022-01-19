# Prabath Girish (1/19/22)
# Program to write and solve and equation with 4 test values
# We know +,-,*, and / but we can learn how to find the remainder and exponents
# We also learn to format printing variables and escape character
import os
os.system('cls')

#Declare variables:
v1=10
v2=2
v3=3
v4=5

result=(3*v1-2*((v2)**2)/v3)/v4
# Exponents are represented with **
#Print your variables and the results
# Percent plus letter indicates spaces/formatting changes
# The "end=" function tells the computer how to end the line, resulting the the next line merging with the
# next one, creating a continuos line
print("The variables are:")
print("V1= %5d"% v1)
print("V2= %5d"% v2)
print("V3= %5.8f"% v3)
print("V4= %5d"% v4)
print("Answer = %6.2f"% result)