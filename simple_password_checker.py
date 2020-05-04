username = input('what is your username?')
password = input('what is your password?')

password_lenght = len(password)
hidden_password = '*' * password_lenght 


print(f'{username}, your password is {hidden_password} and it is {password_lenght} letters long.')