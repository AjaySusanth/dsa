'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

https://leetcode.com/problems/search-in-rotated-sorted-array/

'''

def search_brute(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i


'''
First find the min index from where it is rotated.
Check if the target is before the rotated sequence or after it.
Trim down the search space accroding to the targeted area
'''
def search_better(nums,target):
    l=0
    r = len(nums) - 1

    while l<r:
        mid = (l+r) // 2

        if nums[mid] > nums[r]:
            l = mid+1
        else:
            r = mid

    min_index = l


    if min_index == 0:
        l=0
        r=len(nums)-1
    elif nums[min_index] == target:
        return min_index
    elif target >= nums[0] and target <= nums[min_index-1]:
        l=0
        r=min_index-1
    else:
        l=min_index+1
        r= len(nums)-1

    while l<=r:
        mid = (l+r)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r=mid-1
        else:
            l=mid+1
    return -1

def search_optimal(nums,target):
    l=0
    r = len(nums) - 1

    while l<=r:
        mid = (l+r) // 2

        if nums[mid] == target:
            return mid
        #left half sorted
        elif nums[l] <= nums[mid]:
            if target >= nums[l] and target < nums[mid]:
                r=mid-1
            else:
                l=mid+1
        #right half sorted
        else:
            if target > nums[mid] and target <= nums[r]:
                l=mid+1
            else:
                r=mid-1

    return -1
        

# With duplicate elements return true\false

'''
edge case is when nums[mid] = nums[l] = nums[r]
then trim down the search space since target elt is not nums[mid] which is checked first
'''

def with_duplicates(nums,target):
    l=0
    r = len(nums) - 1

    while l<=r:
        mid = (l+r) // 2

        if nums[mid] == target:
            return True
        if nums[mid] == nums[l] and nums[mid] == nums[r]:
            l+=1
            r-=1
        #left half sorted
        elif nums[l] <= nums[mid]:
            if target >= nums[l] and target < nums[mid]:
                r=mid-1
            else:
                l=mid+1
        #right half sorted
        else:
            if target > nums[mid] and target <= nums[r]:
                l=mid+1
            else:
                r=mid-1

    return False

nums = [4,5,6,7,0,1,2]
target = 4
#print(search_brute(nums,target))
print(search_better(nums,target))