
def add(x,y):
    return x + y

def Subraction(x,y):
    return x - y 

def Multiplication(x,y):
    return x * y

def Division(x,y):
    return x / y

operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

num_1 = float(input('Enter your first number: '))
num_2 = float(input('Enter your second number: '))


if operation == '+':
    print('{} + {} = '.format(num_1,num_2))
    print(num_1 + num_2)

elif operation == '-':
    print('{} - {} = ' .format(num_1, num_2))
    print(num_1 - num_2)
    
elif operation == '*':
    print('{} * {} = ' .format(num_1, num_2))
    print(num_1 * num_2)

elif operation == '/':
    print('{} / {} = '.format(num_1, num_2))
    print(num_1 / num_2)

else:
    print('You selected an invalid operator, please run the program again.')