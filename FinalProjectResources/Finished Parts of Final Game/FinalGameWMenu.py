# Prabath Girish Game Design Final Project
import os, random, time, pygame, math, datetime
os.system('cls')
#initialize pygame
pygame.init()

#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=700
HEIGHT=680
xMs=50
yMs=250
wb=30
hb=30
MAIN=True
INST=False
SETT=False
GAME_ON=False
LEV_I=False
LEV_II=False
LEV_III=False
SCORE=False
screCK=False
#List f messages
MenuList=['Instructions','Settings', 'Play Game','Scoreboard','Exit']
SettingList=['Screen Size(1 for 700x680, 2 for 800x800, 3 for 600x600)','Character(4 for Warrior man, 5 for Jake Paul)','Exit Menu (6)']
sizeList=['700 x 680','800 x 800','600 x 600']
Characters=['Warrior Man', 'Jake Paul']
check=True #for the while loop

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Final Game - Game Design')

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
#Get colors
background= colors.get('white')
randColor=''
cr_color=colors.get('aqua')
sqM_color=colors.get('pink')
BLACK=(0,0,0)
#create fifferent type 
TITLE_FONT=pygame.font.SysFont('georgia',50) #<-- First pice of text within parenthsis is the name of the font, and the number is the height of the letters
MENU_FONT=pygame.font.SysFont('comicsans',40)
INST_FNT=pygame.font.SysFont('proximanova', 30)
#Create square fr menu
# This is to declare our values that we will be using:
# Defines the images for the game and scales them as well as the hitboxes to show:
walkRight = [pygame.image.load('FinalProjectResources\Images\R1.png'), pygame.image.load('FinalProjectResources\Images\R2.png'), pygame.image.load('FinalProjectResources\Images\R3.png'), pygame.image.load('FinalProjectResources\Images\R4.png'), pygame.image.load('FinalProjectResources\Images\R5.png'), pygame.image.load('FinalProjectResources\Images\R6.png'), pygame.image.load('FinalProjectResources\Images\R7.png'), pygame.image.load('FinalProjectResources\Images\R8.png'), pygame.image.load('FinalProjectResources\Images\R9.png')]
walkLeft = [pygame.image.load('FinalProjectResources\Images\L1.png'), pygame.image.load('FinalProjectResources\Images\L2.png'), pygame.image.load('FinalProjectResources\Images\L3.png'), pygame.image.load('FinalProjectResources\Images\L4.png'), pygame.image.load('FinalProjectResources\Images\L5.png'), pygame.image.load('FinalProjectResources\Images\L6.png'), pygame.image.load('FinalProjectResources\Images\L7.png'), pygame.image.load('FinalProjectResources\Images\L8.png'), pygame.image.load('FinalProjectResources\Images\L9.png')]
JakePaul1=pygame.image.load('FinalProjectResources\Images\JakePaulLowEffort.png')
JakePaul=pygame.transform.scale(JakePaul1,(64,64))
bg = pygame.image.load('FinalProjectResources\Images\SkyBackground_Rayquaza.jpg')
bg2= pygame.image.load('FinalProjectResources\Images\SpongebobBackground_SansFightBackground.jpg')
SkyBG=pygame.transform.scale(bg,(WIDTH,HEIGHT))
SansBG=pygame.transform.scale(bg2,(WIDTH,HEIGHT))
char = pygame.image.load('FinalProjectResources\Images\standing.png')
Ray1=pygame.image.load('FinalProjectResources\Images\RayquazaIdle.png')
RayIdle=pygame.transform.scale(Ray1,(WIDTH/4,HEIGHT-175))
RayHitbox=pygame.Rect(WIDTH-WIDTH/4,105,WIDTH/4,HEIGHT-175)
Sans1=pygame.image.load('FinalProjectResources\Images\SansStartIdle.png')
SansIdle=pygame.transform.scale(Sans1,(WIDTH/4,HEIGHT-175))
SansHitbox=pygame.Rect(WIDTH-WIDTH/4,105,WIDTH/4,HEIGHT-175)
manRect=pygame.Rect(210, 400, 64, 64)
# Places the bottom platform to stand on:
BottomPlat= pygame.Rect(0,HEIGHT-20,WIDTH,10)
BottomPlat2=pygame.Rect(0,HEIGHT-20,WIDTH,10)
# Creates a tick count for time functions
clock = pygame.time.Clock()
tickStart=pygame.time.get_ticks()
# Just creates a color for the health bar
green=(18,230,3)
# Defines botht the player and enemy health
RayquazaHealth=pygame.Rect(WIDTH/2-100,WIDTH-(WIDTH-50),200,8)
SansHealth=pygame.Rect(WIDTH/2-100,WIDTH-(WIDTH-50),311,8)
Health=10
#Creates two Counts to check health of the boss and allows the boss to counter attack
hitCount=0
revengeCount=0
# Just defines the player's name and the the bonus that the player gets for time
TimeBonus=0
# Spikes image
Spike1=pygame.image.load('FinalProjectResources\Images\Spikes.png')
Spike=pygame.transform.scale(Spike1,(48,28))
# Gets the Player's name for score
Name=input("Type your name:")
# Checks if the Boss is alive
AliveCheck=True
AliveCheck2=False
# Checks the level:
LevelCheck=False
squareM=pygame.Rect(xMs,yMs,wb,hb)
# Defining some mouse stuff
mouse_pos=pygame.mouse.get_pos()
xm= mouse_pos[0]
ym= mouse_pos[1]
class player(object):
    global Health
    def __init__(self,x,y,width,height):
        # Defines the dimensions of the character
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # Defines the movement and jump checks
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        # Defines the health for the hit function (replaces Health variable)
        self.Health=5
        #Creates the hitbox
        self.hitbox = (self.x+10, self.y+5, 25, 25)

    def draw(self, screen):
        #This function draws the character
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        #This draws the hitbox of the character
        self.hitbox = (self.x+10, self.y+10, 44, 50)
        # pygame.draw.rect(screen, (255,0,0), self.hitbox,2)
        # This animates the character
        if not(self.standing):
            if self.left:
                screen.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                screen.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                screen.blit(walkRight[0], (self.x, self.y))
            else:
                screen.blit(walkLeft[0], (self.x, self.y))
    def hit(self):
        print("oof")
        self.Health-=1
        print("HEALTH:",self.Health)
        if self.Health<=0:
            print("You Died")
            quit()
                

