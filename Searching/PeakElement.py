'''
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

https://leetcode.com/problems/find-peak-element/description/
'''

def brute(nums):
    n = len(nums)
    if n==1:
        return 0
    
    for i in range(n):
        if (i==0 or nums[i]>nums[i-1]) and (i==n-1 or nums[i]>nums[i+1]):
            return i
    return -1

# T-O(N) S-O(1)

def bs(nums):
    n = len(nums)
    if n==1:
        return 0
    if nums[0]>nums[1]:
        return 0
    if nums[n-1]>nums[n-2]:
        return n-1
    
    low,high=1,n-2

    while low<=high:
        mid = (low+high)//2

        if nums[mid]>nums[mid-1] and nums[mid]> nums[mid+1]:
            return mid
        elif nums[mid]>nums[mid-1]:
            low=mid+1
        else:
            high=mid-1
    return -1


nums = [1,2,3,1]
print(bs(nums))
