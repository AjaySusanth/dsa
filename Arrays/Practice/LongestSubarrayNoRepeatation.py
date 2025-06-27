'''
Given a string s, find the length of the longest substring without duplicate characters.

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''
#Sliding window variable length
def long_subarray(s):
    l=0
    sett = set()
    longest = 0
    for r in range(len(s)):
        while s[r] in sett:
            sett.remove(s[l])
            l+=1
        sett.add(s[r])
        length = (r-l)+1
        longest = max(longest,length)
    return longest


s = "abcabcbb"
print(long_subarray(s))