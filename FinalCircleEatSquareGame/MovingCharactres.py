# Prabath Girish
# # 4/4/22
import os, random, time, pygame, math, datetime
from turtle import update
# name=input("What is your name:")
#initialize pygame
pygame.init()
WIDTH=700
HEIGHT=700
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("LEVEL 2")
bg=pygame.image.load('FinalCircleEatSquareGame\Images\Volcano.jpg')
Darm=pygame.image.load('FinalCircleEatSquareGame\Images\Screenshot (12).png')
Gliscor=pygame.image.load('FinalCircleEatSquareGame\Images\Screenshot (13).png')
screen.blit(bg,(0,0))
screen.blit(Darm,(0,0))
screen.blit(Gliscor,(200,300))
pygame.display.update()
pygame.time.delay(2000)