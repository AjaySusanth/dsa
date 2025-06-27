'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

https://leetcode.com/problems/maximum-average-subarray-i/description/
'''

def longest_subarr(arr,k):
    max_sum = float('-inf')
    summ=0
    for i in range(k):
        summ+=arr[i]

    max_sum = max(summ,max_sum)

    for i in range(k,len(arr)):
        summ+=arr[i]
        summ-=arr[i-k]
        max_sum = max(summ,max_sum)

    return max_sum/k





nums = [1,12,-5,-6,50,3]
k = 4
print(longest_subarr(nums,k))
