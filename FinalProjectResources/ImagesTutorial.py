#Prabath Girish
#4/9/22
# Tutorial to create moving images
#Finish Thwomp Machanic
import pygame, os, random
pygame.init()
os.system('cls')
win = pygame.display.set_mode((500,480))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('FinalProjectResources\Images\R1.png'), pygame.image.load('FinalProjectResources\Images\R2.png'), pygame.image.load('FinalProjectResources\Images\R3.png'), pygame.image.load('FinalProjectResources\Images\R4.png'), pygame.image.load('FinalProjectResources\Images\R5.png'), pygame.image.load('FinalProjectResources\Images\R6.png'), pygame.image.load('FinalProjectResources\Images\R7.png'), pygame.image.load('FinalProjectResources\Images\R8.png'), pygame.image.load('FinalProjectResources\Images\R9.png')]
walkLeft = [pygame.image.load('FinalProjectResources\Images\L1.png'), pygame.image.load('FinalProjectResources\Images\L2.png'), pygame.image.load('FinalProjectResources\Images\L3.png'), pygame.image.load('FinalProjectResources\Images\L4.png'), pygame.image.load('FinalProjectResources\Images\L5.png'), pygame.image.load('FinalProjectResources\Images\L6.png'), pygame.image.load('FinalProjectResources\Images\L7.png'), pygame.image.load('FinalProjectResources\Images\L8.png'), pygame.image.load('FinalProjectResources\Images\L9.png')]
bg = pygame.image.load('FinalProjectResources\Images\gb_ImageTutorial.jpg')
bg2=pygame.image.load('FinalProjectResources\Images\Sunset.jpg')
bg3=pygame.image.load('FinalProjectResources\Images\Handshake.jpg')
bg4=pygame.image.load('FinalProjectResources\Images\GrassyBackground.jpg')
bg5=pygame.image.load('FinalProjectResources\Images\Grassland.jpg')
rip=pygame.image.load('FinalProjectResources\Images\dead.png')
RealRIP=pygame.transform.scale(rip,(64,64))
bgList=[bg,bg2,bg3,bg4,bg5]
char = pygame.image.load('FinalProjectResources\Images\standing.png')
thwomp= pygame.image.load('FinalProjectResources\Images\Thwomp.png')
INSTRUCTION_FONT=pygame.font.SysFont('proxmanova',35)
x = 50
y = 400
hitX=50
hitY=400
width = 40
height = 60
hitbox=pygame.Rect(hitX,hitY,width+20,height+10)
ThwompBox=pygame.Rect(250,140,150,160)
vel = 5
MAX=-10

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    pygame.draw.rect(win,(255,255,255),hitbox)
    pygame.draw.rect(win,(255,255,255),ThwompBox)
    win.blit(bg, (0,0)) 
    win.blit(thwomp,(250,140))
    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left:  
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1 
        # if ((x >140 and x < 290) and (y >250 and y <370)):  
        #     # right=False
        #     if y!=400:
        #         y=y+10
        #     print(x+"and"+y)
        #     # left=False
            
 
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0
        
    pygame.display.update() 
    


run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        hitbox.x=x
        left = True
        right = False
        checkCollide= pygame.Rect.colliderect(ThwompBox,hitbox)
        if checkCollide:
            char=RealRIP
            y=400
            hitbox.y=y
            GameOver=INSTRUCTION_FONT.render("YOU DIED. GAME OVER",1,(0,0,255))
            win.blit(GameOver,(0,0))
            # run=False



        pygame.display.update()

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  
        x += vel
        hitbox.x=x
        left = False
        right = True
        checkCollide= pygame.Rect.colliderect(ThwompBox,hitbox)
        if checkCollide:
            char=RealRIP
            y=400
            hitbox.y=y
            GameOver=INSTRUCTION_FONT.render("YOU DIED. GAME OVER",1,(0,0,255))
            win.blit(GameOver,(0,0))
            # run=False



        pygame.display.update()
        
    else: 
        left = False
        right = False
        walkCount = 0
        checkCollide= pygame.Rect.colliderect(ThwompBox,hitbox)
        if checkCollide:
            char=RealRIP
            y=400
            hitbox.y=y
            GameOver=INSTRUCTION_FONT.render("YOU DIED. GAME OVER",1,(0,0,255))
            win.blit(GameOver,(0,0))
            # run=False


    if x== 400:
        bg=random.choice(list(bgList))
        y=400
        x=0
        win.blit(char,(x,y))
        
        
    # if x==390 and y==540:
    #     win.blit(bg2, (0,0)) 
    #     x=0
    #     y=480
    #     win.blit(char, (x, y))
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
            
    else:
        if jumpCount >= MAX:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            hitbox.y=y
            jumpCount -= 1
            if checkCollide:
                y=400
                hitbox.y=y
                # GameOver=INSTRUCTION_FONT.render("YOU DIED. GAME OVER",1,(0,0,255))
                char=RealRIP
                win.blit(GameOver,(0,0))
            # run=False

        else: 
            jumpCount = 10
            isJump = False    


    redrawGameWindow() 
    
    
pygame.quit()