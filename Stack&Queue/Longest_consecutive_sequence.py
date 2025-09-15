# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hset= set(nums)
        longest=0
        for num in hset:
            if num-1 not in hset:
                next_num = num+1
                length=1
                while next_num in hset:
                    next_num+=1
                    length+=1
                longest = max(longest,length)
        return longest                
        