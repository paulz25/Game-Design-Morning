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
import os
os.system('clear')
from secrets import choice
from tabnanny import check 
from time import sleep
#Print menu options 



os.system ('cls')
seconds=.5

list = ["coral","scallop","sea urchin","oyster","mussel","cockle","clam","geoduck","abelone","ostrea"]
count = 0
Game = True
theword = ""





while Game:
        print("**********************************************************************") #Making it pretty 
        print("----------------------------------------------------------------------")#Making it pretty 
        print("                      Guess The Word Game!")
        print("----------------------------------------------------------------------")#Making it pretty 
        print("**********************************************************************") #Making it pretty 
        print("FIRST SELECT GAME MODE")
        print("1) Colors")
        print("2) Fruits")
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
        print("5) But, you only have 8 tries to guess.....")
        print("---------------------------------------------------------------------")#Making it pretty 
        print("                      Will you succeed?")
        print("**********************************************************************")#Making it pretty 
        print()
        print()
        print()
        print()

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
    answer = input("Do you want to play again? ") #
    if ('n' or 'N') in answer:
        Game = False
        print("Thank you for playing")
       



