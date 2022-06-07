import random
import os
from secrets import choice
from tabnanny import check 

os.system ('cls')
from time import sleep
seconds=.5

list = ["coral","scallop","sea urchin","oyster","mussel","cockle","clam","geoduck","abelone","ostrea"]
count = 0
Game = True
theword = ""

def hint(): # allows us to reuse code in multiple spots
    global count
    if count == 0:
        print("|*************************************|")
        print("|         Here is a new hint          |")
        print("|These creatures all have a hard shell|")
        print("|        only 2 shells in fact        |")
        print("|*************************************|")
        
    elif count == 1:
        print("|**************************************|")
        print("|       Here is your final hint        |")
        print("|  These creatures almost never move   |")
        print("|**************************************|")
    
    else:
        print("You are horrible at guessing, no more hints, go till you get it right")

while Game:
    print("|***************************************|")
    print("|         Guess The Animal!!!           |")
    print("|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|")
    print("| 1. Colors                             |")
    print("| 2. Fruits                             |")
    print("| 3. Animals                            |")
    print("|First we will provide you with one hint|")
    print("|           !Your Hint Is!              |")
    print("|  These animals are big fans of water  |")
    print("|***************************************|")

    theword=random.choice(list)
    name = input("What is your name? ")
    print(name, end = ", ")
    answer = input("would you like to play the game? ")
    answer = answer.lower()
    if 'n' in answer:
        Game = False
        break

    while True:
        choice = input("What game would you like to play 1,2, or 3? ")
        try:
            choice = int(choice)
            if choice > 0 and choice < 4:
                break
            else:
                print("give me 1,2, or 3")
        except:
            print("Plese enter a number")

def option1():
    global count 
    os.system("clear")
    check= True
    count= 0 
    list= ["Pink", "Blue", "Red", "Green", "Orange", "Yellow", "Purple", "Magenta", "Gray","Black"]
    theword=random.choice(list)
    while check and count <5:
        guess=input("Put Guess here")
        if guess == theword:
            print("congrats, you got it")
            check = False 
        else:
            print("you failed!!!")
            print("             *                    *  ")
            print()
            print("                      . . .")          
            print('                     .      .')                                 #I TRIED TO MAKE A BIG SAD FACE!!!! 
            print('                   .         .') 
            print('                 .             .') 
            print('                .               .')
            print('               .                 .')
            print('              .                   .' )
            print('             .                     .')
            print("            .                       .")
        count += 1

    def option2():
        global count 
    os.system("clear")
    check= True
    count= 0 
    list= ["Pig", "Dog", "Cat", "Bird", "Fish", "Cow", "Penguin", "Monkey", "Flamingo","Giraffe"]
    theword=random.choice(list)
    while check and count <5:
        guess=input("Put Guess here")
        if guess == theword:
            print("congrats, you got it")
            check = False 
        else:
            print("you failed!!!")
            print("             *                    *  ")
            print()
            print("                      . . .")          
            print('                     .      .')                                 #I TRIED TO MAKE A BIG SAD FACE!!!! 
            print('                   .         .') 
            print('                 .             .') 
            print('                .               .')
            print('               .                 .')
            print('              .                   .' )
            print('             .                     .')
            print("            .                       .")
        count += 1

def option3():
    global count 
    os.system("clear")
    check= True
    count= 0 
    list= ["Apple", "Orange", "Bannana", "Blueberry", "Strawberry", "Blackberry", "Raspberry", "Cherry", "Watermelon","Mango"]
    theword=random.choice(list)
    while check and count <5:
        guess=input("Put Guess here")
        if guess == theword:
            print("congrats, you got it")
            check = False 
        else:
            print("you failed!!!")
            print("             *                    *  ")
            print()
            print("                      . . .")          
            print('                     .      .')                                 #I TRIED TO MAKE A BIG SAD FACE!!!! 
            print('                   .         .') 
            print('                 .             .') 
            print('                .               .')
            print('               .                 .')
            print('              .                   .' )
            print('             .                     .')
            print("            .                       .")
        count += 1
        

    os.system('cls')
    answer = input("Do you want to play again? ")
    if ('n' or 'N') in answer:
        Game = False
        print("Thank you for playing")




