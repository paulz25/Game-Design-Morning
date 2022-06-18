#Zara Paul 
#6/9/2022
#We are learning pygame basic functins, 
# creating screens, clrs, shape ,move 
# move  the square
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow
#picture = pygame. image. load(filename)
#picture = pygame. transform. scale(picture, (1280, 720))
#bg=pygame.image.load('ClassStuff\CircleEatsSquare\Images\\bgSmaller.jpg')


#input name!!!!!!!!!!!!!!

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
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51)}
clr=colors.get("limeGreen")
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window
#game Variable
player=1
markers=[]
lineWidth=10
Game=True
gameOver=False
Xpoints= 0
Opoints= 0
MxMy=(0,0)
print(markers)  
cirClr=colors.get("blue")
xClr=colors.get("BLACK")
#images
bg=pygame.image.load('pygameFiles/Images/images/bgSmaller.jpeg')
char = pygame.image.load('pygameFiles/Images/images/PixelArtTutorial.png')
char = pygame.transform.scale(char, (50, 50))
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)

#square Var
hb=50
wb=50
xb=100
yb=300

#character vars
charx = xb
chary = yb

#circle
cx=350
cy=350
rad=25

#inscribed box
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)

#mouse varuables
mx = 0
my = 0

#objects to draw
square=pygame.Rect(xb,yb,wb,hb)
insSquare=pygame.Rect(xig,yig,ibox,ibox)
mountainSqaure = pygame.Rect(250, 320, 180, 250)

#collors
squareClr=colors.get("pink")
circleClr=colors.get("blue")
backgrnd=colors.get("white")
buttoncolor=colors.get('pink')

#Game control
run = True
Game = False
speed=2

#Menu items
message = ["Instructions", "Settings", "Game 1", "Game 2", "Scoreboard", "Exit"]

