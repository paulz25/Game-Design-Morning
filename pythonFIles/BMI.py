#zara paul 
#BMI Code 
import os # makes everything look nicer 
os. system ('clear') #you always put after import os 
x = 60 #inputed weight in kg
y = 1.75 #inputed height in meters
BMI = x/(y*y) #height squared times weight 
print (BMI) #final answer 
if (BMI <= 18.5):
    print ("you are underweight")
if (BMI >= 25):
    print ("you are overweight")
if (BMI > 18.5 and BMI < 25):
    print ("you are healthy")

