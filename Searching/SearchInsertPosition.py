'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

https://leetcode.com/problems/search-insert-position/description/

'''
#concept = lower bound
def optimal(nums,target):
    ans=len(nums)
    l,h=0,len(nums)-1
    while l<=h:
        mid =(l+h)//2
        if nums[mid] >= target:
            ans=mid
            h=mid-1
        else:
            l=mid+1
    return ans
arr = [1,3,5,6]
target = 0

print(optimal(arr,target))