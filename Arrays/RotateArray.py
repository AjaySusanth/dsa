#Left Rotate Array by one place

def left_rotate(arr,n):
    temp = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = temp

    print(arr)

#Left Rotate Array by 'd' place

#Brute
'''
def l_rotate_brute(arr,n,d):
    temp = arr[0:d]
    for i in range(d,n):
        arr[i-d] = arr[i]

    j=0
    for k in range(d+1,n):
        arr[k] = temp[j]
        j+=1

    print(arr)
'''
def l_rotate_brute(arr,n,d):
    temp = arr[0:d]
    for i in range(d,n):
        arr[i-d] = arr[i]

    for i in range(n-d,n):
        arr[i] = temp[i-(n-d)]

    print(arr)

#Optimal

def l_rotate_optimal(arr,n,d):
    arr[0:d] = arr[0:d][::-1] #reverse first d places
    arr[d:n] = arr[d:n][::-1] #reverse remaining elts
    arr[0:n] = arr[0:n][::-1] #reverse the entire arr
    print(arr)




n = 5
arr = [1, 2, 3, 4, 5]
#left_rotate(arr,n)

l_rotate_optimal(arr,n,2)