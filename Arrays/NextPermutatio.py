'''
https://leetcode.com/problems/next-permutation/description/
'''

def optimal(nums):

    n=len(nums) -1
    index = -1
    for i in range(n-2,-1,-1):
        if nums[i]< nums[i+1]:
            index = i
            break

    if index==-1:
        return nums[::-1]
    
    for i in range(n-1,i,-1):
        if nums[i] > nums[index]:
            nums[i],nums[index] = nums[index],nums[i]
            break
    nums[index+1:n-1] = nums[index+1:n-1][::-1]
    return nums


def optimal1(nums):
        n = len(nums)
        index = -1
        for i in range(n-2,-1,-1):
            if nums[i]< nums[i+1]:
                index = i
                break

        if index==-1:
            nums[0:n] = nums[0:n][::-1]
        else:
            for i in range(n-1,i,-1):
                if nums[i] > nums[index]:
                    nums[i],nums[index] = nums[index],nums[i]
                    break
            nums[index+1:n] = nums[index+1:n][::-1]

nums = [3,2,1]
optimal1(nums)
print(nums)