#Brute Force
'''
Add the elements to a set
Modify the existing arr by the elements in the set

'''
def removeDuplicates(arr):
    unique = set()
    for i in arr:
        unique.add(i)
    index=0
    for i in unique:
        arr[index] = i
        index +=1

    return index

#Optimal

def optimal(arr):
    i=0
    for j in range(1,len(arr)):
        if arr[j]!=arr[i]:
            i+=1
            arr[i] = arr[j]

    return i+1

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 3]
    k = optimal(arr)
    print("The array after removing duplicate elements is ")
    for i in range(k):
        print(arr[i], end=" ")