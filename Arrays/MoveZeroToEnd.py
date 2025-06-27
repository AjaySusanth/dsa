#Brute
'''
Store all non zero in temp and place fill the remaining pos with zero
'''

def brute(arr,n):
    temp = []
    for i in range(n):
        if (arr[i]!=0):
            temp.append(arr[i])

    for i in range(len(temp)):
        arr[i] = temp[i]

    for i in range(len(temp),n):
        arr[i]=0

    print(arr)


#Optimal
'''
Find the first zero elt pos and point to it.
Start iteration from its next pos and swap non-zero elt with that pos and inc the pointer

'''

def optimal(arr,n):
    j=-1
    for i in range(n):
        if arr[i]==0:
            j=i
            break

    if j==-1:
        print('No zero')
    for i in range(j+1,n):
        if arr[i]!=0:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
        
    print(arr)


arr=[1,0,2,4,0,5,0]
n=7


optimal(arr,n)