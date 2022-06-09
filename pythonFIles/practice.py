#zara paul 
#we are going to learn about strings or ' ' " "
import os
os.system ('clear')
print( 'Hi' )
print ( "hi" )
print ("hello let's go to the park")
message="you are awesome" #a string is an array of characters 
#  0   1   2   3   4   5  ALL arrays begin on zero 
# H   E   L   L    O 
print(message)
print(message [5]) #print the letter in position 5
print(message [0:5]) #print all letters from position 0-4 (5 characters) 
if message.isdigit(): #isdigit is a method you must use it with a dot
    sum=message +3 #if the statement is true 
else:       #if it is false 
    print(message+" I say so") #concentation
print(message.upper())
print(message)
if message.upper():
    print(message)
else:
    # print("i am in false") use only for debugging I will delete or com when I am done 
    message=message.upper()
    print(message)
print(type(message)) # type out 
print(dir(message)) #what is dir 

