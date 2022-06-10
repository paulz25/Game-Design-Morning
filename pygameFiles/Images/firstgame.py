#Zara Paul 6/9/2022
#We are learning pygame basic functions, 
#   creating screens. clrs, shapes

from turtle import width
import pygame, time, os
os,os.system('clear')
pygame.init() #initialize pygame package 

width=700 #like a constant 
height=700 
#create display window with any name you like 
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("my first game") #change title of my window
pygame.time.delay(2000)
redClr=(255,0,0)
#screen.fill(redClr) #fills background 
#pygame.display.update()
#pygame.time.delay(2000)
greenClr=(0,255,0)
purpleClr=(125,)
#screen.fill(greenClr)
#pygame.display.update()
#pygame.time.delay(2000)
#keep runnung create a loop
hb=50
wb=50
xb=100
yb=300
backgrnd=greenClr
square=(xb,yb,wb,hb) #create the ject to draw
run = True
while run:
    screen.fill(backgrnd)
    for event in pygame.event.get:
        if event.type==pygame.QUIT:
            run=False
            print("You Quit")
    pygame.draw.rect(screen,redClr, square)
    #circle(surface,color,rect)-> Rect
    

    pygame.display.update()


    

