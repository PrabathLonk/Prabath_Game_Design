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
pygame.display.set_caption("Circle Eat Square Menu")

Check=True
while Check==True:
    # Create fonts
    TITLE_FONT=pygame.font.SysFont('comicsans',80) #<-- First pice of text within parenthsis is the name of the font, and the number is the height of the letters
    MENU_FONT=pygame.font.SysFont('comicsans',40)
    INSTRUCTION_FONT=pygame.font.SysFont('comicsans',25)
    #Create the text we want to write
    text=MENU_FONT.render('Circle Eat Square Instructions',1,(0,255,0)) #<-- Goes in order of actual written text, thickness, and color of the text
    instructions=INSTRUCTION_FONT.render("The goal of this game is for the player controlling the",1,(0,0,255))
    instructions2=INSTRUCTION_FONT.render("circle to catch the player controlling the square.",1,(0,0,255))
    instructions3=INSTRUCTION_FONT.render("The square controlling player uses WASD to control the",1,(0,0,255))
    instructions4=INSTRUCTION_FONT.render("square, the circle is controlled by Player 2 with the arrow",1,(0,0,255))
    instructions4=INSTRUCTION_FONT.render("keys. The square can hit space to get a vertical jump boost.",1,(0,0,255))
    instructions5=INSTRUCTION_FONT.render("Once a circle reaches a certain size, that player wins",1,(0,0,255))
    # Put our text on screen after coloring the screen
    window.fill((255,255,255))
    #Blit is what shows and writes our text
    window.blit(text,(50,50))
    window.blit(instructions,(20,200))
    window.blit(instructions2,(20,230))
    window.blit(instructions3,(20,260))
    window.blit(instructions4,(20,290))
    window.blit(instructions5,(20,320))
    #Update our display 
    pygame.display.update()
    # Set a delay for us to see
    pygame.time.delay(10000)
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            Check=False


# HW:FIND FONTS THAT I LIKE TO USE AND EXPIRIMENT WITH OUR MENU