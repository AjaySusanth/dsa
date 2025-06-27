'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

https://leetcode.com/problems/two-sum/description/
'''

def optimal(nums,target):
    n = len(nums)
    hashmap={}
    for i in range(n):
        hashmap[nums[i]] = i
    
    for i in range(n):
        rem = target - nums[i]
        if rem in hashmap and hashmap[rem]!=i:
            return [i,hashmap[rem]]

    #TC - O(n) Sc-O(n)

# Approach if asked to check if there exists two numbers without extra space 2 pointer

def optimal1(nums,target):
    i=0
    j=len(nums) - 1
    nums.sort()
    while i<j:
        if nums[i]+nums[j]==target:
            return True
        elif nums[i]+nums[j]<target:
            i+=1
        else:
            j-=1
    
    return False
    # Tc - O(nlogn)  sc- o(1)
nums = [3,2,5]
target = 6

print(optimal1(nums,target))