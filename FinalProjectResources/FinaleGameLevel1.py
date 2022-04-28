# Full Code

# The full code should look like the following.

#Prabath Girish
# 4/28/22 

import pygame

pygame.init()

WIDTH=700

HEIGHT=600

win = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Level 1 Game")

 

walkRight = [pygame.image.load('FinalProjectResources\Images\R1.png'), pygame.image.load('FinalProjectResources\Images\R2.png'), pygame.image.load('FinalProjectResources\Images\R3.png'), pygame.image.load('FinalProjectResources\Images\R4.png'), pygame.image.load('FinalProjectResources\Images\R5.png'), pygame.image.load('FinalProjectResources\Images\R6.png'), pygame.image.load('FinalProjectResources\Images\R7.png'), pygame.image.load('FinalProjectResources\Images\R8.png'), pygame.image.load('FinalProjectResources\Images\R9.png')]

walkLeft = [pygame.image.load('FinalProjectResources\Images\L1.png'), pygame.image.load('FinalProjectResources\Images\L2.png'), pygame.image.load('FinalProjectResources\Images\L3.png'), pygame.image.load('FinalProjectResources\Images\L4.png'), pygame.image.load('FinalProjectResources\Images\L5.png'), pygame.image.load('FinalProjectResources\Images\L6.png'), pygame.image.load('FinalProjectResources\Images\L7.png'), pygame.image.load('FinalProjectResources\Images\L8.png'), pygame.image.load('FinalProjectResources\Images\L9.png')]

bg = pygame.image.load('FinalProjectResources\Images\gb_ImageTutorial.jpg')

char = pygame.image.load('FinalProjectResources\Images\standing.png')

 

x = 50

y = 400

width = 40

height = 60

vel = 5

platfrm=pygame.Rect(WIDTH/2-150, HEIGHT/2, WIDTH/5, 10)

clock = pygame.time.Clock()

manRect=pygame.Rect(x, y, 64, 64)

isJump = False

jumpCount = 10

 

left = False

right = False

walkCount = 0

flag=False

def redrawGameWindow(x,yt):

    global walkCount

    global y

    y=yt

    win.blit(bg, (0,0))

    manRect=pygame.Rect(x+10, y+10, 46, 54)

    pygame.draw.rect(win, (255,255,255), platfrm)

    checkCollide = manRect.colliderect(platfrm)

    print(checkCollide)

    if checkCollide:

        flag=True

        y=platfrm.y-64

    manRect=pygame.Rect(x+10, y+10, 46, 54)

    pygame.draw.rect(win, (255,255,255),manRect)

    if walkCount + 1 >= 27:

        walkCount = 0

    if left:  

        win.blit(walkLeft[walkCount//3], (x,y))

        walkCount += 1                          

    elif right:

        win.blit(walkRight[walkCount//3], (x,y))

        walkCount += 1

    else:

        win.blit(char, (x, y))

        walkCount = 0  

    pygame.display.update()

   

run = True

checkCollide=False

while run:

    clock.tick(27)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            run = False

    keys = pygame.key.get_pressed()  

    if keys[pygame.K_LEFT] and x > vel:

        x -= vel

        left = True

        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  

        x += vel

        left = False

        right = True    

    else:

        left = False

        right = False

        walkCount = 0

    if not(isJump):

        if keys[pygame.K_SPACE]:

            isJump = True

            left = False

            right = False

            walkCount = 0

    else:

        if jumpCount >= -10:

            y -= (jumpCount * abs(jumpCount)) * 0.5

            jumpCount -= 1

           

        else:

            jumpCount = 10

            isJump = False

    redrawGameWindow(x,y)

   

pygame.quit()