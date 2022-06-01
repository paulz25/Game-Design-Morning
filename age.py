#Zara Paul 
#Calculate age
#get user year and current year 
import os #library clear screen 
os. system('clear')
by=2001 #assign this value as a number 
#by=2001 #this is a number  #input('year you were born, ') give us a string
by= int( input ('year you were born,'))
currentYear=2022 #also number 
age =currentYear-by 
print('Your age is ',age)
#selection
if age >50: 
    print('You are old')