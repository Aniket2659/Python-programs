import random # import random module to take random elements between 0 to 1
no_trial=abs(int(input('how many time you want to flip the coin :'))) # take input from user
li=[round(random.random(),2) for i in range(no_trial)] # use list comprehension to store value in list and for loop to take 10 value
tail=0 # initialize with zero to count the no of heads and tails
head=0
for j in li: # use for loop for itaration in list
    if j>0.5: # use if,else condition for given condition
        head+=1
    else:
        tail+=1
print(li)
print(f'percentage of head is {(head/no_trial)*100}%')
print(f'percentage of tail is {(tail/no_trial)*100}%')



