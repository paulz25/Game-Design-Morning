#Zara Paul 
#Guess a Word Game 

#Psuedocode 
#Start 
#Get instructions, make them pretty 
#Get new menu within instructions
#Process: print("Instructions"... "******"..... etc.)
#Get os, and random, 
#Process: Import os, Import Random 
#Get randomizer and "insert guess here", make sure randomizer supports the lowercase entries 
#Process thislist= ["Pink", "Pink", "Pink", "Pink", "Pink", "Pink", "Pink"] #do 10 colors  
#ask user whihc menu item and their name zndif they would like to play
#Input.(), etc. etc. 
#word= random.choice(thislist) #chooses complete random element 
#Get answers and possible outcomes 
#Process Get words used (colors) and if true and false 
#Get If answer is correct print _______
#Process if statement 
#Get If answer is not correct print _____
#Process else statement 
#print("hint")
#repeat fro 3 ore menu items
#get out of code if answer is true any of the times 
#Process: "break" Code 
#End

import random #For random generator 
import os #importing all the key words 
os.system('clear') #importing all the key words 
from secrets import choice #importing all the key words 
from tabnanny import check #importing all the key words 
from time import sleep #importing all the key words 
#Print menu options 



os.system ('clear') #makes look clean
seconds=.5 

count = 0 
Game = True 
theword = "" #is like an import thing for the word, this is what user inputs 

def option1(): #option 1 is our first option we have on the menu 
    global count #this makes sure it runs to all the code 
    os.system("clear") #makes look clean 
    check= True #starts the loop/guesses 
    count= 0 
    list= ["Pink", "Blue", "Red", "Green", "Orange", "Yellow", "Purple", "Magenta", "Gray","Black"]
    theword=random.choice(list) #imports random 
    while check and count <5: #makes look run thourgh 5 times
        guess=input("Input name of a color:") #for the user to put in the name of something 
        if guess == theword: 
            print("congrats, you got it") #when they get it right 
            check = False  #breaks game if right 
        else: #if wrong 
            print("you failed!!!")
            print("             *                    *  ")
            print()
            print("                      . . .")          
            print('                    .      .')                                 #I TRIED TO MAKE A BIG SAD FACE!!!! 
            print('                   .         .') 
            print('                 .             .') 
            print('                .               .')
            print('               .                 .')
            print('              .                   .' )
            print('             .                     .')
            print("            .                       .")
        count += 1 #happens once in the loop 

def option2(): #comments for all the options will be the same besides the different lists 
    global count 
    os.system("clear") #makes look clean
    check= True
    count= 0 
    list= ["Pig", "Dog", "Cat", "Bird", "Fish", "Cow", "Penguin", "Monkey", "Flamingo","Giraffe"] #aniamls for option 2
    theword=random.choice(list)
    while check and count <5:
        guess=input("Input name of animal: ") #reminds user what they are guessing 
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

def option3(): #comments for all the options will be the same besides the different lists 
    global count 
    os.system("clear") #makes look clean
    check= True
    count= 0 
    list= ["Apple", "Orange", "Bannana", "Blueberry", "Strawberry", "Blackberry", "Raspberry", "Cherry", "Watermelon","Mango"] #fruits fro option 3
    theword=random.choice(list)
    while check and count <5:
        guess=input("Input name of a fruit:") #reminds user what they are guesisng 
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



while Game: #while loop makes sure loop runs and runs and runs 
    os.system('clear') #makes look clean
    print("**********************************************************************") #Making it pretty 
    print("----------------------------------------------------------------------")#Making it pretty 
    print("                      Guess The Word Game!")
    print("----------------------------------------------------------------------")#Making it pretty 
    print("**********************************************************************") #Making it pretty 
    print("FIRST SELECT GAME MODE")
    print("1) Colors")
    print("2) Fruits") #menu 
    print("3) Animals")
    print("----------------------------------------------------------------------")#Making it pretty 
    print("***************************INSTRUCTIONS*******************************")#Making it pretty 
    print("----------------------------------------------------------------------")#Making it pretty 
    print("1) The game will generate a word.")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_")#Making it pretty 
    print("2) You will have to guess what the word is.")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_")#Making it pretty 
    print("3) Input your guesses in the game, it will tell you if any are correct.")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_")#Making it pretty 
    print("4) You will get one hint at the begginning about the category of the word.")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_")#Making it pretty 
    print("5) But, you only have 5 tries to guess.....")
    print("---------------------------------------------------------------------")#Making it pretty 
    print("                      Will you succeed?")
    print("**********************************************************************")#Making it pretty 
    print()
    print()
    print()
    print()
# we put below because if not while loop would try to apply to all 

    name = input("What is your name? ") #making it cute and personal 
    print(name, end = ", ") #makes sure that the name has commas and stuff 
    answer = input("would you like to play the game? ") #asking user 
    answer = answer.lower() #makes sure lowercase is usable
    while 'n' in answer: #no answer 
        Game = False #stops game 
        break #ends code if user doesn't want to play 

    while True: #when the user answers yes:
        choice = input("What game would you like to play 1,2, or 3? ") #asking what game 
        try:
            choice = int(choice) #makes sure choice is a whole number 
            if choice > 0 and choice < 4:
                break #code wont run if this and will print whats on line 175, if integers are within range, it will print 
            else:
                print("give me 1,2, or 3")
        except: #like an elif statement 
            print("Plese enter a number")
    if choice == 1:
        option1() #if users choose option __ then they will recieve that option 
    if choice == 2:
        option2()
    if choice == 3:
        option3() #functions need these thinsgs 
        
    answer = input("Do you want to play again? ") #asks user 
    if ('n' or 'N') in answer:
        Game = False #will stop and print if user says no 
        print("Thank you for playing")


        



