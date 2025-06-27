'''
Given an array of N numbers from 1 to N, find the missing number in the array
'''

#BRUTE

def missing_number(arr,n):
    for i in range(1,n+1):
        flag=0
        for j in range(0,n-1):
            if arr[j] == i:
                flag=1
                break

        if flag == 0:
            return i
        

#Better

def missing_number_better(arr,n):
    hasharr=[0 for _ in range(0,n+1)]

    for i in range(0,n-1):
        hasharr[arr[i]] = 1
    
    for i in range(1,len(hasharr)):
        if hasharr[i] == 0:
            return i


#Optimal 1

def missing_number_optimal1(arr,n):
    n_sum = (n*(n+1))/2
    arr_sum = 0

    for i in range(0,n-1):
        arr_sum += arr[i]

    return int(n_sum - arr_sum)

def missing_number_optimal2(arr,n):
    xor1,xor2=0,0
    for i in range(0,n-1):
        xor2 = xor2 ^ arr[i]
        xor1 = xor1 ^ (i+1)

    xor1 = xor1 ^ n
    return xor1 ^ xor2

'''
XOR approach is better because, as the no. becomes larger, int cannot hold it and overflows to long which take slightly more space. Hence xor has a slight adv than sum
'''

N = 5
a = [1, 2, 4, 5]
ans = missing_number_optimal2(a, N)
print("The missing number is:", ans)