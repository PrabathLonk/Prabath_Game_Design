#Prabath Girish
# 5/5/22
# Code inspiration for animations, bullets
# Import the systems we need to use
import pygame, os, random, datetime
pygame.init()
os.system('cls')

#Create our screen and it's width and height from Tech With Tim's Pygame Tutorial : https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/projectiles/
WIDTH=700
HEIGHT=600
win = pygame.display.set_mode((WIDTH,HEIGHT))

#Title Our sceen
pygame.display.set_caption("Level 1: Rayquaza")

# This is to declare our values that we will be using:
# Defines the images for the game and scales them as well as the hitboxes to show:
walkRight = [pygame.image.load('FinalProjectResources\Images\R1.png'), pygame.image.load('FinalProjectResources\Images\R2.png'), pygame.image.load('FinalProjectResources\Images\R3.png'), pygame.image.load('FinalProjectResources\Images\R4.png'), pygame.image.load('FinalProjectResources\Images\R5.png'), pygame.image.load('FinalProjectResources\Images\R6.png'), pygame.image.load('FinalProjectResources\Images\R7.png'), pygame.image.load('FinalProjectResources\Images\R8.png'), pygame.image.load('FinalProjectResources\Images\R9.png')]
walkLeft = [pygame.image.load('FinalProjectResources\Images\L1.png'), pygame.image.load('FinalProjectResources\Images\L2.png'), pygame.image.load('FinalProjectResources\Images\L3.png'), pygame.image.load('FinalProjectResources\Images\L4.png'), pygame.image.load('FinalProjectResources\Images\L5.png'), pygame.image.load('FinalProjectResources\Images\L6.png'), pygame.image.load('FinalProjectResources\Images\L7.png'), pygame.image.load('FinalProjectResources\Images\L8.png'), pygame.image.load('FinalProjectResources\Images\L9.png')]
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
# Here we make our Player class that defines the Player Character
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
        self.Health=10
        #Creates the hitbox
        self.hitbox = (self.x+10, self.y+5, 25, 25)

    def draw(self, win):
        #This function draws the character
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        #This draws the hitbox of the character
        self.hitbox = (self.x+10, self.y+10, 44, 50)
        # pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        # This animates the character
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
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

    def draw(self,win):
        # Draws the bullet
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
        self.hitbox=(self.x-self.radius,self.y-self.radius,2*self.radius,2*self.radius)
        # pygame.draw.rect(win, (255,0,0), self.hitbox,2)
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
    def draw(self, win):
        # self.move()
        win.blit(RayIdle,(RayHitbox.x,RayHitbox.y))
        self.hitbox = (self.x, self.y, WIDTH/4, HEIGHT-175) 
        # pygame.draw.rect(win, (255,0,0), self.hitbox,2)
    def hit(self):  # This will display when the enemy is hit and indicate they have taken damage via the health
        RayquazaHealth.width-=5
# This function draws everything we need on the window and updates it as the game runs
def redrawGameWindow():
    global AliveCheck
    manRect=pygame.Rect(man.x+10, man.y+10, 46, 54)
    pygame.draw.rect(win, (255,255,255),manRect)
    pygame.draw.rect(win, (255,255,255),RayHitbox)
    # Draws the spikes only in he second level
    if RayIdle==SansIdle and AliveCheck:
        pygame.draw.rect(win,(255,255,255),SpikeHitbox)
        pygame.draw.rect(win,(255,255,255),SpikeHitbox2)
    win.blit(SkyBG, (0,0))
    # This only draws the boss if his health is higher than 0
    if AliveCheck:
        Rayquaza.draw(win)
    if RayIdle==SansIdle and AliveCheck:
        spike.draw(win)
        spike2.draw(win)
    # Draws the boss healthbar, player, and bottom platform
    man.draw(win)
    pygame.draw.rect(win, (255,255,255),BottomPlat)
    pygame.draw.rect(win,green,RayquazaHealth)
    # Draws the bullets when needed
    for bullet in bullets:
        bullet.draw(win)
    for fireBall in fireBalls:
        fireBall.draw(win)
        
    
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
    def draw(self, win):
        win.blit(Spike,(self.x,self.y))





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
# fireBall=projectile(Rayquaza.x,random.randint((man.x-50),(man.x+50)),5,(255,0,0),0)
# Creates the loop that runs the game
run = True
run2=False
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
                        ScoreLine="\n" + Name+ ":" + str(Score) + "(LEVEL 2)"
                        print(ScoreLine)
                        # Writes the score string in the file
                        MyFile=open('FinalProjectResources\Finished Parts of Final Game\FinalGameScores.txt', 'a') # BY using the relative path we can open the highscore text file 
                        MyFile.write(ScoreLine)
                        MyFile.close()
                        print("THANKS FOR PLAYING")
                        quit()
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
                                            print("HEALTH:",man.Health)
                                            print("YOU DIED")
                                            quit()
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
        if Health<=0:
            print("YOU DIED")
            quit()  
    # Deals damage to the player if they touch the spikes when the second boss is visible
    if SpikeHitbox.colliderect(manRect) and AliveCheck and RayIdle==SansIdle :
        man.x=0
        man.Health-=1
        print("HEALTH:",man.Health) 
        if Health<=0:
            print("YOU DIED")
            quit() 
    if SpikeHitbox2.colliderect(manRect) and AliveCheck and RayIdle==SansIdle :
        man.x=0
        man.Health-=1
        print("HEALTH:",man.Health) 
        if Health<=0:
            print("YOU DIED")
            quit() 
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
    if man.x==WIDTH-manRect.width and not LevelCheck:
        man.x=0
        Health=10
        SkyBG=SansBG
        RayIdle=SansIdle
        AliveCheck=True
        RayquazaHealth.width=305
        hitCount=0
        tickStart=pygame.time.get_ticks()
        LevelCheck=True
    # Updates animations and movement        
    redrawGameWindow()

pygame.quit()