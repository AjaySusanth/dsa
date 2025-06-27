#Reverse the array

# Brute

def reverse_brute(arr):
    rev = []

    for i in range(len(arr)-1,-1,-1):
        rev.append(arr[i])

    for i in range(0,len(rev)):
        arr[i] = rev[i]

    print(arr)

#Optimal (2 pointer approach)


def reverse_optimal(arr):
    i,j=0,len(arr)-1

    while i<j:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1
    print(arr)
    
# TC - o(n)  sc- o(1)

arr = [1,2,3,4,5]
reverse_optimal(arr)
reverse_brute(arr)

# TC - O(2n) SC - O(n)



