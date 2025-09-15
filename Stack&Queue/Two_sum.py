# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h={}
        n=len(nums)
        for i in range(n):
            h[nums[i]] = i

        for i in range(n):
            y = target - nums[i]
            if y in h and h[y] !=i:
                return [i,h[y]]
        