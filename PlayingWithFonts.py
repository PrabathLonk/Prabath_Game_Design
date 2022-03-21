# Prabath Girish
# 3/21/22
#Today we are going to learn how to select and use fonts
# Import pygame and os
import pygame, time
# INitialize pygame
pygame.init()
# Set our window size
window=pygame.display.set_mode((700,700))
#Set our caption:
pygame.display.set_caption("Font Testing")




# Create fonts
TITLE_FONT=pygame.font.SysFont('comicsans',80) #<-- First pice of text within parenthsis is the name of the font, and the number is the height of the letters
MENU_FONT=pygame.font.SysFont('comicsans',40)
INSTRUCTION_FONT=pygame.font.SysFont('comicsans',25)
#Create the text we want to wite
text=TITLE_FONT.render('HELLO GAMERS',1,(0,255,0)) #<-- Goes in order of actual written text, thickness, and color of the text
# Put our text on screen after coloring the screen
window.fill((255,255,255))
#Blit is what shows and writes our text
window.blit(text,(50,50))
#Update our display 
pygame.display.update()
# Set a delay for us to see
pygame.time.delay(5000)

# HW:FIND FONTS THAT I LIKE TO USE AND EXPIRIMENT WITH OUR MENU