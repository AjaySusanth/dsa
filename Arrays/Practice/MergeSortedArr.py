'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

https://leetcode.com/problems/merge-sorted-array/description/
'''

# Two pointer method using an extra array
def brute(arr1,arr2,m,n):
    merge=[]
    i=0
    j=0
    while i<m and j<n:
        if arr1[i] <=arr2[j]:
            merge.append(arr1[i])
            i+=1
        else:
            merge.append(arr2[j])
            j+=1

    while i<m:
        merge.append(arr1[i])
        i+=1

    while j<n:
        merge.append(arr2[j])
        j+=1

    for i in range(len(merge)):
            arr1[i] = merge[i]

'''
Use two pointer, one at the last index of the arr1 and another at the first index of arr2
This is because last index containst the largest of arr1 and first contains the smalles of arr2. Comparing this ensures that the smallest values can be swapped to the first arr and largest to the second arr

After that sort each of them to get the desired arrays
'''
def optimal(arr1,arr2,m,n):
    i=m-1
    j=0

    while i>-1 and j<n:
        if arr1[i] > arr2[j]:
            arr1[i],arr2[j] = arr2[j],arr1[i]
            i-=1
            j+=1
        else:
            break


    arr1[0:m]=sorted(arr1[0:m])
    arr2.sort()

    for i in range(n):
        arr1[m]=arr2[i]
        m+=1


nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
optimal(nums1,nums2,m,n)
print(nums1)