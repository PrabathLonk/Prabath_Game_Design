#Prabath Girish
#2/16/22

import os,random
os.system('cls')

numbercards=[]
for i in range (2,11):
    numbercards.append(i)
    numbercards[i-2]=str(numbercards[1-2])
print(numbercards)
suits=['s','c','h','d']
royals=['j','q','k',"JK"]