# This class defines the projectile class and its attributes
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        # Defines position
        self.x = x
        self.y = y
        #Defines radius
        self.radius = radius
        # Define color
        self.color = color
        # Defines the direction of the bullet
        self.facing = facing
        self.vel = 8 * facing
        # Defines the projectile hitbox
        self.hitbox=(self.x-self.radius,self.y-self.radius,2*self.radius,2*self.radius)

    def draw(self,screen):
        # Draws the bullet
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.radius)
        self.hitbox=(self.x-self.radius,self.y-self.radius,2*self.radius,2*self.radius)
        # pygame.draw.rect(screen, (255,0,0), self.hitbox,2)
# This creates the class for the boss
class enemy(object):
    # walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    # walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
    #This defines the character's dimension and hitbox, like the character
    def __init__(self, x, y, width, height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end=end
        self.hitbox = (self.x, self.y,WIDTH/4,HEIGHT-175)
        print((self.hitbox[0]))
        # self.path = [x, end]
        # self.walkCount = 0
        # self.vel = 3
    #This function draws the enemy
    def draw(self, screen):
        # self.move()
        screen.blit(RayIdle,(RayHitbox.x,RayHitbox.y))
        self.hitbox = (self.x, self.y, WIDTH/4, HEIGHT-175) 
        # pygame.draw.rect(screen, (255,0,0), self.hitbox,2)
    def hit(self):  # This will display when the enemy is hit and indicate they have taken damage via the health
        RayquazaHealth.width-=5
# This function draws everything we need on the screendow and updates it as the game runs
def redrawGameWindow():
    global AliveCheck
    manRect=pygame.Rect(man.x+10, man.y+10, 46, 54)
    pygame.draw.rect(screen, (255,255,255),manRect)
    pygame.draw.rect(screen, (255,255,255),RayHitbox)
    # Draws the spikes only in he second level
    if RayIdle==SansIdle and AliveCheck:
        pygame.draw.rect(screen,(255,255,255),SpikeHitbox)
        pygame.draw.rect(screen,(255,255,255),SpikeHitbox2)
    screen.blit(SkyBG, (0,0))
    # This only draws the boss if his health is higher than 0
    if AliveCheck:
        Rayquaza.draw(screen)
    if RayIdle==SansIdle and AliveCheck:
        spike.draw(screen)
        spike2.draw(screen)
    # Draws the boss healthbar, player, and bottom platform
    man.draw(screen)
    pygame.draw.rect(screen, (255,255,255),BottomPlat)
    pygame.draw.rect(screen,green,RayquazaHealth)
    # Draws the bullets when needed
    for bullet in bullets:
        bullet.draw(screen)
    for fireBall in fireBalls:
        fireBall.draw(screen)
        
    
    pygame.display.update()

# This defines the spikes on the ground in level 2:
class spikes(object):
    def __init__(self, x, y, width, height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end=end
        self.hitbox = (self.x, self.y,self.width,self.height)
        print((self.hitbox[0]))
    def draw(self, screen):
        screen.blit(Spike,(self.x,self.y))
#mainloop
# Define the player, boss, and their respective projectiles, as well as the 2 sets of spikes for the 2nd level
man = player(0, BottomPlat.y-64, 64,64)
Rayquaza=enemy(WIDTH-WIDTH/4,100,WIDTH/4,HEIGHT-175,0)
Sans=enemy(WIDTH-WIDTH/4,100,WIDTH/4,HEIGHT-175,0)
spike=spikes(WIDTH/4,BottomPlat.y-28,25,28,0)
spike2=spikes((3*WIDTH/4),BottomPlat.y-28,25,28,0)
SpikeHitbox=pygame.Rect(spike.x,spike.y,spike.width,spike.height)
SpikeHitbox2=pygame.Rect(spike2.x,spike2.y,spike2.width,spike2.height)
bullets = []
fireBalls=[]
GastBlasts=[]
#Create Title
def bak():
    global MAIN
    global INST
    global SETT
    global LEV_I
    global LEV_II
    global LEV_III
    global SCORE
    MAIN=True
    INST=False
    SETT=False
    LEV_I=False
    LEV_II=False
    LEV_III=False
    SCORE=False
def ScoreB():
    global N
    global temp
    global SCORE
    MyFile=open('FinalProjectResources\Finished Parts of Final Game\FinalGameScores.txt', 'r')
    yi=150
    stuff=MyFile.readlines()
    MyFile.close()
    stuff.sort()
    N=len(stuff)-1
    temp=[]
    for i in range(N, -1, -1):
        
        # temp[j]=stuff[i]
        # j+=1
        textSCORE=INST_FNT.render(stuff[i],1,'black')
        screen.blit(textSCORE,(40,yi))
        # pygame.display.update()
        # pygame.time.delay(50)
        yi+=50
    if ((mouse_pos[0] >200 and mouse_pos[0] <540) and (mouse_pos[1] >500 and mouse_pos[1] <540)):
                global MAIN
                screen.fill(background)
                SCORE=False
                MAIN=True
                TitleMenu("MENU")
                MainMenu(MenuList)
def TitleMenu(Message):
    text=TITLE_FONT.render(Message, 1, (255,0,0))
    screen.fill((255,255,255))
    #get the width  the text 
    #x value = WIDTH/2 - wText/2
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))
#This is a function uses a parameter
def MainMenu(Mlist):
    txty=243
    squareM.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(51,131,51))
        screen.blit(text,(90,txty))
        pygame.draw.rect(screen,sqM_color, squareM )
        squareM.y +=50
        txty+=50
    pygame.display.update()
    # pygame.time.delay(10)
