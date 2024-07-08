user=input('enter a username :') # take a username as input
str= "Hello <<UserName>>, How are you?" # assign given string to str variable
if len(user)>=3:
    after_replace=str.replace('<<UserName>>',user)  # use if condition for minimum character condition and store it in variable variable
    print(after_replace)
else:
    print('username should be greater than 3 characters') # print error message if condition is not satisfy

# 2nd way
user=input('enter a username :') # take a username as input
if len(user)>3:
    print(f'Hello {user}, How are you?') # use fstring
else:
    print('username should be greater than 3 characters') # print error message if condition is not

 
