#Prabath Girish
#Learning files
# a) open/create a file
# b) write 'w'
# c) append 'a'
# d) read r
# e) close our file 'close()'


import pygame, os, datetime
os.system('cls')
date=datetime.datetime.now() #This is the function to find the exact date at the current moment from the computer
score=123 # This and name are for example purposes
score2=333
name2='Timmy'
name="Jesse"
print(date.strftime('%m/%d/%Y')) # This is to reorder the date into month, day, year order (which allows us to use this function to rearrange the date to how we like)

#You must convert something to a string to add it to a file
scoreLine=str(score)+' '+name+' '+(date.strftime('%m/%d/%Y')) #This converts the score to a string and combines it with the name and the date
print(scoreLine)
scoreLine2=str(score2)+' '+name2+' '+(date.strftime('%m/%d/%Y')) #This converts the score to a string and combines it with the name and the date
print(scoreLine2)
MyFile=open('FinalCircleEatSquareGame\highscore.txt','a') # BY using the relative path we can open the highscore text file 
MyFile.write(scoreLine) # This writes out score in the file
MyFile.write(scoreLine2)
MyFile.close() # This closes the file once the program is done writing

# If we look at the file we see that the previous text was deletd and replaced by the new text, so be careful when writing into a new file