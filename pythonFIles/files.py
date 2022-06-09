#zara paul 
# Files"
# append = a 
# read = r 
# write = w 

#open files make sure you close

import os, datetime

os.system('clear')
name="Zara"
score=120
date=datetime.datetime.now() #todays date and time
print(date.strftime("%m/%d/%Y")) #you can switch order around too 
screLine= str(score) + "\t"+name+"\t"+ (date.strftime("%m/%d/%Y")) 
print(screLine) #make like a scoreboard 
#to open a file we must create an object 
myFile=open("scre.txt", 'w') #open a file to write it clear the file if it exists 
myFile.write(screLine)
myFile.close()
myFile=open("scre.txt", 'a') #open a file to write it clear the file if it exists 
myFile.write(screLine)
myFile.close()
myFile=open("scre.txt", 'r') #open a file to read
#lines=myFile.readlines()
print()
for line in myFile.readlines():
    print(line)
myFile.close()

