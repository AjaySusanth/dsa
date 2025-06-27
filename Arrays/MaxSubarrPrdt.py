'''
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

https://leetcode.com/problems/maximum-product-subarray/description/
'''


#Brute - Generate all subarray and get the max prdt

#Optimal

def optimal(arr):
    maxi = float('-inf')
    prefix,suffix=1,1
    n=len(arr)
    for i in range(n):
        if prefix == 0:prefix=1
        if suffix == 0: suffix=1

        prefix *=arr[i]
        suffix*=arr[n-i-1]

        maxi = max(maxi,max(prefix,suffix))

    return maxi

nums = [2,3,-2,4]
print(optimal(nums))


