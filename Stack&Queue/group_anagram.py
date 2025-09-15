# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        h = defaultdict(list)
        for word in strs:
            count = [0] * 26

            for i in word:
                index = ord(i) - ord('a')
                count[index]+=1
            
            key = tuple(count)
            h[key].append(word)

        return h.values()

