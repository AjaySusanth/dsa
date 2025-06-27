'''
Given an array of integers arr[]. Find the Inversion Count in the array.
Two elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum. 

https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1
'''

def merge(arr,low,mid,high):
    count=0
    temp=[]
    left=low
    right=mid+1

    while left<=mid and right<=high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            count+=(mid-left+1)
            right+=1
            
    
    while left<=mid:
        temp.append(arr[left])
        left+=1

    while right<=high:
        temp.append(arr[right])
        right+=1

    for i in range(low, high+1):
        arr[i] = temp[i-low]

    return count

def mergeSort(arr,low,high):
    count=0

    if low>=high:
        return count
    mid = (low+high)//2
    count+=mergeSort(arr,low,mid)
    count+=mergeSort(arr,mid+1,high)
    count+=merge(arr,low,mid,high)

    return count

def count_inversion(arr):
    n=len(arr)
    return mergeSort(arr,0,n-1)


arr = [2, 4, 1, 3, 5]

print(count_inversion(arr))
print(arr)
