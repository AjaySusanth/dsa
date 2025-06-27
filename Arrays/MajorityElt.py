'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

https://leetcode.com/problems/majority-element/description/
'''

def better(arr):
    n = len(arr)
    hashmap = {}
    for i in range(n):
        if arr[i] in hashmap:
            hashmap[arr[i]]+=1
        else:
            hashmap[arr[i]] = 1
    for k,v in hashmap.items():
        if v>n//2:
            return k
        
    return -1

def optimal(nums):
    count=0
    candidate = None

    n = len(nums)

    for i in range(n):
        if count==0:
            candidate = nums[i]
            count=1
        elif candidate == nums[i]:
            count+=1
        else:
            count-=1
    count=0
    for num in nums:
        if num == candidate:
            count+=1

    if count > n//2:
        return candidate
    return -1


    

nums = [3,2,3]

print(better(nums))
print(optimal(nums))