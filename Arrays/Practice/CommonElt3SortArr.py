'''
Given three sorted arrays in non-decreasing order, print all common elements in non-decreasing order across these arrays. If there are no such elements return an empty array. In this case, the output will be -1.

https://www.geeksforgeeks.org/problems/common-elements1132/1
'''


def optimal(arr1,arr2,arr3):
    i,j,k=0,0,0
    comm = []
    while i<len(arr1) and j<len(arr2) and k<len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            comm.append(arr1[i])
            i+=1
            j+=1
            k+=1
        elif arr1[i] < arr2[j]:
            i+=1
        elif arr2[j] < arr3[k]:
            j+=1
        else:
            k+=1

    return comm        


arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

print(optimal(arr1,arr2,arr3))