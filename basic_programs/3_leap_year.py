year=int(input('enter a year :')) # take a input from user
digit=len(str(year)) # use len and string to calculate the length of number
if digit==4: # year should be 4 digit
    if (year%4==0 and year%100!=0) or year%400==0:  # use these 3 conditions
        print('year is a leap year')
    else:
        print('year is not a leap year')



