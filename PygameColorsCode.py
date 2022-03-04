#Prabath Girish
# 3/4/22
import os, time

import pygame as p

os.system('cls')

 

#initialize pygame

p.init()

#define colors

 

white=[255,255,255]

red=[255,0,0]

mag=[255,0,255]

aqua=[51,153,255]

m=[47,192,229]

 

# create a window/screen

WIDTH=600

HEIGHT=700

screen=p.display.set_mode((WIDTH,HEIGHT))

p.display.set_caption("My window")

# screen.fill(mag)

# p.display.update()

# p.time.delay(500)

# screen.fill(aqua)

# p.display.update()

# p.time.delay(500)

# screen.fill(red)

# p.display.update()

# p.time.delay(500)

#how to draw something?

#define a rectangle

#position

x=20

y=30

#w and h of rectangle

wbox=50

hbox=50

square=p.Rect(x,y,wbox,hbox)

 

run=True

while run:

    screen.fill(mag)

 

    for event in p.event.get():

        if event.type== p.QUIT:

            run=False

    square.x +=5

    square.y +=5

    p.draw.rect(screen,(white), square)

    p.draw.rect(screen,(red), square)

    p.display.update()

    p.time.delay(100)