def SettMenu(Mlist):
    txty=320
    squareM.y=315
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(51,131,51))
        screen.blit(text,(90,txty))
        pygame.draw.rect(screen,sqM_color, squareM )
        squareM.y +=50
        txty+=50
    pygame.display.update()
    # pygame.time.delay(10)
def changeColor():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor)==background:
            print(randColor)
            print(background)
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
def instr():
    global text
    # print("in instr")
    text=TITLE_FONT.render('Boss Battle Game Instructions',1,(0,255,0)) #<-- Goes in order of actual written text, thickness, and color of the text
    instructions=INST_FNT.render("You, the champion warrior of the land, are tasked with purifying",1,(0,0,255))
    instructions2=INST_FNT.render("the majestic beasts of the land by breaking the Dark Diamond that",1,(0,0,255))
    instructions3=INST_FNT.render("have taken them over. Move left or right with the arrow keys",1,(0,0,255))
    instructions4=INST_FNT.render("and use the up arrow to jump. Use the space bar to shoot",1,(0,0,255))
    instructions4=INST_FNT.render("magical bullets that damage the opponent. Find their weak spot and",1,(0,0,255))
    instructions5=INST_FNT.render("strike! Keep an eye out for the fireballs and spikes!",1,(0,0,255))
    instructions6=INST_FNT.render("You will have 5 Health. Good luck warrior.",1,(0,0,255))
    BackButton=MENU_FONT.render("BACK",1,(0,0,0))
    screen.blit(instructions,(20,200))
    screen.blit(instructions2,(20,230))
    screen.blit(instructions3,(20,260))
    screen.blit(instructions4,(15,290))
    screen.blit(instructions5,(20,320))
    screen.blit(instructions6,(20,350))
    screen.blit(BackButton,(200,500))


    # print(stuff)
    # for line in stuff:
    #     print(line)
    #     text=INST_FNT.render(line, 1, BLACK)
    #     screen.blit(text, (40,yi))
    #     pygame.display.update()
    #     pygame.time.delay(50)
    #     yi+=50
    #     myFile.close()
def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine=str(score)+"\t"+Name+"\t"+date.strftime('%m/%d/%Y'+'\n')
 
    #open a file and write in it 
    # when y write it erases the prev 
    myFile=open('FinalProjectResources\FinalCircleEatSquareGame\highscore.txt','a') 
    myFile.write(scoreLine)
    myFile.close()
def scoreBoard():
    global stuff
    myFile=open('FinalProjectResources\FinalCircleEatSquareGame\highscore.txt', 'r')
    yi=150
    stuff= myFile.readlines()
    myFile.close()
    stuff.sort()
    N=len(stuff)-1
    temp=[]
    j=0
    for i in range(N, -1, -1):
        print(i,stuff[i])
        # temp[j]=stuff[i]
        #     j +=1
        # print(temp)
        # for i in range(N):
        #     text=INST_FNT.render(temp[i], 1, BLACK)
        #     screen.blit(text, (40,yi))
        #     pygame.display.update()
        #     pygame.time.delay(50)
        #     yi+=50
    
def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine='\n'+str(score)+"\t"+Name+"\t"+date.strftime('%m/%d/%Y'+'\n')
 
    #open a file and write in it 
    # when y write it erases the prev 
    myFile=open('FinalProjectResources\FinalCircleEatSquareGame\highscore.txt','a') 
    myFile.write(scoreLine)
    myFile.close()
def changeScreenSize(xZ,yZ):
    global HEIGHT, WIDTH, screen, set_first, c_first,SETT
    WIDTH=xZ
    HEIGHT=yZ
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    set_first=False
    c_first=True
    SETT=True
