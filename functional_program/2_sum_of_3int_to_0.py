
def three_sum(arr): # use threesum function with arr parameter
    li=[]            # create an empty list 
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)): # use 3 nested loop 
                if arr[i]+arr[j]+arr[k]==0:
                    
                    li.append([arr[i],arr[j],arr[k]]) # append to list
    return li
ar=[1,5,-1,0,-2,-3,-5]
print(three_sum(ar))
