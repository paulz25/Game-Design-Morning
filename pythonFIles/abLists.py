#Zara Paul
#We are going to learn about lists, and functions related to lists 
#We are going to learn abt fr lp (four loop)
import random #psuedo random numbers 
import os
os.system('clear')

thislist=["apple", "bannana", "cherry", "orange", "kiwi", "melon", "mango"]
#            0          1       2           3        4       5       6
#                                          -4         -3      -2     -1
print(thislist[1]) #print from a specfifc index
print(thislist[-1]) #print from the end 
print(thislist[2:5]) # print from two value the first one is included in the set the second is excluded 
print(thislist[:3]) #print up to a value but not including a value
print(thislist[2:]) #prints eevrything after a value including the original element 
print(thislist[-4:-1])

if "apple" in thislist:
    print("yes the apple is in the list")
#loops 
for num in range(10): # loops a specific number of times 
    print(num)

for element in thislist: # element= thislist[times run through the loop]
    print(element, end = "")
print()

print(thislist[0:]) #add watermelon/ add an element 

for num in range(10):
    thislist.append(input("input a food"))
print(thislist[0:]) 

thislist.insert(1, "watermelon") #ADDING A ELEMENT TO A SPECIFIC INDEX INSERT (INDEX, ELEMENT you wantto add)
print(thislist[0:])

for i in range(len(thislist)): #length and loop for list 
    print(thislist [i], end = "/")
print()

#extending is adding elements 

list_num = [1, 2, 3, 4]
list_num.extend(thislist) #adds two list 
print(list_num) 

list_num.append(thislist) #creating list inside of a list 
print(list_num) 
print(list_num[-1]) # print the last element 
print(list_num[-1][0]) # print a element in an element if that element is ia list [0, 1, 2, 3,[list 2]], 

for i in range(5):
    word= random.choice(thislist) #chooses complete random element 
print(word) 

guess = input ("input a food") 
if guess.lower in word.lower:
    print("congrats you guessed the food")