# def changeScreen(xm,ym):
#     global HEIGHT, WIDTH, screen
#     if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
#         HEIGHT=1000
#         WIDTH=1000

#     if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <330)):
#         HEIGHT=800
#         WIDTH=800
        
#     if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <380)):
#         HEIGHT=600
#         WIDTH=600
#     screen=pygame.display.set_mode((WIDTH,HEIGHT))
# def SpriteChange(mouse_pos[0],mouse_pos[1]):
#     global walkLeft, walkRight
#     if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
#         walkRight = [pygame.image.load('FinalProjectResources\Images\R1.png'), pygame.image.load('FinalProjectResources\Images\R2.png'), pygame.image.load('FinalProjectResources\Images\R3.png'), pygame.image.load('FinalProjectResources\Images\R4.png'), pygame.image.load('FinalProjectResources\Images\R5.png'), pygame.image.load('FinalProjectResources\Images\R6.png'), pygame.image.load('FinalProjectResources\Images\R7.png'), pygame.image.load('FinalProjectResources\Images\R8.png'), pygame.image.load('FinalProjectResources\Images\R9.png')]
#         walkLeft = [pygame.image.load('FinalProjectResources\Images\L1.png'), pygame.image.load('FinalProjectResources\Images\L2.png'), pygame.image.load('FinalProjectResources\Images\L3.png'), pygame.image.load('FinalProjectResources\Images\L4.png'), pygame.image.load('FinalProjectResources\Images\L5.png'), pygame.image.load('FinalProjectResources\Images\L6.png'), pygame.image.load('FinalProjectResources\Images\L7.png'), pygame.image.load('FinalProjectResources\Images\L8.png'), pygame.image.load('FinalProjectResources\Images\L9.png')]

#     if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <330)):
#         walkRight=[JAKEPAULREAL]
#         walkLeft=[JAKEPAULREAL]
        

