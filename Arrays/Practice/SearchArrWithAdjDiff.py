'''
Given a step array arr[], its step value k, and a key x, we need to find the index of key x in the array arr[]. If multiple occurrences of key x exist, return the first occurrence of the key. In case of no occurrence of key x exists return -1.

Note: A step array is an array of integers where the difference between adjacent elements is at most k. For example: arr[] = [4, 6, 7, 9] and k = 2 is a step array as the difference between the adjacent elements in the arr[] is at most 2.  

https://www.geeksforgeeks.org/problems/searching-in-an-array-where-adjacent-differ-by-at-most-k0456/1
'''



class Solution:
    def findStepKeyIndex(self, arr, k, x):
        # code here
        i=0
        while i<len(arr):
            if arr[i] == x:
                return i
            else:
                diff = arr[i] - x
                i+=max(1,diff//k)
        return -1
