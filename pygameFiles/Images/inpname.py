#Zara Paul
#06/17/22
#Get user name :
#Create screen 
#title= enter yr name (FONTS)
#create box
#create name variable:
#   add the letter  
#   if press backspace delete last character 
#   if press RETURN they are done

import sys
from turtle import done, width
import pygame, time,os,random, math
pygame.init()#initialize the pygame package

# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)

os.system('clear')
WIDTH=700 #like constant
HEIGHT=700
colors={"magenta":(255,0,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51)}
clr=colors.get("limeGreen")
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Daniel 2.0")  #change the title of my window
clock=pygame.time.Clock()

backgrnd=(255,0,255)
screen.fill(backgrnd)
nameColor=(153,255,51)
bxColor= (200,200,200)
pygame.display.update()
pygame.time.delay(500)

Title = TITLE_FONT.render("Daniel", 1, bxColor)
#create your box related to width and height 

input_rect= pygame.Rect(WIDTH//3, HEIGHT//3, 140,32)
user_name=""
run=True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        #menu(maintitle,messageMenu)
         print(user_name)
         pygame.quit()
         sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #change BOX color 
            print()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                print(user_name)
                pygame.quit()
                sys.exit()
        if event.key==pygame.K_BACKSPACE:
            user_name = user_name[:-1]
            # or an else statement 
        else:
            user_name += event.unicode #gives all characters that exist 
            #update my userName += event.unic
    screen.fill((255,255,255))

    screen.blit(Title,(200,50))
            #draw rect
    pygame.draw.rect(screen, bxColor, input_rect)
        #update the name user 
    name=MENU_FONT.render(user_name,1, nameColor)
    screen.blit(name(input_rect.x+5, input_rect.y+5))
    pygame.display.flip()

#draw rectangle 