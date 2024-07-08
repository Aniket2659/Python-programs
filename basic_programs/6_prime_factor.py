num=int(input('enter a number :')) # take a input from user
a=num # use for constant value
while num%2==0: # to check divided by 2
    print(2)
    num=num/2 # update it
for i in range(3,((a-1)),2): # it is for odd value
    while num%i==0: # for duplicacy
        print(i)
        num=num/i # update again