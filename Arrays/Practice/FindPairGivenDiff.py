'''
Given an array, arr[] and an integer x, return true if there exists a pair of elements in the array whose absolute difference is x, otherwise, return false.
https://www.geeksforgeeks.org/problems/find-pair-given-difference1559/1
'''


from typing import List


class Solution:
    def findPair(self, arr: List[int], x: int) -> int:
        # code here
        arr.sort()
        i=0
        j=1
        while i<len(arr) and j<len(arr):
            if i!=j and arr[j] - arr[i] == x:
                return True
            elif arr[j] - arr[i] > x:
                i+=1
            else:
                j+=1
        return False
        