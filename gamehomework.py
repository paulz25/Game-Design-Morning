#Zara Paul 
#Guess a Word Game 




#Psuedocode 
#Start 
#Get instructions, make them pretty 
#Process: print("Instructions"... "******"..... etc.)
#Get os, and random, 
#Process: Import os, Import Random 
#Get borders, spacing, titles, etc. 
#Process: print("-----------" "Guess 1,2,3,4,5" etc...)
#Get randomizer and "insert guess here", make sure randomizer supports the upper and lowercase entries 
#Process
#Get answers and possible outcomes 
#Process
#Get If answer is correct print _______
#Process
#Get If answer is not correct print _____
#Process
#Repeat if answer is not correct x4, on last one display correct answer 
#End




import random #For random generator 
import os
os.system('clear')

print("**********************************************************************")
print("----------------------------------------------------------------------")
print("                      Guess The Word Game!")
print("----------------------------------------------------------------------")
print("***************************INSTRUCTIONS*******************************")
print("----------------------------------------------------------------------")
print("1) The game will generate a word.")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("2) You will have to guess what the word is.")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("3) Input your guesses in the game, it will tell you if any are correct.")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("4) You will get hints until you guess the word.")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print("5) But, you only have 5 tries to guess.....")
print("---------------------------------------------------------------------")
print("                      Will you succeed?")
print("**********************************************************************")
print("                    ")
print("                    ")
print("                    ")
print("                    ")


thislist= ["Pink", "Pink", "Pink", "Pink", "Pink", "Pink", "Pink"] #do 10 colors 
word= random.choice(thislist) #chooses complete random element
loop=False  

# for(i)in range (5):





print("                            ")
print("---------------------------------------------------------------------")
print("                            GUESS #1")
print("---------------------------------------------------------------------")
print("                            ")
guess = input ("Input a guess:") 

print("                            ")
print("**********************************************************************")
print("                            ")
if guess.lower() == word.lower(): #is this correct 
    print( "Answer is correct!")
    print("                            ")
    print("CONGRATS!!! YOU DID IT!!!")
    print("                            ")
    print("Play Again?")
    print("                            ")
    print("**********************************************************************")
else:
    print ("Sorry, you didn't guess the word. Guess again!")
    print("                            ")
    print("**********************************************************************")
    print("                            ")
    print("Hint: This word is a color")
    print("                            ")
    print("---------------------------------------------------------------------")
    print("                            GUESS #2")
    print("---------------------------------------------------------------------")
    print("                            ")
    hi= input("Guess any word here:")

    print("                            ")
    print("**********************************************************************")
    print("                            ")

    if hi is word:
        print( "Answer is correct!")
        print("                            ")
        print("CONGRATS!!! YOU DID IT!!!")
        print("                            ")
        print("Play Again?")
        print("                            ")
        print("**********************************************************************")
    else:
        print ("Sorry, you didn't guess the word. Guess again!")
        print("                            ")
        print("**********************************************************************")
        print("                            ")
        print("Hint: This word is a color") #if word is blue print..... #how do you make it until user does not want to play anymore, send email and ask if mine is okay 

        print("                            ")
        print("---------------------------------------------------------------------")
        print("                            GUESS #3")
        print("---------------------------------------------------------------------")
        print("                            ")
        hi= input("Guess any word here:")

        print("                            ")
        print("**********************************************************************")
        print("                            ")

        if hi is word:
            print( "Answer is correct!")
            print("                            ")
            print("CONGRATS!!! YOU DID IT!!!")
            print("                            ")
            print("Play Again?")
            print("                            ")
            print("**********************************************************************")
        else:
            print ("Sorry, you didn't guess the word. Guess again!")
            print("                            ")
            print("**********************************************************************")
            print("                            ")
            print("Hint: This word is a color")

            print("                            ")
            print("---------------------------------------------------------------------")
            print("                            GUESS #4")
            print("---------------------------------------------------------------------")
            print("                            ")
            hi= input("Guess any word here:")

            print("                            ")
            print("**********************************************************************")
            print("                            ")

            if hi is word:
                print( "Answer is correct!")
                print("                            ")
                print("CONGRATS!!! YOU DID IT!!!")
                print("                            ")
                print("Play Again?")
                print("                            ")
                print("**********************************************************************")
            else:
                print ("Sorry, you didn't guess the word. Guess again!")
                print("                            ")
                print("**********************************************************************")
                print("                            ")
                print("Hint: This word is a color")
                print("                            ")
                print("---------------------------------------------------------------------")
                print("                            GUESS #5")
                print("---------------------------------------------------------------------")
                print("                            ")

            hi= input("Guess any word here:")

            print("                            ")
            print("**********************************************************************")
            print("                            ")

            if hi is word:
                print( "Answer is correct!")
                print("                            ")
                print("CONGRATS!!! YOU DID IT!!!")
                print("                            ")
                print("Play Again?")
                print("                            ")
                print("**********************************************************************")
                
            else:
                print ("Sorry, you didn't guess the word!")
                print("                            ")
                print ("You lost the game.. try again next time")
                print("                            ")
                print("**********************************************************************")
                print("                            ")
                print("The word was:")
                print (word)
                print("                            ")
                print("**********************************************************************")