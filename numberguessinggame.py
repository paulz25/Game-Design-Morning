#Zara Paul 
#Guessing a number game 
#Psuedocode 
#Print “hello welcome to the number guessing game” 
#Print “there are three levels to this game” 
#Print”instructions”
# level one 
#Random_number1= random.radiant(1,25)
#print(welcome to level 1) 
#print(rules) 
#While number_of_guesses <5:
		#Input number_guess=random number 
			#Break 
		#Elif number guess <5:
			#“Print the number is higher”
		#Elif number guess > random_number 1:
			#“Print the random number is lower” 
#If number_guess == random number1:
#Print “you are correct! The random number was “ + str(random_number1) +!
#Else: 
#Print “sorry you are not correct. The random  number was” + str(random_number1) + !

#Level #2 repeat code with levels 1-50 
#Level #3 repeat code with levels 1-100
#Put file rpinting below it 
#open files for instructions 
#open files for high score 
#be able to break 
#ask if wants to play again 
# end


import random
import os
from unicodedata import name 
os.system("clear")
import datetime
count=0 
Game=True
score=0 
high=0
cnt=5


def option1():
    myFile=open("Instructions.for.Number.Guessing.Game.txt", 'r') #open a file to read
    #lines=myFile.readlines()
    print()
    for line in myFile.readlines():
        print(line)
    myFile.close()

game=True
def option2():
    global count 
    os.system('clear')
    check = True 
    count= 0 
    number= random.randint (1,25)
    print("welcome to level 1!")
    count=0 
    while check and count < 5:
        guess=int(input("please put your number guess here"))
        if guess < number:
            print("That is not the right number, the number is larger!")
        if guess > number:
            print("That is not the right number, the number is smaller!")
        if guess == number:
            print("You guessed the number! YAY!")
        else:
            count+=1
    return count 


def option3():
    global count 
    os.system('clear')
    check = True 
    count= 0 
    number= random.randint (1,50)
    print("welcome to level 1!")
    count=0 
    while check and count < 5:
        guess=int(input("please put your number guess here"))
        if guess < number:
            print("That is not the right number, the number is larger!")
        if guess > number:
            print("That is not the right number, the number is smaller!")
        if guess == number:
            print("You guessed the number! YAY!")
        else:
            count+=1
    return count 

def option4():
    global count 
    os.system('clear')
    check = True 
    count= 0 
    number= random.randint (1,100)
    print("welcome to level 1!")
    count=0 
    while check and count < 5:
        guess=input(int("please put your number guess here"))
        if guess < number:
            print("That is not the right number, the number is larger!")
        if guess > number:
            print("That is not the right number, the number is smaller!")
        if guess == number:
            print("You guessed the number! YAY!")
        else:
            count+=1
    return count 



def option5():
    myFile=open("Score.for.Number.Guessing.Game.txt", 'r')
    for line in myFile.readlines():
        print(line)
    myFile.close()
    




#for 6 if user selects option 6 then break 

name=input("What is your name? ")

while Game: 
    print(name, end=", ")
    answer=input("Would you like to play? ")
    if 'n' in answer:
        break
    print(" Menu ")
    print("Challenges:")
    print("1) Instruction")
    print("2) Guess numbers between 1-25")
    print("3) Guess numbers between 1-50")
    print("4) Guess numbers between 1-100")
    print("5) Print score")
    print("6) Exit")

    while True:
        choice=input("Select option 1,2,3,4,5,6: ")
        try: 
            choice=int(choice)
            if choice >0 and choice<7:
                break
            else: 
                print("give me a 1,2,3,4,5, 0r 6 please!")
        except:
            print("Please enter a number between 1-6")
    if choice==1:
        option1()
    if choice ==2:
        cnt=option2()
    if choice ==3:
        cnt=option3()
    if choice ==4:
        cnt=option4()
    if choice ==5:
        option5()
    if choice ==6:
        break
    score=200-40*cnt
    if score > high:   # find highest sce
        high=score
    print(name+", your score is "+str(score))
    input("Press enter ")
    os.system('clear')
    print("<><><><><><><><><><><><>")
    answer=input("Do yo want to play again? ")
    if ('n' or 'N') in answer:
        Game=False
        print("Thank you for playing my game" )
    
    cnt=0 
    print("your highest score is " + str(high))


#write high score to file here 



os.system('clear')
date=datetime.datetime.now() #todays date and time
screLine= str(score) + "\t"+name+"\t"+ (date.strftime("%m/%d/%Y"))+"\n" #\n is enter \t is tab 
myFile=open("scre.txt", 'a') #open a file to write it clear the file if it exists 
myFile.write(screLine)
myFile.close() 

    




