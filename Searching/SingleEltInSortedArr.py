'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

https://leetcode.com/problems/single-element-in-a-sorted-array/description/
'''

def brute(arr):
    n = len(arr)
    if n==1:
        return arr[0]
    for i in range(n):
        if i==0:
            if arr[i+1]!=arr[i]:
                return arr[i]
        elif i==n-1:
            if arr[i]!=arr[i-1]:
                return arr[i]
        else:
            if arr[i]!=arr[i+1] and arr[i]!=arr[i-1]:
                return arr[i]
            
    return -1
# OR you can xor all the elements to get the single elt, same complexity
    #t-O(n) s-O(1)

#Optimal BS
def bs(nums):
    n=len(nums)
    if n==1:
        return nums[0]
    if nums[0]!=nums[1]:
        return nums[0]
    if nums[n-1]!=nums[n-2]:
        return nums[n-1]

    low=1
    high=n-2

    while low<=high:
        mid = (low+high)//2

        if nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]:
            return nums[mid]
        elif (mid%2==0 and nums[mid+1]==nums[mid]) or (mid%2==1 and nums[mid]==nums[mid-1]):
            low=mid+1
        else:
            high=mid-1
    return -1
    

nums = [1,1,2,3,3,4,4,8,8]
print(bs(nums))