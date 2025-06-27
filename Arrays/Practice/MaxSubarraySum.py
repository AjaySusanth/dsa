'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
https://leetcode.com/problems/maximum-subarray/description/
'''

#Brute - Find all subarray and take the max sum

def max_subarr_sum_brute(arr):
    maxx = float('-inf')
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            summ=0
            for k in range(i,j):
                summ+=arr[k]
                maxx = max(summ,maxx)
    return maxx



#Better - Same approach of brute, but optimising the iteration to find sum

def max_subarr_sum_better(arr):
    maxx = float('-inf')
    for i in range(len(arr)):
        summ=0
        for j in range(i,len(arr)):
            summ+=arr[j]
            maxx = max(summ,maxx)

    return maxx

#Optimal  - Kadane's Algo


'''
Iterate through the array
Add it to the sum
Compare with maxx
if sum < 0 => sum=0

'''

def max_subarr_sum_optimal(nums):
    maxx = float('-inf')
    ansStart =-1
    ansEnd =-1
    summ= 0
    for i in range(len(nums)):
        if summ == 0:
            start = i

        summ +=nums[i]

        if summ > maxx:
            maxx =summ
            ansStart,ansEnd = start,i

        if summ <0 :
            summ=0

    print(nums[ansStart:ansEnd+1])
    
    return maxx

        



nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarr_sum_brute(nums))
print(max_subarr_sum_better(nums))
print(max_subarr_sum_optimal(nums))