#Zara Paul
#This is a string practice 
import os
os.system('clear')
#Create a string made of the first, middle and last character
string1= "James"
print(string1[0],end= '')
print(string1[int(len(string1)/2)],end= '')
print(string1[len(string1)-1])

#Write a program to create a new string made of the middle three characters of an input string.
#JhonDipPeta
#want Dip
string1= "JhonDipPeta" #both cases work 

print(string1[int(len(string1)/2)-1], end = "")
print(string1[int(len(string1)/2)], end = "")
print(string1[int(len(string1)/2)+1])

#JaSonAy output Son
string1= "JaSonAy"
# print(string1[(int(len(string1)/2)-1):(int(len(string1)/2) + 2)]) 
print(string1[int(len(string1)/2)-1], end = "")
print(string1[int(len(string1)/2)], end = "")
print(string1[int(len(string1)/2)+1])

#append strin in the middle of a given string
# s1= "ault" 
# s2= "kelly"
#create "aultkellylt"

s1 = "ault"
s2 = "kelly"

word =s1[0:int(len(s1)/2)] + s2 + s1[int(len(s1)/2):int(len(s1))]
print(word)

s1 = "ault"
s2 = "kelly"

message= s1[0:2] + s2 + s1[2:]
print(message)
  
#Given two strings,s1ands2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
#expected turnout is AJrpan

s1 = "America"
s2 = "Japan"

word = s1[0] + s2[0] + s1[int(len(s1)/2)] + s2[int(len(s1)/2-1)] + s1[int(len(s1)-1)] + s2[int(len(s2)-1)]
print(word)

message= s1[0] + s2[0] + s1[3] + s2[2:]
print(message)

word = s1[0] + s2[0] + s1[int(len(s1)/2)] + s2[int(len(s1)/2-1)] + s1[int(len(s1)-1)] + s2[int(len(s2)-1)]
print(word)



# Arrange string characters such that lowercase letters should come firstGiven string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
# give  Pynative 
# re- aarrange to yaivePNT 

message= "PyNaTive"
print(message[1],end="")
print(message[3],end="")
print(message[5:8],end="")
print(message[0],end="")
print(message[2],end="")
print(message[4]) 









