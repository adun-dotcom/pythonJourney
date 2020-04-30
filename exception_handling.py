#Errors can be handled with try and except statments

print('How many cats do you have?')     #ask for the number of cat
numCats = input()                      #collects the number of cats
try:                                    # the try/except statement handles the error if a value that is not an integer is given as the number of cats.
    if int(numCats) >= 5:
        print('Wow you have a lot of cats.')
    else:
        print('You just have few cats.')
except ValueError:
 print('You did not enter a number')