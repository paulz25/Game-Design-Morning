from ctypes.wintypes import WORD
import random
import os 

os.system ('clear')
import datetime
from time import sleep
seconds=.5
#psuedocde for adding a score
#get lists
#list..=_
#Game=true 
#get file qnd define it 
#def file_ 
#open the file 
#file=open/close
#fernandos code so already hints 
#add the number 
#get the score and add in 
#200-40 , etc. etc. 
#open file with that and append the file 
#end 



theWord=""

list1 = ["coral","scallop","sea urchin","oyster","mussel","cockle","clam","geoduck","abelone","ostrea"]
list2 = ["apple","kiwi",'Banana']
list3 = ["CPU","RAM", "ROM"]

Game=True
cnt=0
def FileR():
    myFile=open("scre.txt", 'r')
    for line in myFile.readlines():
        print(line)
    myFile.close()
#a function is a section  the prram that we call when we need it
def hint():
    global cnt     #allow us to modify the variable all over the program
    if cnt ==0:
        print("|*************************************|")
        print("|         Here is a new hint          |")
        print("|These creatures all have a hard shell|")
        print("|        only 2 shells in fact        |")
        print("|*************************************|")
        

    # guess2 = input("plese put your new guess here: ")
    # if guess2 == theword:
    #     print("Congrats, You got it")
    # else:
    #     print("wrong again, you are pretty bad at this, try again")
    elif cnt ==1:     #else if
        print("|**************************************|")
        print("|       Here is your final hint        |")
        print("|  These creatures almost never move   |")
        print("|**************************************|")

    else:
        print("You are horrible at guessing, no more hints, go till you get it right")
    
    print()
def selectWrd(choice):  #is a function with a parameter
    global theWord
    if choice ==1:
        theWord= random.choice(list1)    
    if choice ==2:
        theWord= random.choice(list2)
    if choice ==3:
        theWord= random.choice(list3)
    return theWord  
name=input("What is your name? ")
high=0 #tfind highest score
while Game:
    
    print("|***************************************|")
    print("|         Guessing  Game   !!           |")
    print("|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|")
    print("|          1.animals                    |")
    print("|          2.Fruits                     |")
    print("|          3. Cputer parts              |")
    print("|          4. see high score            |")
    print("|First we will provide you with one hint|")
    print("|           !Your Hint Is!              |")
    print("|  These animals are big fans of water  |")
    print("|***************************************|")
# add user name, make it more personal y will need for keeping score
    
    print(name, end=", ")
    answer=input("Would you like to play? ")
    if 'n' in answer:
        break
    while True:
        choice=input("What game would y like to play 1, 2, 3, or 4")
        #preventing error we use try and except
        try:
            choice=int(choice)
            if choice>0 and choice <5:
                break
            else:
                print("give me 1,2,3, or 4")
        except:
            print("sorry")
    if choice== 4:
        FileR()
    theWord = selectWrd(choice) #call to a function that will return a value
    #call function to select the word from the right list
    os.system('clear')
    check=True
    while check and cnt <5 and choice!=4: 
        guess=input("plese put your guess here: ")
        print()
        if guess == theWord:
            print("Congrats, You got it")
            check=False
        else:
            hint()
        cnt+=1   # cnt= cnt + 1
        if cnt ==5:
            print("Sorry!" )
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


os.system('clear')
date=datetime.datetime.now() #todays date and time
screLine= str(score) + "\t"+name+"\t"+ (date.strftime("%m/%d/%Y"))+"\n" #\n is enter \t is tab 
myFile=open("scre.txt", 'a') #open a file to write it clear the file if it exists 
myFile.write(screLine)
myFile.close() 

