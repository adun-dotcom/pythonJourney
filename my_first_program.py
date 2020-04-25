#This program says hello and asks for my name
print('Hello!')
print('What is your name?')     #Ask for their name 

myName = input()       #This collects their name
print('It\'s good to meet you,' + ' ' + myName)

print('The lenght of your name is:')
print(len(myName))      #Display the lenght of their name

print('What is your age?')      #Ask for their age

myAge = input()     #This collects their age 
print('You will be' + ' ' + str(int(myAge)+1) + ' ' + 'in a year.') 


