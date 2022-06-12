#Zara Paul 
#Today we will be learning how to animate images 




import pygame
pygame.init() #initiate pygame

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png') 

#Omg took so long!! LOL
#walk right and left lists is file name, extension, etc. 
#pyg.mr path join from a different folder 
#Pygame.path(join)
#bg is background image 
#char is standing/jumping sprite

clock = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
vel = 5 #velocity?
isJump = False
jumpCount = 10 #steps he told us to do 
left = False
right = False
walkCount = 0


def redrawGameWindow(): #redraw game window 
    global walkCount #changing variable 
    win.blit(bg, (0,0))

    if walkCount + 1 >= 27: #if we tried to have walkcount greater than 27 it will run into index error
        walkCount = 0

    if left: #int divdide by three gets rid of integers 
        win.blit(walkLeft[walkCount//3], (x,y)) #win.blit with photo and where you want to place it 
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount +=1 #incrementing walk count variables 
    else:
        win.blit(char, (x,y)) #standing still or jumping is blit character  
    
    pygame.display.update()

#Frame Rate is how long displayed and the display 
#Clock will set SPS to 27 which is pretty much frame rate 

#mainloop
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False #going left 
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel #going right 
        right = True
        left = False
    else:
        right = False
        left = False #if not 
        walkCount = 0 #shows how many steps 
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0 #no longer moving left and right with spaces 
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
            
    redrawGameWindow()

pygame.quit()

