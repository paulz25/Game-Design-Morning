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
#zara paul 
#
import pygame
WIDTH=700
HEIGHT=700
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
box = pygame.Rect(WIDTH//3-25, 0, 50, 50)
down = True
up = False
backgrnd= (0,0,0)
 
 
class Wall(pygame.sprite.Sprite):
   #represents the bar at the bottom that the player controls 
 
    def __init__(self, x, y, width, height, color):
 
        # Call the parent's constructor
        super().__init__()
 
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
 
class Player(pygame.sprite.Sprite): #basic code need to add onto this 

    change_x = 0 #speed for now 
    change_y = 0
 
    def __init__(self, x, y): #constructing this 
 
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
    def changespeed(self, x, y):
       #for settings and chnaginng speed 
        self.change_x += x
        self.change_y += y
 
    def move(self, walls): #making it when the player hits nothing moves 
 
        # Move left/right
        self.rect.x += self.change_x
 
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of item hit 
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                #opposite 
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0: #our reset would not be dramatic
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
        
        #set the value 
 
 
class Room(object):
    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    enemy_sprites = None
 
    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
 
 
class Room1(Room):
 #creates our "rooms"
    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [390, 50, 20, 500, BLUE]
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

 
 
class Room2(Room):
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, RED],
                 [0, 350, 20, 250, RED],
                 [780, 0, 20, 250, RED],
                 [780, 350, 20, 250, RED],
                 [20, 0, 760, 20, RED],
                 [20, 580, 760, 20, RED],
                 [190, 50, 20, 500, GREEN],
                 [590, 50, 20, 500, GREEN]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
 
class Room3(Room):
    #same code as above 
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, PURPLE],
                 [0, 350, 20, 250, PURPLE],
                 [780, 0, 20, 250, PURPLE],
                 [780, 350, 20, 250, PURPLE],
                 [20, 0, 760, 20, PURPLE],
                 [20, 580, 760, 20, PURPLE]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
        for x in range(100, 800, 100):
            for y in range(50, 451, 300):
                wall = Wall(x, y, 20, 200, RED)
                self.wall_list.add(wall)
 
        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, WHITE)
            self.wall_list.add(wall)
 
 
def main():

    # Call this function so the Pygame library can initialize itself
    pygame.init()
 
    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])
 
    # Set the title of the window
    pygame.display.set_caption('Secure the Prize')
 
    # Create the player paddle object
    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
 
    rooms = []
 
    room = Room1()
    rooms.append(room)
 
    room = Room2()
    rooms.append(room) #rooms being treated like files in this sense 
 
    room = Room3()
    rooms.append(room)
 
    current_room_no = 0
    current_room = rooms[current_room_no]
 
    clock = pygame.time.Clock()
 
    done = False
 
    while not done: #put room number if statement for the moving box
        # --- Event Processing ---
        screen.fill((0,0,0))  
        pygame.time.delay(50)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0) #moving evrrything around chnaging the coordinates and how much it moves when youclick 
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5) #moving 5 down, etc. 
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)

        # if current_room_no == 0:
        #     if box.y >= 650:
        #         up = True
        #         down = False

        #     if box.y <= 0:
        #         up = False
        #         down = True
            
        #     if up:
        #         box.y -= 5
            
        #     if down:
        #         box.y += 5
        # pygame.draw.rect(screen, (255,0,0), box)
        # pygame.display.update()

 
        # --- Game Logic --- #movinng from rooms and also just having the character move in right sport above 
 
        player.move(current_room.wall_list)
    
        if player.rect.x < -15:
                if current_room_no == 0:
                    current_room_no = 2
                    current_room = rooms[current_room_no]
                    player.rect.x = 790
                elif current_room_no == 2:
                    current_room_no = 1
                    current_room = rooms[current_room_no]
                    player.rect.x = 790
                else:
                    current_room_no = 0
                    current_room = rooms[current_room_no]
                    player.rect.x = 790
    
        if player.rect.x > 801:
                if current_room_no == 0:
                    current_room_no = 1
                    current_room = rooms[current_room_no]
                    player.rect.x = 0
                elif current_room_no == 1:
                    current_room_no = 2
                    current_room = rooms[current_room_no]
                    player.rect.x = 0
                else:
                    current_room_no = 0
                    current_room = rooms[current_room_no]
                    player.rect.x = 0 #refrenced this equation it was complicated to understand at first
    
            # --- Drawing ---
        screen.fill(BLACK)
    # put in draw rect for mving thing 
        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)
    
        pygame.display.flip() #we learned in class 
    
        clock.tick(60)
 
    pygame.quit()
 
if __name__ == "__main__":
    main()


    



   

  
        




