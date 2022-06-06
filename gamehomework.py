#Zara Paul 
#Guess a Word Game 

#Psuedocode 
#Start 
#Get instructions, make them pretty 
#Process: print("Instructions"... "******"..... etc.)
#Get os, and random, 
#Process: Import os, Import Random 
#Get randomizer and "insert guess here", make sure randomizer supports the lowercase entries 
#Process thislist= ["Pink", "Pink", "Pink", "Pink", "Pink", "Pink", "Pink"] #do 10 colors  
#word= random.choice(thislist) #chooses complete random element
#Get loop to make sure program will run 8 times 
#Process for(i)in range (8): 
#Get borders, spacing, titles, etc. 
#Process: print("-----------" "Guess 1,2,3,4,5" etc...) DO guess i+1 to add a number to the guess each time. 
# Get something that inputs the color and gives a hint 
# Process: guess = input ("Input a color:") The hint is that it is a color!!
#Get answers and possible outcomes 
#Process Get words used (colors) and if true and false 
#Get If answer is correct print _______
#Process if statement 
#Get If answer is not correct print _____
#Process else statement 
#Get last guess to reveal answer (guess 8)
#Elif i==7: print("The word was", word)
#get out of code if answer is true any of the times 
#Process: "break" Code 
#End

import random #For random generator 
import os
os.system('clear')

print("**********************************************************************") #Making it pretty 
print("----------------------------------------------------------------------")#Making it pretty 
print("                      Guess The Word Game!")
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


thislist= ["Pink", "Blue", "Red", "Green", "Orange", "Yellow", "Purple", "Magenta", "Gray","Black"] #do 10 colors 
word= random.choice(thislist) #chooses complete random element
loop=False  #So doesn't repeat

for(i)in range (8): #Running loop so I don't have to code each guess individually 
    print()#Making it pretty 
    print("---------------------------------------------------------------------")#Making it pretty 
    print("                            GUESS #", i+1) #Guess ___ and will add a number with each guess 
    print("---------------------------------------------------------------------")#Making it pretty 
    print()#Making it pretty 
    guess = input ("Input a color:") #So user can input their word, also giving a hint that the word is a color 

    print()#Making it pretty 
    print("**********************************************************************")#Making it pretty 
    print()#Making it pretty 
    if guess.lower() == word.lower(): #is this correct 
        print( "Answer is correct!") #If answer is correct, display to players 
        print()#Making it pretty 
        print("CONGRATS!!! YOU DID IT!!!") #Extra motivation to players 
        print()#Making it pretty 
        print("**********************************************************************")#Making it pretty 
        break #breaks out of the code if true, stops loop 
    elif i==7: #When it is the last guess, this will happen ELIF is an else with conditions 
        print("The word was", word) #
        print()#Making it pretty 
        print("You didn't guess it!!!")
        print()#Making it pretty 
        print(" ----------                -----------")
        print()
        print('                     ** ')                                 #I TRIED TO MAKE A BIG SAD FACE!!!! 
        print('                 **      ** ') 
        print('             **               ** ') 
        print('         **                      **')
        print('      **                            **  ')
        print('   **                                 **' )
        print(' **                                     **')
        print("**                                        **")
        print()
        print("**********************************************************************")#Making it pretty 
    else:
        print ("Sorry, you didn't guess the word. Guess again!") #telling players to guess again if they got it wrong, code will continue 
        print()#Making it pretty 
        print("**********************************************************************")#Making it pretty 
        print()#Making it pretty 
        
