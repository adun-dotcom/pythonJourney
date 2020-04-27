print('What is your name') #Displays your name

name = input()              #ask for your name 
# if name == 'Alice':
print('Hello',name,'How old are you')
age = int(input())          #ask for your age
if age < 12:
    print(name,'You are a kid')
elif age >= 18:
    print('You are',age,'years old,\nYou are an adult.')