def menu():
    screen.fill(backgrnd)
    ymenu = 155
    Title = TITLE_FONT.render("tic tac toe", 1, colors.get("blue"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 100))
    Bx = WIDTH//3

    Button_1 = pygame.Rect(Bx, 150, WIDTH//4, 40)
    Button_2 = pygame.Rect(Bx, 200, WIDTH//4, 40)
    Button_3 = pygame.Rect(Bx, 250, WIDTH//4, 40)
    Button_4 = pygame.Rect(Bx, 300, WIDTH//4, 40)
    Button_5 = pygame.Rect(Bx, 350, WIDTH//4, 40)
    Button_6 = pygame.Rect(Bx, 400, WIDTH//4, 40)
    pygame.draw.rect(screen,buttoncolor, Button_1)
    pygame.draw.rect(screen,buttoncolor, Button_2)
    pygame.draw.rect(screen,buttoncolor, Button_3)
    pygame.draw.rect(screen,buttoncolor, Button_4)
    pygame.draw.rect(screen,buttoncolor, Button_5)
    pygame.draw.rect(screen,buttoncolor, Button_6)

    for item in message:
        text = MENU_FONT.render(item, 1, colors.get('blue'))
        screen.blit(text, (Bx, ymenu))
        pygame.display.update()
        pygame.time.delay(50)
        ymenu += 50
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint((mx, my)):
                    Instructions("Instructions", "pygameFiles/Images/instructions.txt")
                if Button_2.collidepoint((mx, my)):
                    settings()
                if Button_3.collidepoint((mx, my)):
                    game1()
                if Button_4.collidepoint((mx, my)):
                    game2()
                if Button_5.collidepoint((mx, my)):
                    Instructions ("Scoreboard", "pythonFIles/scre.txt")
                if Button_6.collidepoint((mx, my)):
                    pygame.quit()
                    sys.exit()

def Instructions(TITLE,FILE):
    #rendering text objects
    Title = TITLE_FONT.render("Instructions", 1, colors.get("blue"))
    Title = TITLE_FONT.render(TITLE, 1, colors.get("blue"))

    #fills screen with white
    screen.fill(backgrnd)

    #creating button options
    #Button_1 = pygame.Rect(200, 400, 100, 50)
    #Button_2 = pygame.Rect(400, 400, 100, 50)
    #pygame.draw.rect(screen, colors.get("limeGreen"), Button_1)
    #pygame.draw.rect(screen, colors.get("limeGreen"), Button_2)

    #Instructions
    myFile = open(FILE, "r")
    content = myFile.readlines()

    #var to controll change of line
    yinstructions = 150
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 40

    myFile.close()

    #renderig fonts to the screen
    xd = WIDTH//2 - (Title.get_width()//2)
    #screen.blit(Title, (xd, 50))
    #screen.blit(text1, (Bx, 300)) #help 

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                menu()
                print("Y quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                #if Button_1.collidepoint((mx, my)):
                    #return True 
def settings (): 
    global WIDTH, HEIGHT, backgrnd, buttoncolor, screen, mx, my
    screen.fill(backgrnd)
    ymenu = 155
    Title = TITLE_FONT.render("Settings", 1, colors.get("blue"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 100))
    Bx = WIDTH//3
    colorRand = MENU_FONT.render("Randomize background color", 1, colors.get("blue"))
    bgcolor = MENU_FONT.render("Randomize button color", 1, colors.get("blue"))
    sizeincrease = MENU_FONT.render("Increase screen size",1, colors.get ("blue"))
    sizedecrease = MENU_FONT.render("Decrease screen size",1, colors.get ("blue"))
    done = MENU_FONT.render("Done changing settings",1, colors.get ("blue"))

    Button_Background = pygame.Rect(Bx, 150, WIDTH//4, 40)
    Button_Characters = pygame.Rect(Bx, 200, WIDTH//4, 40)
    Button_ScreensizeIncrease = pygame.Rect(Bx, 250, WIDTH//4, 40)
    Button_ScreensizeDecrease = pygame.Rect(Bx, 300, WIDTH//4, 40)
    Button_Done = pygame.Rect(Bx, 350, WIDTH//4, 40)

    pygame.draw.rect(screen, buttoncolor, Button_Background)
    pygame.draw.rect(screen, buttoncolor, Button_Characters)
    pygame.draw.rect(screen, buttoncolor, Button_ScreensizeIncrease)
    pygame.draw.rect(screen, buttoncolor, Button_ScreensizeDecrease)
    pygame.draw.rect(screen, buttoncolor, Button_Done)

    screen.blit(colorRand, (WIDTH//2 - (colorRand.get_width()//2), 160))
    screen.blit(bgcolor, (WIDTH//2 - (bgcolor.get_width()//2), 210))
    screen.blit(sizeincrease, (WIDTH//2 - (sizeincrease.get_width()//2), 260))
    screen.blit(sizedecrease, (WIDTH//2 - (sizedecrease.get_width()//2), 310))
    screen.blit(sizedecrease, (WIDTH//2 - (done.get_width()//2), 360)) 
    pygame.display.update()

    while True: 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos=pygame.mouse.get_pos()
                mx=mousepos[0]
                my=mousepos[1]
                if Button_Background.collidepoint(mx,my):
                    backgrnd=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                    screen.fill(backgrnd)
                if Button_Characters.collidepoint(mx,my):
                    buttoncolor=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                if Button_ScreensizeIncrease.collidepoint(mx,my)and WIDTH < 1100:
                    WIDTH+=100
                    screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
                if Button_ScreensizeDecrease.collidepoint(mx,my)and WIDTH > 500:
                    WIDTH-=100
                    screen=pygame.display.set_mode((WIDTH,HEIGHT))
                if Button_Done.collidepoint(mx,my):
                    return menu()
            pygame.display.update()
            settings() 
                    #creen size is plus and minus box 
                    #change width = 800 and redefine screen variables screen=pygame.display.set
def game1(): 
    global run, insSquare, charx, chary, cx, cy, rad
    while run:
        # screen.fill(backgrnd)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                # print(mousePos)
        
        pygame.draw.rect(screen, colors.get("white"), mountainSqaure)
        screen.blit(bg, (0,0))
        keys= pygame.key.get_pressed() #this is a list
        #mve square
        if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb):
            square.x += speed
            charx += speed
        if keys[pygame.K_LEFT] and  square.x > speed:
            square.x -= speed
            charx -= speed
        if keys[pygame.K_UP] and square.y >speed:   #means clser t 0
            square.y -= speed
            chary -= speed
        if keys[pygame.K_DOWN] and square.y <HEIGHT -hb:  #means clser t max value HEIGHT
            square.y += speed
            chary += speed
            #mve Circle
        if keys[pygame.K_d] and cx < WIDTH -(rad):
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_a] and  cx > (speed+rad):
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_w] and cy >(speed+rad):   #means clser t 0
            cy -= speed
            insSquare.y -= speed
        if keys[pygame.K_s] and cy <HEIGHT -(rad):  #means clser t max value HEIGHT
            cy += speed
            insSquare.y += speed

        if square.colliderect(insSquare):
            print("BOOM")
            rad+=1
            cx=random.randint(rad, WIDTH-rad)
            cy=random.randint(rad, HEIGHT-rad)
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
        
        if square.colliderect(mountainSqaure):
            square.x = 10
            square.y = 10
            charx = 10
            chary = 10

        #rect(surface, color, rect) -> Rect
        pygame.draw.rect(screen, squareClr,square)
        screen.blit(char, (charx, chary))

        #circle(surface, color, center, radius)
        pygame.draw.rect(screen, squareClr, insSquare)
        pygame.draw.circle(screen, circleClr, (cx,cy), rad)

        pygame.display.update()
        pygame.time.delay(5)
        pygame.display.update()

def game2():
    pygame.display.set_caption("Tic Tac Toe")  #change the title of my window
    backgrnd=colors.get("pink")
    def zero_Array(): 
        for x in range(3):
            row= [0] *3
        markers.append(row)


    def draw_grid():
        lineClr=colors.get("white")
        for x in range(1,3):
            pygame.draw.line(screen,lineClr,(0,HEIGHT//3*x),(WIDTH,HEIGHT//3*x),lineWidth)  #Hztal line
            pygame.draw.line(screen,lineClr,(WIDTH//3*x, 0),(WIDTH//3*x,HEIGHT),lineWidth)  #Vert line
        pygame.time.delay(100)

    def draw_Markers():
        xValue=0
        for x in markers:   # getting a rw
            yValue=0
            for y in x:  #each elem fthe rw
                if y ==1:
                    #print ("x")
                    pygame.draw.line(screen,xClr,(xValue * WIDTH//3 + 15, yValue * HEIGHT//3 + 15), (xValue * WIDTH//3 + WIDTH//3-15, yValue * WIDTH//3 + WIDTH//3-15),lineWidth)
                    pygame.draw.line(screen, xClr,(xValue*WIDTH//3 +WIDTH//3-15, yValue*HEIGHT//3+15),(xValue *WIDTH//3+15,yValue*HEIGHT//3+HEIGHT//3-15),lineWidth)
                if y==-1:
                    #print("O")
                    pygame.draw.circle(screen,cirClr,(xValue*WIDTH//3+WIDTH//6,yValue*HEIGHT//3 +HEIGHT//6),WIDTH//6-15, lineWidth)
                yValue +=1
            xValue +=1
        pygame.display.update() 

    def checkWinner():
        global gameOver,winner
        x_pOs=0
        for x in markers:
            #check COL
            if sum(x) ==3:
                print("sum")
                winner = 1
                gameOver=True
            if sum(x) ==-3:
                winner = -1
                gameOver=True
            #Check ROWS
            if markers[0][x_pOs] +markers[1][x_pOs]+markers[2][x_pOs] == 3:
                winner = 1
                gameOver=True

            if markers[0][x_pOs] +markers[1][x_pOs]+markers[2][x_pOs] == -3:
                winner = -1
                gameOver=True
            x_pOs +=1
        # #Check DiagOnals 
        if markers[0][0]+markers[1][1]+markers[2][2] == 3 or markers[2][0]+markers[1][1]+markers[0][2] == 3:
            winner = 1
            gameOver=True
        if markers[0][0]+markers[1][1]+markers[2][2] == -3 or markers[2][0]+markers[1][1]+markers[0][2] == -3:
            winner = -1
            gameOver=True
        #Check FOR a tie
        if gameOver ==False:
            tie=True
            for ROW in markers:
                for COL in ROW:
                    if COL ==0:
                        tie=False
            #LEts make winner =0 if it is tie
            if tie:   #in a bOOlean variable dOnt need ==  if tie == True
                gameOver=True
                winner=0

    def gameEnd(): 
        while gameEnd():
            global Game, Xpoints, Opoints 
        #we will be displaying here!
        screen.fill(backgrnd)
        dis=""
        if winner == 1:
            dis="Player X is the winner!"
            Xpoints += 1 
        if winner == -1:
            dis="Player O is the winner!"
            Opoints += 1 
        if winner == 0:
            dis="No one won......."
        item=MENU_FONT.render(dis, 1, (200,200,200))
        screen.blit(item,(WIDTH//2 - (item.get_width()//2), 200))  
        pygame.time.delay(3000)
        text2= MENU_FONT.render("The game is over. Do you want to play again?", 1, colors.get("blue"))
        screen.blit(text2,(WIDTH//2 - (text2.get_width()//2),50))

        Button_Yes= pygame.Rect((WIDTH//4, HEIGHT//2), (100, 40))
        Button_No= pygame.Rect((3*WIDTH//4, HEIGHT//2), (100, 40))
        pygame.draw.rect(screen, colors.get("limeGreen"), Button_Yes)
        pygame.draw.rect(screen, colors.get("limeGreen"), Button_No)  

        text3= MENU_FONT.render("Yes play again", 1, colors.get("blue"))
        screen.blit(text3,(WIDTH//4, HEIGHT//2))

        text4= MENU_FONT.render("No,exit", 1, colors.get("blue"))
        screen.blit(text4,(3*WIDTH//4, HEIGHT//2))


        scoreText = MENU_FONT.render("X has: " + str(Xpoints) + " points    O has: " + str(Opoints) + " points", 1, colors.get("blue"))
        screen.blit(scoreText,(WIDTH//2 - (scoreText.get_width()//2),100))
    
        pygame.display.update()
        loop=True
        while loop: 
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                #Menu(mainTitle,messageMenu)
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                MxMy = pygame.mouse.get_pos()
                mx=MxMy[0]
                my=MxMy[1]
                if Button_No.collidepoint((mx, my)):
                    pygame.quit()
                    sys.exit()
                if Button_Yes.collidepoint((mx, my)):
                    zero_Array()
                    loop=False
    zero_Array()
    while Game:
        screen.fill(backgrnd)
        draw_grid()
        draw_Markers()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                #Menu(mainTitle,messageMenu)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                MxMy = pygame.mouse.get_pos()
                cellx=MxMy[0]//(WIDTH//3)
                celly=MxMy[1]//(HEIGHT//3)
                print(cellx, celly)
                if markers[cellx][celly]==0:
                    markers[cellx][celly]=player
                    player *=-1
                    checkWinner()
                    if gameOver:
                        pygame.quit()
                        sys.exit()     
        pygame.display.update() 
        pygame.time.delay(100)
menu()
