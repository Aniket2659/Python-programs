harmonic_value=int(input('enter a harmonic value :')) # take input from user
sum=0 # initialize sum is equal to zero
for i in range(1,harmonic_value+1): # use loop to calculate teh total sum
    sum=(1/i)+sum
print(f'the Nth harmonic number is {round(sum,2)}')