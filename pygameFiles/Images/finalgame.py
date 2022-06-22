#zara paul 
#I need to create a mouse eating cheese and cat eating mouse game 
#get all necessary imports such as os, etc. 
#get menu working 
#menu has settings 
#menu has exit
#menu had game options one and two
# menu also has enter name 
# menu also has scoreboard 
# make options for games 
#games will be mouse vs cat and mouse vs cheese different levels 
#Games will also be with different maps based on the level
#I need to import my files 
#insert files path in get background fill, or get “character”
#I need to make map one 
#screen.blit(Image)
# i also need to figure out how to make the maze a barrier
# so screen.collidepoint. Etc. etc., maybe if something collides with certain walls it will just stop characters motion (need to research)
#maybe an if statement, elif for that 
#character moves and secures cheese
#everytime the character hits the cheese (collidepoint) the game += 1 to score 
#score keeps track when hit all 4 cheeses 
#if you hit the moving targets (cats, etc. you will get killed)
#if collidepoint >3 while run:
	#End game 
#i need to make map two and do the same, change characters, etc. 

import os, pygame, time 
pygame.init()
os.system("clear")

backgrnd= pygame.image.load("/Users/zarapaul/Desktop/Game-Design-Morning/pygameFiles/Images/Screen Shot 2022-06-21 at 9.07.17 AM.png")
pygame.display.set_caption("Collect The Prize")
WIDTH= 700
HEIGHT= 700
screen= pygame.display.set_mode((WIDTH, HEIGHT))
backgrnd= pygame.transform.scale(backgrnd,(WIDTH,HEIGHT))
clock = pygame.time.Clock()

def Game1():
    screen.blit(backgrnd,(0,0))
    
    pygame.display.update()
run=True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False 
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            mousepos=pygame.mouse.get_pos()
            mx=mousepos[0]
            my=mousepos[1]
            print(mx,my)
    Game1()

box1= #top left x, y, wdith, height 

    



   

  
        




