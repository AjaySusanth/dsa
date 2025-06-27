'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
'''

# Using lower bounds and upper bounds
def lower_bound(nums,target):
    ans = -1
    l=0
    h = len(nums) - 1
    
    while l<=h:
        mid = (l+h)//2
        
        if nums[mid] >= target:
            ans = mid
            h = mid-1
        else:
            l = mid+1
            
    return ans

def upper_bound(nums,target):
    ans = -1
    l=0
    h = len(nums) - 1
    
    while l<=h:
        mid = (l+h)//2
        
        if nums[mid] > target:
            ans = mid
            h = mid-1
        else:
            l = mid+1
            
    return ans
        

def bounds(nums,target):
    lb = lower_bound(nums,target)
    if lb==-1 or nums[lb]!=target:
        return [-1,-1]
    else:
        up = upper_bound(nums,target)-1
        return [lb,up]


# Using binary search

def first_occurence(nums,target):
    first =-1
    l,h=0,len(nums)-1
    
    while l<=h:
        mid = (l+h)//2
        
        if nums[mid] == target:
            first=mid
            h = mid-1
        elif nums[mid] > target:
            h = mid-1
        else:
            l = mid+1 
    return first

def last_occurence(nums,target):
    last =-1
    l,h=0,len(nums)-1
    
    while l<=h:
        mid = (l+h)//2
        
        if nums[mid] == target:
            last=mid
            l = mid+1
        elif nums[mid] > target:
            h = mid-1
        else:
            l = mid+1 
    return last

def bs(nums,target):
    first = first_occurence(nums,target)
    if first==-1:
        return [-1,-1]
    else:
        last = last_occurence(nums,target)
        return [first,last]
    
    
nums = [5,7,7,8,8,10]
target = 8

print(bs(nums,target))