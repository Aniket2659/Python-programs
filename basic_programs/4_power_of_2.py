power=int(input('enter a power :')) # take input from user
if 0<=power<=31: # check the condition
    for i in range(power+1): # use for loop to iterate 0 to power
        print(f'2 * {i} ={2**i}') # use fstring to print table