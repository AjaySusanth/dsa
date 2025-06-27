#Brute
'''
For each elt in one arr, look for corresponding elt in other arr. If found mark it as taken in an visited arr, store it in returning arr.
'''

def brute(arr1,arr2):
    vis = [0 for _ in range(len(arr2))]
    intersection=[]
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]==arr2[j] and vis[j]==0:
                intersection.append(arr1[i])
                vis[j] = 1
                break
            
            if arr2[j] > arr1[i]: break
    print(intersection)


#Optimal
'''
Pointers to both arr
if an elt has a equal corresponding elt in the other arr, inc both pointers and append elt to returning arr. 
if elt in first arr less than sec arr elt, inc first pointer(since sorted arr).
otherwise inc sec pointer
'''
def optimal(arr1,arr2):
    i,j=0,0
    intersection=[]
    while i<len(arr1) and j <len(arr2):
        if arr1[i] == arr2[j]:
            intersection.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i] <arr2[j]:
            i+=1
        else:
            j+=1

    print(intersection)



arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]
optimal(arr1,arr2)