def playGame():
    global LEV_I
    global MENU
    global AliveCheck
    global RayIdle
    global SansIdle
    # Defines the images for the game and scales them as well as the hitboxes to show:
    walkRight = [pygame.image.load('FinalProjectResources\Images\R1.png'), pygame.image.load('FinalProjectResources\Images\R2.png'), pygame.image.load('FinalProjectResources\Images\R3.png'), pygame.image.load('FinalProjectResources\Images\R4.png'), pygame.image.load('FinalProjectResources\Images\R5.png'), pygame.image.load('FinalProjectResources\Images\R6.png'), pygame.image.load('FinalProjectResources\Images\R7.png'), pygame.image.load('FinalProjectResources\Images\R8.png'), pygame.image.load('FinalProjectResources\Images\R9.png')]
    walkLeft = [pygame.image.load('FinalProjectResources\Images\L1.png'), pygame.image.load('FinalProjectResources\Images\L2.png'), pygame.image.load('FinalProjectResources\Images\L3.png'), pygame.image.load('FinalProjectResources\Images\L4.png'), pygame.image.load('FinalProjectResources\Images\L5.png'), pygame.image.load('FinalProjectResources\Images\L6.png'), pygame.image.load('FinalProjectResources\Images\L7.png'), pygame.image.load('FinalProjectResources\Images\L8.png'), pygame.image.load('FinalProjectResources\Images\L9.png')]
    JakePaul1=pygame.image.load('FinalProjectResources\Images\JakePaulLowEffort.png')
    JakePaul=pygame.transform.scale(JakePaul1,(64,64))
    bg = pygame.image.load('FinalProjectResources\Images\SkyBackground_Rayquaza.jpg')
    bg2= pygame.image.load('FinalProjectResources\Images\SpongebobBackground_SansFightBackground.jpg')
    SkyBG=pygame.transform.scale(bg,(WIDTH,HEIGHT))
    SansBG=pygame.transform.scale(bg2,(WIDTH,HEIGHT))
    char = pygame.image.load('FinalProjectResources\Images\standing.png')
    Ray1=pygame.image.load('FinalProjectResources\Images\RayquazaIdle.png')
    RayIdle=pygame.transform.scale(Ray1,(WIDTH/4,HEIGHT-175))
    RayHitbox=pygame.Rect(WIDTH-WIDTH/4,105,WIDTH/4,HEIGHT-175)
    Sans1=pygame.image.load('FinalProjectResources\Images\SansStartIdle.png')
    SansIdle=pygame.transform.scale(Sans1,(WIDTH/4,HEIGHT-175))
    SansHitbox=pygame.Rect(WIDTH-WIDTH/4,105,WIDTH/4,HEIGHT-175)
    manRect=pygame.Rect(210, 400, 64, 64)
    # Places the bottom platform to stand on:
    BottomPlat= pygame.Rect(0,HEIGHT-20,WIDTH,10)
    # Creates a tick count for time functions
    clock = pygame.time.Clock()
    tickStart=pygame.time.get_ticks()
    # Just creates a color for the health bar
    green=(18,230,3)
    # Defines botht the player and enemy health
    RayquazaHealth=pygame.Rect(WIDTH/2-100,WIDTH-(WIDTH-50),200,8)
    SansHealth=pygame.Rect(WIDTH/2-100,WIDTH-(WIDTH-50),311,8)
    Health=10
    #Creates two Counts to check health of the boss and allows the boss to counter attack
    hitCount=0
    revengeCount=0
    # Just defines the player's name and the the bonus that the player gets for time
    TimeBonus=0
    # Spikes image
    Spike1=pygame.image.load('FinalProjectResources\Images\Spikes.png')
    Spike=pygame.transform.scale(Spike1,(48,28))
    # Gets the Player's name for score
    # Name=input("Type your name:")
    # Checks if the Boss is alive
    AliveCheck=True
    AliveCheck2=False
    # Checks the level:
    LevelCheck=False
    global player
    global spikes
    global enemy
    global projectile
    class player(object):
        def __init__(self,x,y,width,height):
            # Defines the dimensions of the character
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            # Defines the movement and jump checks
            self.vel = 5
            self.isJump = False
            self.left = False
            self.right = False
            self.walkCount = 0
            self.jumpCount = 10
            self.standing = True
            # Defines the health for the hit function (replaces Health variable)
            self.Health=5
            #Creates the hitbox
            self.hitbox = (self.x+10, self.y+5, 25, 25)

        def draw(self, screen):
            #This function draws the character
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
            #This draws the hitbox of the character
            self.hitbox = (self.x+10, self.y+10, 44, 50)
            # pygame.draw.rect(screen, (255,0,0), self.hitbox,2)
            # This animates the character
            if not(self.standing):
                if self.left:
                    screen.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1
                elif self.right:
                    screen.blit(walkRight[self.walkCount//3], (self.x,self.y))
                    self.walkCount +=1
            else:
                if self.right:
                    screen.blit(walkRight[0], (self.x, self.y))
                else:
                    screen.blit(walkLeft[0], (self.x, self.y))
        def hit(self):
            print("oof")
            self.Health-=1
            print("HEALTH:",self.Health)
            if self.Health<=0:
                print("You Died")
                quit()
                    

    # This class defines the projectile class and its attributes
    class projectile(object):
        def __init__(self,x,y,radius,color,facing):
            # Defines position
            self.x = x
            self.y = y
            #Defines radius
            self.radius = radius
            # Define color
            self.color = color
            # Defines the direction of the bullet
            self.facing = facing
            self.vel = 8 * facing
            # Defines the projectile hitbox
            self.hitbox=(self.x-self.radius,self.y-self.radius,2*self.radius,2*self.radius)

        def draw(self,screen):
            # Draws the bullet
            pygame.draw.circle(screen, self.color, (self.x,self.y), self.radius)
            self.hitbox=(self.x-self.radius,self.y-self.radius,2*self.radius,2*self.radius)
            # pygame.draw.rect(screen, (255,0,0), self.hitbox,2)
    # This creates the class for the boss
    class enemy(object):
        # walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
        # walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
        #This defines the character's dimension and hitbox, like the character
        def __init__(self, x, y, width, height,end):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.end=end
            self.hitbox = (self.x, self.y,WIDTH/4,HEIGHT-175)
            print((self.hitbox[0]))
            # self.path = [x, end]
            # self.walkCount = 0
            # self.vel = 3
        #This function draws the enemy
        def draw(self, screen):
            # self.move()
            screen.blit(RayIdle,(RayHitbox.x,RayHitbox.y))
            self.hitbox = (self.x, self.y, WIDTH/4, HEIGHT-175) 
            # pygame.draw.rect(screen, (255,0,0), self.hitbox,2)
        def hit(self):  # This will display when the enemy is hit and indicate they have taken damage via the health
            RayquazaHealth.width-=5
    class spikes(object):
        def __init__(self, x, y, width, height,end):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.end=end
            self.hitbox = (self.x, self.y,self.width,self.height)
            print((self.hitbox[0]))
        def draw(self, screen):
            screen.blit(Spike,(self.x,self.y))
    # This function draws everything we need on the screendow and updates it as the game runs
    def redrawGameWindow():
        global AliveCheck
        manRect=pygame.Rect(man.x+10, man.y+10, 46, 54)
        pygame.draw.rect(screen, (255,255,255),manRect)
        pygame.draw.rect(screen, (255,255,255),RayHitbox)
        # Draws the spikes only in he second level
        if RayIdle==SansIdle and AliveCheck:
            pygame.draw.rect(screen,(255,255,255),SpikeHitbox)
            pygame.draw.rect(screen,(255,255,255),SpikeHitbox2)
        screen.blit(SkyBG, (0,0))
        # This only draws the boss if his health is higher than 0
        if AliveCheck:
            Rayquaza.draw(screen)
        if RayIdle==SansIdle and AliveCheck:
            spike.draw(screen)
            spike2.draw(screen)
        # Draws the boss healthbar, player, and bottom platform
        man.draw(screen)
        pygame.draw.rect(screen, (255,255,255),BottomPlat)
        pygame.draw.rect(screen,green,RayquazaHealth)
        # Draws the bullets when needed
        for bullet in bullets:
            bullet.draw(screen)
        for fireBall in fireBalls:
            fireBall.draw(screen)
            
        pygame.display.update()


    run = True
        # run2=False
    while run:
            # print(man.x)
            for fireBall in fireBalls:
                fireBall.x-=5
            clock.tick(27)
            # Allows us to quit the game with the "X"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # Creates the velocity and movement of the bullets    
            for bullet in bullets:
                if bullet.x < WIDTH and bullet.x > 0:
                    bullet.x += bullet.vel
                else:
                    bullets.pop(bullets.index(bullet))
            # for fireBall in fireBalls:
            #     if fireBall.x < WIDTH and fireBall.x > 0:
            #         fireBall.x += fireBall.vel
            #     else:
            #         fireBall.pop(fireBalls.index(fireBall))

            # Gets us a variable to check if the keys are being pressed
            keys = pygame.key.get_pressed()

            # This checks if we have pressed Space to call the bullets
            if keys[pygame.K_SPACE]:
                if man.left:
                    facing = -1
                else:
                    facing = 1
                    
                if len(bullets) < 5:
                    bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))
                for bullet in bullets:
                    # Checks if the bullet hits the boss' hitbox
                    if (bullet.y - bullet.radius < Rayquaza.hitbox[1] + Rayquaza.hitbox[3]  and (bullet.y + bullet.radius > Rayquaza.hitbox[1]) and bullet.x + bullet.radius > Rayquaza.hitbox[0] and bullet.x - bullet.radius < Rayquaza.hitbox[0]+Rayquaza.hitbox[2]):
                        # print("hi")
                        # if bullet.x + bullet.radius > Rayquaza.hitbox[0] and bullet.x - bullet.radius < Rayquaza.hitbox[0]+Rayquaza.hitbox[2]:
                        # print("hello")

                        #Activates the hit function of the boss and adjusts the lists and counts for the boss and bullets
                        Rayquaza.hit()
                        bullets.pop(bullets.index(bullet))
                        hitCount+=1
                        revengeCount+=1
                        # print(revengeCount)

                        # Creates the ability for the boss to die once they take 40 hits (first level)
                        if hitCount==40 and not LevelCheck:
                                print('unga')
                                tickEnd=pygame.time.get_ticks()
                                print("LEVEL 1 COMPLETE")
                                ScoreTime=tickEnd-tickStart
                                RayIdle=pygame.image.load('FinalProjectResources\Images\BLANK_ICON.png')
                                AliveCheck=False
                                # print(ScoreTime)
                                # print(tickStart)
                                # print(tickEnd)

                                # Creates a time bonus and a score for the player
                                if ScoreTime<=6000:
                                    TimeBonus=1000
                                elif ScoreTime>6000 and ScoreTime<18500:
                                    TimeBonus=500
                                elif ScoreTime>=18500:
                                    TimeBonus=200
                                # Writes the score as a string with the name
                                Score=1000+ScoreTime+TimeBonus+(man.Health*100)
                                ScoreLine=Name+ ":" + str(Score) + "(LEVEL 1)"
                                print(ScoreLine)
                                # Writes the score string in the file
                                MyFile=open('FinalProjectResources\Finished Parts of Final Game\FinalGameScores.txt', 'a') # BY using the relative path we can open the highscore text file 
                                MyFile.write("\n")
                                MyFile.write(ScoreLine)
                                MyFile.close()
                        # Makes the level 2 boss die after 61 hits
                        if hitCount==61 and LevelCheck: 
                            if RayIdle==SansIdle:
                                tickEnd=pygame.time.get_ticks()
                                print("LEVEL 2 COMPLETE")
                                ScoreTime=tickEnd-tickStart
                                RayIdle=pygame.image.load('FinalProjectResources\Images\BLANK_ICON.png')
                                AliveCheck=False
                                # print(ScoreTime)
                                # print(tickStart)
                                # print(tickEnd)

                                # Creates a time bonus and a score for the player
                                if ScoreTime<=6000:
                                    TimeBonus=1000
                                elif ScoreTime>6000 and ScoreTime<18500:
                                    TimeBonus=500
                                elif ScoreTime>=18500:
                                    TimeBonus=200
                                # Writes the score as a string with the name
                                Score=1000+ScoreTime+TimeBonus+(man.Health*100)
                                ScoreLine2=Name+ ":" + str(Score) + "(LEVEL 2)"
                                print(ScoreLine2)
                                # Writes the score string in the file
                                MyFile=open('FinalProjectResources\Finished Parts of Final Game\FinalGameScores.txt', 'a') # BY using the relative path we can open the highscore text file 
                                MyFile.write("\n")
                                MyFile.write(ScoreLine2)
                                MyFile.close()
                                print("THANKS FOR PLAYING")
                                LEV_I=False
                                MENU=True
                                screen.fill(background)
                                TitleMenu("MENU")
                                MainMenu(MenuList)
                        # This creates a revenge ability that allows the boss to shoot back
                        if revengeCount==3:
                            if AliveCheck:
                                # Appends the list to fit the max amount of hits taken by the boss
                                if len(fireBalls) < 66:
                                    # Changes the color based on the boss
                                    if not LevelCheck:
                                        fireBalls.append(projectile(round(Rayquaza.x+Rayquaza.width//2), man.y, 20, (255,0,0), facing)) 
                                    if LevelCheck:
                                        fireBalls.append(projectile(round(Rayquaza.x+Rayquaza.width//2), man.y, 20, (0,0,255), facing)) 
                                # Determines the direction of the fireBall
                                for fireBall in fireBalls:
                                    facing=-1
                                    # Checks if the fireball hits the player
                                    if (fireBall.y - fireBall.radius < man.hitbox[1] + man.hitbox[3]  and (fireBall.y + fireBall.radius > man.hitbox[1]) and fireBall.x + fireBall.radius > man.hitbox[0] and fireBall.x - fireBall.radius < man.hitbox[0]+man.hitbox[2]):
                                                # Activates the plyer's damage function and checks if the health is 0 yet (lets him die)
                                                man.hit()
                                                if man.Health<=0:
                                                    print("YOU DIED")
                                                    LEV_I=False
                                                    MENU=True
                                                    TitleMenu("MENU")
                                                    MainMenu(MenuList)
                            else:
                                        print("He's DED lol")
                            revengeCount=0


            # Lets the player go left as long as he is within the screen
            if keys[pygame.K_LEFT] and man.x > man.vel:
                man.x -= man.vel
                manRect.x=man.x
                man.left = True
                man.right = False
                man.standing = False
            # Lets the player go right as long as he is within the boundries
            elif keys[pygame.K_RIGHT] and man.x < WIDTH - man.width - man.vel:
                man.x += man.vel
                manRect.x=man.x
                man.right = True
                man.left = False
                man.standing = False
            # Lets the player stand in one place
            else:
                man.standing = True
                man.walkCount = 0

            # Deals damage to the player if he touches the boss
            if RayHitbox.colliderect(manRect) and AliveCheck:
                man.Health-=1
                print("HEALTH:",man.Health) 
                man.x=0
                if man.Health<=0:
                    print("YOU DIED")
                    LEV_I=False
                    MENU=True
                    TitleMenu("MENU")
                    MainMenu(MenuList) 
            # Deals damage to the player if they touch the spikes when the second boss is visible
            if SpikeHitbox.colliderect(manRect) and AliveCheck and RayIdle==SansIdle :
                man.x=0
                man.Health-=1
                print("HEALTH:",man.Health) 
                if man.Health<=0:
                    print("YOU DIED")
                    LEV_I=False
                    MENU=True
                    TitleMenu("MENU")
                    MainMenu(MenuList)
            if SpikeHitbox2.colliderect(manRect) and AliveCheck and RayIdle==SansIdle :
                man.x=0
                man.Health-=1
                print("HEALTH:",man.Health) 
                if man.Health<=0:
                    print("YOU DIED")
                    LEV_I=False
                    MENU=True
                    TitleMenu("MENU")
                    MainMenu(MenuList)
            # Stuff for the jumping of the player
            if not(man.isJump):
                if keys[pygame.K_UP]:
                    man.isJump = True
                    man.right = False
                    man.left = False
                    man.walkCount = 0
            else:
                if man.jumpCount >= -10:
                    neg = 1
                    if man.jumpCount < 0:
                        neg = -1
                    man.y -= (man.jumpCount ** 2) * 0.5 * neg
                    manRect.y=man.y
                    man.jumpCount -= 1
                else:
                    man.isJump = False
                    man.jumpCount = 10

        #Resets and changes the level, health, changes the background and boss, and creates the spikes on the ground (when you touch the end of the screen)
    if man.x==WIDTH-65 and not AliveCheck:
        man.x=0
        man.Health=10
        SkyBG=SansBG
        RayIdle=SansIdle
        AliveCheck=True
        RayquazaHealth.width=305
        hitCount=0
        tickStart=pygame.time.get_ticks()
        LevelCheck=True
    redrawGameWindow()
    pygame.display.update()
    # Updates animations and movement        

while check:
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
        if case.type ==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            xm= mouse_pos[0]
            ym= mouse_pos[1]
        # print(mouse_pos)
    keys=pygame.key.get_pressed() #this returns a list
    if MAIN:
        screen.fill(background)
        TitleMenu("MENU")
        MainMenu(MenuList)
    if INST:
        screen.fill(background)
        TitleMenu("INSTRUCTIONS")
        instr()
        first=False
        if ((mouse_pos[0] >200 and mouse_pos[0] <540) and (mouse_pos[1] >500 and mouse_pos[1] <540)):
            INST=False
            first=False
            MAIN=True
    if INST:
        if keys[pygame.K_ESCAPE]:
            INST=False
            MAIN=True
            first=True
    # if SETT and f_SEET:
    #     screen.fill(background)
    #     TitleMenu("SETTINGS")
    #     SettMenu(SettingList)
    #     f_SEET=False
        

    if SETT:
        screen.fill(background)
        TitleMenu("SETTINGS")
        SettMenu(SettingList)
        f_SEET=False
        if keys[pygame.K_ESCAPE]:
            # screen.fill(background)
            SETT=False
            MAIN=True
            f_SEET=False
            bak()
        if keys[pygame.K_1]:
            changeScreenSize(700,680)
            SETT=False
            screen.fill(background)
            MAIN=True
            MainMenu(MenuList)
        if keys[pygame.K_2]:
            changeScreenSize(800,800)
            SETT=False
            screen.fill(background)
            MAIN=True
            MainMenu(MenuList)
        if keys[pygame.K_3]:
            changeScreenSize(600,600)
            SETT=False
            screen.fill(background)
            MAIN=True
            MainMenu(MenuList)
        if keys[pygame.K_4]:
            walkRight = [pygame.image.load('FinalProjectResources\Images\R1.png'), pygame.image.load('FinalProjectResources\Images\R2.png'), pygame.image.load('FinalProjectResources\Images\R3.png'), pygame.image.load('FinalProjectResources\Images\R4.png'), pygame.image.load('FinalProjectResources\Images\R5.png'), pygame.image.load('FinalProjectResources\Images\R6.png'), pygame.image.load('FinalProjectResources\Images\R7.png'), pygame.image.load('FinalProjectResources\Images\R8.png'), pygame.image.load('FinalProjectResources\Images\R9.png')]
            walkLeft = [pygame.image.load('FinalProjectResources\Images\L1.png'), pygame.image.load('FinalProjectResources\Images\L2.png'), pygame.image.load('FinalProjectResources\Images\L3.png'), pygame.image.load('FinalProjectResources\Images\L4.png'), pygame.image.load('FinalProjectResources\Images\L5.png'), pygame.image.load('FinalProjectResources\Images\L6.png'), pygame.image.load('FinalProjectResources\Images\L7.png'), pygame.image.load('FinalProjectResources\Images\L8.png'), pygame.image.load('FinalProjectResources\Images\L9.png')]
        if keys[pygame.K_5]:
            walkLeft=[JakePaul]
            walkRight=[JakePaul]
        if keys[pygame.K_6]:
            MAIN=True
            screen.fill(background)
            MainMenu(MenuList)
            SETT=False
            f_SEET=False
            pygame.time.delay(10)

        
    if LEV_I:
        MAIN=False
        playGame()
        
    if LEV_II:
        screen.fill(background)
        TitleMenu("LEVEL II")
        if keys[pygame.K_ESCAPE]:
            LEV_II=False
            MAIN=True
    if LEV_III:
        screen.fill(background)
        TitleMenu("LEVEL III")
        if keys[pygame.K_ESCAPE]:
            LEV_III=False
            MAIN=True
    # if SCORE and screCk:
        
        #call funct t print scres
    if SCORE:
        TitleMenu("SCORES")
        MyFile=open('FinalProjectResources\Finished Parts of Final Game\FinalGameScores.txt', 'a')
        ScoreB()
        BackButton=INST_FNT.render("BACK",1,(0,0,0))
        screen.blit(BackButton,(260,525))
        pygame.display.update()
        if ((mouse_pos[0] >260 and mouse_pos[0] <300) and (mouse_pos[1] >525 and mouse_pos[1] <565)):
                bak()
                TitleMenu("Main Menu")
                MainMenu(MenuList)
    if ((mouse_pos[0]>20 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)) and MAIN:
        MAIN=False
        INST=True
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <330))and MAIN:
        MAIN=False
        SETT=True  
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <380))and MAIN :
        MAIN=False
        LEV_I=True   
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <430))and MAIN :
        MAIN=False
        SCORE=True  
    if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >450 and mouse_pos[1] <480))and MAIN :
        quit()
    # if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >450 and mouse_pos[1] <480))and MAIN:
    #     MAIN=False
    #     LEV_III=True   
    # if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >500 and mouse_pos[1] <530))and MAIN:
    #     MAIN=False
    #     SCORE=True 
    # if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <330)) and SETT and set_first:  
    #     screen.fill(background)
    #     TitleMenu("Screen Size")
    #     MainMenu(sizeList )
    #     sc_size=True
    #     set_first=False
    #     f_SEET=True
    #     if keys[pygame.K_ESCAPE]:
    #         sc_size=False
    #         set_first=False
    #         SETT=True
    #         f_SEET=True
    # if sc_size and mouse_pos[0] >0:
    #     changeScreenSize(mouse_pos[0],mouse_pos[1])
    #     screen.fill(background)
    #     TitleMenu("Screen Size")
    #     MainMenu(sizeList)
    #     if keys[pygame.K_ESCAPE]:
    #         sc_size=False
    #         set_first=True
    #         c_first=True
    #         SETT=True
    # # if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <330))and SETT and set_first:
    # if (SETT and c_first and not sc_size and set_first):

    #         screen.fill(background)
    #         TitleMenu("Characters")
    #         SettMenu(Characters)
    #         c_first=True
    #         if keys[pygame.K_ESCAPE]:
    #             c_first=True
    #             set_first=True
    # if ((mouse_pos[0] >20 and mouse_pos[0] <80) and (mouse_pos[1] >550 and mouse_pos[1] <580)) :
    #     screen.fill(background)
    #     keepScore(121)
    #     text=INST_FNT.render("Make sure you update the score file", 1, BLACK)
    #     screen.blit(text, (40,200))
    #     text=INST_FNT.render("before you exit", 1, BLACK)
    #     screen.blit(text, (40,300))
    #     text=INST_FNT.render("Thank you for playing", 1, BLACK)
    #     screen.blit(text, (40,400))
    #     pygame.display.update()
    #     pygame.time.delay(50)
    #     MAIN=False
    #     SCORE=False 
    #     pygame.time.delay(3000)
    #     check=False
    pygame.display.update()
    # pygame.time.delay(10)

os.system('cls')
# pygame.quit()