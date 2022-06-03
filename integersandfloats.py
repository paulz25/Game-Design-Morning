#Zara Paul 
#write code that finds an input number to be even or odd 


import os
os .system('clear')

variable= input('enter a number') #put number in 
variable=int(variable) #number is integer 
num= (variable % 2) #% modulu thing 
print(num) #prints the 1 or the 0 
if num == 0: 
    print ('you are even') 
else:
    print('you are odd') 


if (num%3==0):
    print ("number is a multiple of 3" )
else:
    print ("number is not a multiple of 3")

if (num%5==0):
    print ("number is a multiple of 5" )
else:
    print ("number is not a multiple of 5") 
