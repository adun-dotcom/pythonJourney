#list is a value that contains multiple values in an ordered sequence.
number = [23, 67, 2, 5, 69, 30]                 #list of values assigned to number
name = ['mike', 'jake', 'charlie', 'tim', 'dave', 'jane']       #list of values assigned to name
print(name[2] + ' is ' + str(number[5]) + ' years old.')       

#list can be contained in other list

spam =[['cat', 'dog', 'bat'], [4, 80, 57, 'figo', 'ayo'], [10, 45, 100, 5, 6, 9]]      #This list contains 3 lists
print(spam[1] [4])      
print(spam[2] [2])
print(spam[1] [2])

#Negative indexes
animals = ['cat', 'bat', 'rat', 'elephant']
print('The ' + animals[-4] + ' is ' + 'afraid ' + ' of the ' + animals[-1] + '.')

#Getting sublist with slices
animals = ['cat', 'bat', 'rat', 'elephant', 'goat']
print(animals[1:3])
animals[1:4] = ['snake', 'fox', 'antelope']
print(animals)

name = ['mike', 'jake', 'charlie', 'tim', 'dave', 'jane'] 
print(name[:5])                 #This is a shortcut that leaves out the first index or the begining of the list but starts the slice from 0
print(name[3:])                 #This is a shortcut that leaves out the second index  of the list but ends the slice at the end of the list
print(name[:])                  #This is a shortcut that slices the list from the begining to the end
print(len(name))                #This gives the lenght of the list

#Changing values in the list with slices 
city = ['lagos', 'abuja','kano','benin', 'jos', 'ilorin', 'ibadan', 'owerri']
city[2] = 'auchi'           #This switches the value in index 2 which is kano to auchi
print(city)

city[3] = city[5]           #This makes the value in index 3 same with index 5
print(city)
city[-1] = 'Bida'
print(city)


#List Concatenation and List Replication
new_list = animals + city               #This adds both list together to form a new list
print(new_list)

new_list = (new_list + name)
print(new_list)

city = ['lagos', 'abuja','kano','benin', 'jos', 'ilorin', 'ibadan', 'owerri'] 
new_city = city * 3                 #This replicates the list 3 times
print(new_city)

#Removing Values from Lists with del Statements

city = ['lagos', 'abuja','kano','benin', 'jos', 'ilorin', 'ibadan', 'owerri'] 
del(city[2])            # this removes the value at index 2 from the list 
print(city)

#list(function)
x = ('Hello World')
list(x)
print(list(x))















